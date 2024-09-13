FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# Install dependencies directly into the app source directory
RUN pip install --target=/app requests

# Use a full Python runtime instead of distroless
FROM python:3-slim
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["python", "/app/donate.py"]
