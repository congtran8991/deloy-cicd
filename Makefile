.PHONY: install dev run test lint clean docker-build docker-up docker-down db-create

# ─── Local Development ───────────────────────────────────

## Create virtual environment & install dependencies
install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

## Start dev server with auto-reload
dev:
	. venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## Start production server
run:
	. venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

## Create database tables
db-create:
	. venv/bin/activate && python -c "from app.core.database import Base, engine; Base.metadata.create_all(bind=engine); print('Database tables created!')"

# ─── Quality ─────────────────────────────────────────────

## Run tests
test:
	. venv/bin/activate && pip install -q pytest httpx && pytest tests/ -v --tb=short

## Run linter
lint:
	. venv/bin/activate && pip install -q ruff && ruff check app/ && ruff format --check app/

## Auto-format code
format:
	. venv/bin/activate && pip install -q ruff && ruff check --fix app/ && ruff format app/

# ─── Docker ──────────────────────────────────────────────

## Build Docker image
docker-build:
	docker build -t fastapi-app .

## Start with docker-compose
docker-up:
	docker compose up -d

## Stop containers
docker-down:
	docker compose down

# ─── Cleanup ─────────────────────────────────────────────

## Remove cache & temp files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; \
	find . -type f -name "*.pyc" -delete 2>/dev/null; \
	rm -f app.db; \
	echo "Cleaned!"
