# ------------------------------
# 1️⃣ Base image (Python 3.13 slim)
# ------------------------------
FROM python:3.13-slim AS base

# Prevent Python from writing pyc files & buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (optional: for building deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------
# Install dependencies
# ------------------------------
# Copy the requirements file first (to leverage Docker cache)
COPY web/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || \
    pip install --no-cache-dir fastapi uvicorn

# ------------------------------
# 3️⃣ Copy the source code
# ------------------------------
COPY . /app

# ------------------------------
# 4️⃣ Expose app port
# ------------------------------
EXPOSE 8000

# ------------------------------
# 5️⃣ Run FastAPI via Uvicorn
# ------------------------------
CMD ["uvicorn", "web.app:app", "--host", "0.0.0.0", "--port", "8000"]
# Use official Python image
FROM python:3.13-slim

# Set work directory inside container
WORKDIR /app

# Copy root requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy web requirements and install
COPY web/requirements.txt ./web/
RUN pip install --no-cache-dir -r web/requirements.txt

# Copy the full application code
COPY . . 

# Expose FastAPI port
EXPOSE 8000

# Set environment variable for uvicorn to reload automatically (optional for dev)
ENV PYTHONUNBUFFERED=1

# Default command to run FastAPI web server
CMD ["uvicorn", "web.app:app", "--host", "0.0.0.0", "--port", "8000"]
