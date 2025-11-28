FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
# Встановити залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
# Скопіювати весь код у контейнер
COPY . .

# Ensure logs appear immediately (no buffering)
# Логи одразу виводити в консоль
ENV PYTHONUNBUFFERED=1

# DATABASE_URL can come from .env (locally) or GitHub Actions secrets (CI/CD)
# URL бази будемо передавати при запуску контейнера
# DATABASE_URL приходить з .env або з секретів у GitHub Actions
ENV DATABASE_URL=""  

# ENTRYPOINT:
# 1) Run Alembic migrations
# 2) Start FastAPI with Uvicorn

# ЗАПУСК:
# 1) Прогнати Alembic міграції
# 2) Запустити FastAPI через uvicorn

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]