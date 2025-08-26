FROM python:3.9-slim

# Prevent Python from writing .pyc files and enable stdout/stderr buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	wget \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first for better layer caching
COPY requirements.txt ./

# Install Python deps (including TensorFlow CPU)
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source
COPY . .

# Expose port
EXPOSE 8080

# Default command runs the FastAPI app
CMD ["python", "app.py"]

