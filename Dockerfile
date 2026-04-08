# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first (for layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --timeout=120 -r requirements.txt

# Copy the rest of the app
COPY . .

# Don't run as root — security best practice
RUN useradd -m appuser
USER appuser

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]