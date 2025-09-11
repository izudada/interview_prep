FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    curl \
    # software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8502

# Start Streamlit app
CMD ["streamlit", "run", "index.py", "--server.port=8502", "--server.address=0.0.0.0"]