# PDT-doacao
Plataforma de Doações Transparentes para Projetos Locais

## Problema
Falta de transparência e rastreabilidade nas doações locais, dificultando o engajamento e a confiança do doador.

## Solução
Uma plataforma centralizada e transparente que conecta doadores a projetos locais, fornecendo métricas claras e recibos rastreáveis das doações.

## Stack
- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Docker & Docker Compose
- pytest

## Como rodar

1. Clone o repositório.
2. Copie `.env.example` para `.env` e ajuste se necessário.
3. Suba a aplicação com Docker Compose:
   ```bash
   docker-compose up --build
   ```
4. A API estará disponível em `http://localhost:8000`. A documentação interativa Swagger estará em `http://localhost:8000/docs`.

## Endpoints Principais
- `POST /register`: Cria um novo usuário.
- `POST /login`: Retorna o token JWT para acesso.
- `POST /projects/`: Cria um novo projeto.
- `GET /projects/`: Lista os projetos.
- `POST /donations/`: Cria uma doação vinculada a um projeto e um usuário (requer autenticação JWT). Retorna a doação com um `receipt_hash` para rastreabilidade.
