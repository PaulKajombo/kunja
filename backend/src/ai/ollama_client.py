"""
Ollama LLM integration for Kunja.

This module provides local LLM inference using Ollama.
No API keys or forex needed - runs 100% locally.

Setup:
    1. Install Ollama: https://ollama.com
    2. Pull model: ollama pull llama3.2
    3. Ollama runs on http://localhost:11434
"""

import httpx
from src.config import settings


async def chat_completion(messages: list[dict], model: str = None) -> str:
    """
    Send a chat completion request to Ollama.

    Args:
        messages: List of message dicts with 'role' and 'content'
        model: Model name (defaults to settings.OLLAMA_MODEL)

    Returns:
        The assistant's response text
    """
    model = model or settings.OLLAMA_MODEL

    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            f"{settings.OLLAMA_HOST}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": False,
            },
        )
        response.raise_for_status()
        result = response.json()
        return result["message"]["content"]


async def analyze_document(
    document_text: str,
    document_type: str = "general",
    target_country: str = "Malawi",
) -> dict:
    """
    Analyze a document for cross-border compliance using Ollama.

    Args:
        document_text: Extracted text from the document
        document_type: Type of document (contract, policy, etc.)
        target_country: Country where business is being established

    Returns:
        Dict with findings and compliance assessment
    """
    system_prompt = f"""You are a cross-border compliance expert specializing in 
Malawi and Zambia business regulations.

Analyze the uploaded document for compliance with {target_country} regulations.
Focus on:
- Business registration requirements
- Tax compliance (VAT, PAYE, corporate tax)
- Employment law compliance
- Data protection requirements
- Work permit and immigration requirements

Return your analysis as JSON with this structure:
{{
    "findings": [
        {{
            "issue": "description of the issue",
            "severity": "critical|high|medium|low",
            "act_reference": "name of the relevant act",
            "recommendation": "what needs to be done"
        }}
    ],
    "overall_compliance": 0.0-1.0,
    "summary": "brief summary of compliance status"
}}
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"Document type: {document_type}\n\nDocument content:\n{document_text}",
        },
    ]

    response = await chat_completion(messages)

    # Try to parse JSON from response
    import json
    try:
        # Find JSON in the response (it might be wrapped in markdown)
        start = response.find("{")
        end = response.rfind("}") + 1
        if start != -1 and end != -1:
            return json.loads(response[start:end])
    except json.JSONDecodeError:
        pass

    # Fallback: return raw response
    return {
        "findings": [
            {
                "issue": "AI analysis completed",
                "severity": "info",
                "act_reference": "N/A",
                "recommendation": response[:500],
            }
        ],
        "overall_compliance": 0.5,
        "summary": "Analysis completed - review findings above",
    }


async def check_ollama_health() -> bool:
    """Check if Ollama server is running."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{settings.OLLAMA_HOST}/api/tags")
            return response.status_code == 200
    except Exception:
        return False


async def ask_about_journey(context: dict) -> str:
    """
    Answer a user's question about their market-entry journey using Ollama.

    The context contains the user's journey profile, the specific step
    (or whole journey), and their question. The AI explains requirements
    in plain language and points to official sources.
    """
    # Build a readable text context from the structured data
    journey = context.get("journey", {})
    question = context.get("question", "")

    context_lines = [
        f"Company: {journey.get('company_name', 'N/A')}",
        f"Route: {journey.get('origin_country', '?')} → {journey.get('target_country', '?')}",
        f"Industry: {journey.get('industry', 'N/A')}",
        f"Business model: {journey.get('business_model', 'N/A')}",
    ]
    if journey.get("business_description"):
        context_lines.append(
            f"Business description: {journey['business_description']}"
        )

    if "step" in context:
        step = context["step"]
        context_lines.append("\n--- CURRENT STEP ---")
        context_lines.append(f"Phase: {step.get('phase', 'N/A')}")
        context_lines.append(f"Step: {step.get('title', 'N/A')}")
        context_lines.append(f"What it is: {step.get('description', '')}")
        context_lines.append(f"Why needed: {step.get('why_needed', '')}")
        if step.get("authority"):
            context_lines.append(f"Responsible authority: {step['authority']}")
        if step.get("documents_needed"):
            context_lines.append(
                f"Documents needed: {', '.join(step['documents_needed'])}"
            )
        if step.get("estimated_cost"):
            context_lines.append(f"Estimated cost: {step['estimated_cost']}")
        if step.get("estimated_timeline"):
            context_lines.append(f"Estimated timeline: {step['estimated_timeline']}")
        if step.get("official_source"):
            context_lines.append(f"Official source: {step['official_source']}")
        context_lines.append(f"Current status: {step.get('status', 'N/A')}")
    elif "phases" in context:
        context_lines.append("\n--- JOURNEY OVERVIEW ---")
        for phase in context.get("phases", []):
            steps_str = "; ".join(
                f"{s['title']} ({s['status']})" for s in phase.get("steps", [])
            )
            context_lines.append(f"{phase.get('name', 'Phase')}: {steps_str}")

    system_prompt = (
        "You are Kunja, a friendly, expert guide helping businesses enter "
        "Malawi and Zambian markets. You are embedded inside a market-entry "
        "roadmap app. Answer the user's question clearly and helpfully using "
        "the provided journey context. Always:\n"
        "1. Answer directly in plain language — no jargon\n"
        "2. Reference the specific step/requirement they're asking about\n"
        "3. Mention official sources/authorities where relevant\n"
        "4. Be practical and action-oriented — tell them what to do next\n"
        "5. If the question is outside your knowledge, say so honestly and "
        "recommend consulting the official authority\n"
        "Keep answers under 250 words unless the question needs more detail. "
        "Do NOT invent fees, timelines, or regulations that are not in the context."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": (
                "JOURNEY CONTEXT:\n"
                + "\n".join(context_lines)
                + f"\n\nUSER QUESTION: {question}"
            ),
        },
    ]

    return await chat_completion(messages)
