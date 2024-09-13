FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# Install requests and importlib-metadata (backport) for compatibility
RUN pip install --target=/app requests importlib-metadata

# Use distroless image with a minimal Python runtime
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/donate.py"]
