FROM python:3.10-slim

WORKDIR /app

# Install system deps often needed for python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 8502

CMD ["streamlit", "run", "index.py", "--server.port=8502", "--server.address=0.0.0.0"]
