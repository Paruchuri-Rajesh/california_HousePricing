FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default port (overridden by hosting providers)
ENV PORT=8000

# Expose the port
EXPOSE $PORT

# Run the app with proper bind syntax
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:$PORT", "app:app"]
