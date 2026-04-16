from fastapi import FastAPI
from app.routes import auth, projects, donations
from app.core.database import engine, Base

# Create tables if they don't exist (useful for simple setups, normally Alembic handles this)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PDT-doacao",
    description="Plataforma de Doações Transparentes para Projetos Locais",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(donations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PDT-doacao API"}
