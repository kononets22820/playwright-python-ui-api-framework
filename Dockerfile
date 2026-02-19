FROM python:3.12-slim

WORKDIR /app

# System deps for Playwright browsers
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip \
    && pip install playwright pytest pytest-xdist \
    && playwright install --with-deps

# default command (can be overridden)
CMD ["pytest", "-m", "smoke or api", "-n", "2", "-q"]
