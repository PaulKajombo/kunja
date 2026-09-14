from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import auth, checklists, analyze, regulations, dashboard

app = FastAPI(
    title="Kunja API",
    description="Cross-border compliance tool for Malawi ↔ Zambia",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(checklists.router, prefix="/api/v1/checklists", tags=["Checklists"])
app.include_router(analyze.router, prefix="/api/v1/analyze", tags=["Document Analysis"])
app.include_router(regulations.router, prefix="/api/v1/regulations", tags=["Regulations"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["Dashboard"])


@app.get("/")
def root():
    return {
        "app": "Kunja",
        "description": "Cross-border compliance tool for Malawi ↔ Zambia",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
