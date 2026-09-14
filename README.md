# Kunja 🇲🇼 ↔ 🇿🇲

Cross-border compliance tool for businesses expanding between **Malawi** and **Zambia**.

## What is Kunja?

Kunja helps:
- **Malawians** establish businesses in Zambia
- **Zambians** establish businesses in Malawi

### Features
- Cross-border compliance checklists
- AI-powered document analysis (runs locally via Ollama)
- Regulatory tracking for both countries
- Work permit guidance
- Tax compliance tracking

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3.11 + FastAPI |
| Frontend | React 18 + TypeScript |
| Database | PostgreSQL 16 |
| AI/LLM | Ollama (Llama 3.2-8B, local) |
| Containerization | Docker + Docker Compose |

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Ollama (for AI features)

### 1. Start with Docker
```bash
docker-compose up
```

### 2. Or run locally

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn src.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### 3. Set up Ollama (for AI features)
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull models
ollama pull llama3.2
ollama pull mistral
```

## Project Structure

```
kunja/
├── backend/           # FastAPI backend
│   ├── src/
│   │   ├── api/       # API endpoints
│   │   ├── ai/        # Ollama LLM integration
│   │   └── models/    # Database models
│   └── requirements.txt
├── frontend/          # React frontend
│   ├── src/
│   │   ├── pages/
│   │   └── components/
│   └── package.json
├── docs/              # Documentation
│   ├── spec.md        # Technical specification
│   └── roadmap.md     # Project roadmap
└── docker-compose.yml
```

## Malawi Compliance Framework

### Regulations Tracked
- Companies Act (Chapter 49:03)
- Income Tax Act (Chapter 44:06)
- Data Protection Act (Chapter 4:10)
- Employment Act (Chapter 4:03)
- Immigration Act (Chapter 15:08)
- VAT Act (Chapter 4:05)

## Zambia Compliance Framework

### Regulations Tracked
- Companies Act No. 10 of 2017
- Income Tax Act No. 12 of 2015
- Data Protection Act No. 3 of 2021
- Employment Code Act No. 3 of 2019
- Immigration and Deportation Act
- VAT Act No. 12 of 2018
- Citizens Economic Empowerment Act

## License

Private - All rights reserved.
