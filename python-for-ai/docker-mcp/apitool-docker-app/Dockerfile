FROM python:3.14-slim

WORKDIR /app

# Install uv for faster dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Copy application code
COPY imageapi.py ./
COPY configsettings.docker.py ./configsettings.py

# Copy SSL certificates from root directory
COPY key.pem cert.pem ./

# Create images directory
RUN mkdir -p images

# Expose HTTPS port
EXPOSE 8443

# Run the application using uv
CMD ["uv", "run", "python", "imageapi.py"]
