# FastAPI Project

A modern, production-ready FastAPI application with a clean architecture.

## 📁 Project Structure

```
app/
├── main.py                     # FastAPI app entry point
├── api/                        # API layer (routes + schemas)
│   └── v1/
│       ├── router.py           # Aggregates all v1 routers
│       ├── endpoints/
│       │   └── items.py        # Item CRUD endpoints
│       └── schemas/
│           └── item.py         # Pydantic request/response schemas
├── constants/                  # App-wide constants & enums
│   └── common.py
├── core/                       # Core config & infrastructure
│   ├── config.py               # Settings (loaded from .env)
│   └── database.py             # SQLAlchemy engine & session
├── middleware/                  # Custom middleware
│   └── cors.py                 # CORS configuration
├── models/                     # SQLAlchemy ORM models
│   └── item.py
└── utils/                      # Utilities & service logic
    ├── crud.py                 # Generic CRUD helpers
    └── item_service.py         # Item business logic
```

## 🚀 Quick Start

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env if needed
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at **http://127.0.0.1:8000**

## 📖 API Documentation

| URL | Description |
|-----|-------------|
| `/docs` | Swagger UI (interactive) |
| `/redoc` | ReDoc (read-only) |
| `/health` | Health check endpoint |

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/items/` | List items (pagination + filter) |
| `GET` | `/api/v1/items/{id}` | Get item by ID |
| `POST` | `/api/v1/items/` | Create a new item |
| `PATCH` | `/api/v1/items/{id}` | Partially update an item |
| `DELETE` | `/api/v1/items/{id}` | Delete an item |
