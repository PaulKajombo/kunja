# Kunja - Technical Specification

## Overview
**Kunja** is a cross-border compliance and regulatory tool for businesses expanding between Malawi and Zambia, with AI-powered assistance for compliance gap assessment, document analysis, and regulatory monitoring.

### Core Concept
- **MVP Focus**: Malawi ↔ Zambia cross-border business compliance
- **Primary Users**: Malawians establishing businesses in Zambia AND Zambians establishing businesses in Malawi
- **Initial Focus Areas**: Business registration, tax compliance, employment law, work permits, cross-border trade
- **AI Integration**: Document analysis, compliance gap assessment, regulatory alerts
- **Target Users**: SMEs (5-200 employees), legal teams, business founders, cross-border traders
- **Expansion Path**: Malawi/Zambia → Africa (Kenya, Nigeria, South Africa, Ghana, Zimbabwe, etc.)

---

## Tech Stack (MVP)

### Backend
- **Framework**: Python 3.11+ with FastAPI
- **Database**: PostgreSQL (compliance data, user data, regulatory framework)
- **AI/ML**: Ollama (local LLM inference)
- **LLM Models**: Llama 3.2-8B, Mistral 7B, or Hermes 3 via Ollama
- **Authentication**: JWT-based auth with FastAPI Security

### AI/ML: Ollama (Local LLM Inference)

**Why Ollama:**
- Free and open-source
- No forex/API costs - runs 100% locally
- Works offline
- No data leaves your machine (privacy-first)
- One-command model downloads

**Models to Use (via Ollama):**
| Model | Size | RAM Needed | Use Case |
|-------|------|------------|----------|
| `llama3.2` | 8B | 8GB | Document analysis, Q&A |
| `mistral` | 7B | 8GB | Fast compliance queries |
| `hermes3` | 8B | 8GB | Conversational assistant |
| `phi3` | 3.8B | 4GB | Lightweight fallback |

**Setup:**
```bash
# Install Ollama (Linux/Mac/Windows)
curl -fsSL https://ollama.com/install.sh | sh

# Pull models
ollama pull llama3.2
ollama pull mistral

# Run locally
ollama run llama3.2
```

**Python Integration:**
```bash
pip install ollama
# or
pip install langchain-ollama  # For LangChain integration
```

**Hardware Requirements:**
- Minimum: 8GB RAM, any modern CPU
- Recommended: 16GB RAM, dedicated GPU (RTX 3060+)
- Production: Cloud VM with GPU ($15-30/month) or dedicated server

### Frontend
- **Framework**: React 18+ with TypeScript
- **UI Library**: Tailwind CSS + shadcn/ui
- **State Management**: Zustand or Context API

### DevOps
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Hosting**: Vercel (frontend) + Render/Supabase (backend)

---

## MVP Feature Scope

### 1. Compliance Checklist Engine
- Cross-border compliance questionnaires ("I'm Malawian, starting a business in Zambia")
- Automated gap assessment based on user responses
- Risk scoring for compliance areas
- Exportable checklist reports (PDF/Markdown)

### 2. AI Document Analyzer
- Upload and analyze business documents (contracts, policies, terms)
- Cross-border compliance flagging (both Malawi and Zambia regulations)
- Red flag detection for common compliance gaps
- Actionable remediation recommendations

### 3. Regulatory Change Tracker
- Malawi AND Zambia regulatory updates (dual-country monitoring)
- AI-summarized changes to regulations in both countries
- Custom alert settings (topic, severity, affected areas, which country)
- Historical change tracking
- Expandable to other African countries over time

### 4. Compliance Dashboard
- Overall compliance score per country
- Timeline of compliance activities
- Document repository
- Task management for remediation

---

## Project Structure

```
kunja/
├── docs/                    # Documentation
│   ├── spec.md             # This file
│   ├── architecture.md     # System architecture
│   ├── malawi-framework.md # Malawi regulations framework
│   └── zambia-framework.md # Zambia regulations framework
├── backend/
│   ├── src/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Core business logic
│   │   ├── models/         # Database models
│   │   │   ├── compliance/ # Country-specific compliance models
│   │   │   ├── malawi/     # Malawi-specific models
│   │   │   └── zambia/     # Zambia-specific models
│   │   ├── ai/             # AI/LLM integration
│   │   └── utils/          # Utilities
│   ├── tests/
│   ├── requirements.txt
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── countries/  # Country-specific dashboards
│   │   │   ├── malawi/     # Malawi-specific pages
│   │   │   └── zambia/     # Zambia-specific pages
│   │   ├── lib/            # Helpers, API clients
│   │   └── hooks/
│   ├── public/
│   ├── package.json
│   └── tailwind.config.ts
├── docker-compose.yml
└── README.md
```

---

## API Endpoints (MVP)

### Compliance Checklists (Cross-border)
- `POST /api/v1/checklists` - Create cross-border compliance checklist
- `GET /api/v1/checklists/:id` - Get checklist details
- `PUT /api/v1/checklists/:id` - Update checklist
- `GET /api/v1/checklists/:id/export` - Export checklist
- `GET /api/v1/checklists?origin=mw&target=zm` - Filter by origin/target country

### Document Analysis
- `POST /api/v1/analyze` - Upload document for analysis
- `GET /api/v1/analyze/:task_id` - Get analysis results

### Regulatory Updates (Dual-country)
- `GET /api/v1/regulations/malawi` - List Malawi regulations
- `GET /api/v1/regulations/zambia` - List Zambia regulations
- `GET /api/v1/regulations/:country/:id/updates` - Get updates for regulation

### Dashboard
- `GET /api/v1/dashboard/compliance-score` - Overall compliance score (both countries)
- `GET /api/v1/dashboard/timeline` - Compliance activity timeline

### Document Analysis
- `POST /api/v1/analyze` - Upload document for analysis
- `GET /api/v1/analyze/:task_id` - Get analysis results

### Regulatory Updates
- `GET /api/v1/regulations` - List regulations
- `GET /api/v1/regulations/:id/updates` - Get updates for regulation
- `POST /api/v1/alerts` - Create alert preferences

### Dashboard
- `GET /api/v1/dashboard/compliance-score` - Overall compliance score
- `GET /api/v1/dashboard/timeline` - Compliance activity timeline

---

## Data Models (Simplified)

### Compliance Checklist
```python
{
    "id": str,
    "country": str,  # e.g., "Malawi"
    "regulation": str,  # e.g., "Companies Act"
    "company_profile": dict,
    "questions_answered": list,
    "gap_analysis": list,
    "ai_findings": list,  # Optional AI analysis results
    "risk_score": float,
    "created_at": datetime,
    "updated_at": datetime
}
```

### Document Analysis Result
```python
{
    "id": str,
    "document_url": str,
    "document_type": str,  # "tax_contract", "privacy_policy", "employment_contract"
    "analysis_method": str,  # "ollama_llm", "rule_based", "hybrid"
    "llm_model_used": str,  # "llama3.2", "mistral", "hermes3"
    "findings": [
        {
            "issue": str,
            "severity": "critical" | "high" | "medium" | "low",
            "act_reference": str,  # e.g., "Companies Act Section 42"
            "malawi_law_reference": str,  # e.g., "Chapter 49:03, Section 42"
            "recommendation": str,
            "confidence": float  # 0-1, LLM confidence score
        }
    ],
    "overall_compliance": float,
    "generated_at": datetime
}
```

---

## AI Integration Points

### 1. Document Analysis Pipeline
```
Upload → Extract Text → Ollama LLM Analysis → Generate Report
          ↓
    (Llama 3.2-8B via Ollama, running locally)
```

#### Document Processing Steps:
1. **PDF/Document Parsing**: PyMuPDF, pdfplumber, python-docx
2. **Text Chunking**: Semantic chunking (LangChain/Unstructured)
3. **Local LLM Inference**: Llama 3.2-8B via Ollama (localhost:11434)
4. **Structured Output**: Pydantic models for compliance findings

#### Ollama API Call Example:
```python
import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'system',
            'content': '''You are a Malawi compliance expert. 
            Analyze this document for compliance with:
            - Companies Act (Chapter 49:03)
            - Income Tax Act (Chapter 44:06)
            - Data Protection Act (Chapter 4:10)
            - Employment Act (Chapter 4:03)
            
            Return JSON with findings array.'''
        },
        {
            'role': 'user', 
            'content': f'Analyze this document:\n\n{document_text}'
        }
    ]
)
```

### 2. Compliance Gap Assessment
- User profile → Rule engine → Gap identification → AI validation
- Use LLM to cross-reference answers against regulatory requirements

### 3. Regulatory Alert Summarization
- RSS feed → Filter → LLM summarization (local Llama 3.2) → User alert

---

## Compliance Framework (Malawi MVP)

### Key Regulations to Track
1. **Companies Act (Chapter 49:03)** - Business registration, directors duties, filing requirements
2. **Income Tax Act (Chapter 44:06)** - Corporate tax, VAT, PAYE, tax filings
3. **Data Protection Act (Chapter 4:10)** - Malawi's GDPR equivalent (2021 Act)
4. **Employment Act (Chapter 4:03)** - Labour laws, contracts, termination, benefits
5. **Companies and Pensions Act** - Pension fund compliance
6. ** excise Act** - Specific industry regulations

### Compliance Categories
1. **Business Registration & Licensing**
   - Company registration (Registrar General)
   - Business name registration
   - Sector-specific licenses

2. **Tax Compliance**
   - VAT registration and filing
   - PAYE for employees
   - Corporate income tax
   - Tax clearance certificates

3. **Employment Law**
   - Employment contracts
   - Working hours and leave
   - Termination procedures
   - Social security contributions

4. **Data Protection**
   - Privacy policy requirements
   - Data subject rights
   - Data breach notification
   - Cross-border data transfers

---

## Development Roadmap

### Phase 1: Foundation (Weeks 1-4)
- [ ] Project setup and CI/CD
- [ ] Database schema design (Malawi regulatory framework)
- [ ] Basic API structure
- [ ] User authentication

### Phase 2: Malawi Compliance Engine (Weeks 5-8)
- [ ] Malawi compliance questionnaire framework (Companies Act, Tax Act, Data Protection Act, Employment Act)
- [ ] Gap assessment logic for Malawi regulations
- [ ] Risk scoring algorithm for Malawi-specific issues
- [ ] Checklist export functionality

### 2. Malawi AI Integration (Weeks 9-12)
- [ ] Document upload and processing
- [ ] Malawi-specific contract analysis (tax, employment, commercial)
- [ ] Local LLM integration (Llama 3.2-8B via Ollama or Hugging Face)
- [ ] Compliance flagging for Malawi regulations
- [ ] Rule-based fallback for high-confidence checks

### Phase 4: Malawi Dashboard (Weeks 13-16)
- [ ] Malawi-specific dashboard
- [ ] Document analysis interface
- [ ] Compliance checklist UI
- [ ] Regulatory alert system (Malawi sources)

### Phase 5: Testing & Malawi Launch (Weeks 17-18)
- [ ] User testing with Malawi businesses
- [ ] Legal review of compliance checks
- [ ] Security review
- [ ] Documentation
- [ ] Launch MVP for Malawi

### Phase 6: Africa Expansion (Weeks 19-24)
- [ ] Country expansion framework (modular country support)
- [ ] Kenya compliance framework
- [ ] Nigeria compliance framework
- [ ] South Africa compliance framework
- [ ] Multi-country dashboard

---

## Malawi-Specific Compliance Sources

### Regulatory Authorities
1. **Registar General's Office (RGO)** - Business registration, Companies House
2. **Malawi Revenue Authority (MRA)** - Tax collection, VAT, PAYE
3. **Malawi Data Protection Society (MDPS)** - Data protection oversight
4. **Labour Office** - Employment law enforcement

### Key Legislation
- Companies Act (Chapter 49:03)
- Income Tax Act (Chapter 44:06)
- Data Protection Act (Chapter 4:10)
- Employment Act (Chapter 4:03)
- Value Added Tax Act (Chapter 4:05)
- Social Security Act (Chapter 4:02)

## Success Metrics (Malawi MVP)
- 90%+ accuracy on sample compliance checks
- Document analysis completed in <2 minutes
- Regulatory alerts delivered within 24 hours of publication
- User compliance score generation in <30 seconds

---

## Risks & Mitigations
1. **AI hallucination**: Implement confidence scoring, rule-based fallback, and human review prompts
2. **Regulatory complexity**: Start with narrow scope, expand gradually
3. **Data privacy**: Ensure self-hosting capability for enterprise clients
4. **Legal liability**: Include clear disclaimers and audit trail features
5. **Local LLM performance**: Test on target hardware (Ryzen 5/i5 minimum for 8B models)
6. **No internet dependency**: Local LLMs work offline, no forex issues

---

## Next Steps
1. Review and approve this specification
2. Set up development environment
3. Create detailed architecture diagram
4. Begin Phase 1 implementation

---

*Version: 1.0 | Date: 2026-09-04*