FROM python:3.14-slim

WORKDIR /app

# Install uv for faster dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Copy application code
COPY imageapi.py webapp.py start.sh ./
COPY configsettings.docker.py ./configsettings.py

# Copy SSL certificates from root directory
COPY key.pem cert.pem ./

# Copy images folder with all images
COPY images/ ./images/

# Copy Flask templates
COPY templates/ ./templates/

# Make start script executable
RUN chmod +x start.sh

# Expose HTTPS ports (8443 for API, 8080 for web app)
EXPOSE 8443 8080

# Run both applications using the start script
CMD ["./start.sh"]
