# Base image from docker hub
FROM python:3.12-slim

# Working directory inside the container
WORKDIR /app

# Python dependencies (layer: dependencies)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and data (layer: application code)
COPY src/ ./src/
COPY data/ ./data/

# Command to run the game (layer: run app)
CMD ["python", "-m", "src.game"]
