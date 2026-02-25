# Start with a lightweight Linux Python runtime
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies first (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Explicitly set where the model artifact will be saved and loaded from
ENV MODEL_PATH=/app/sentinela_model.pkl

# By default, run the offline ML brain to generate the model artifact
CMD ["python", "engine.py"]
