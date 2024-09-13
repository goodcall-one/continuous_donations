# Use python:3-alpine for a small but complete Python environment
FROM python:3-alpine AS builder

# Add application files
ADD . /app
WORKDIR /app

# Install dependencies directly into the app source directory
RUN pip install --target=/app requests

# Final stage with alpine
FROM python:3-alpine
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app

# Run the Python script
CMD ["python", "/app/donate.py"]
