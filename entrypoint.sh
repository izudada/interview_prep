#!/bin/sh
set -e

echo "Pulling gemma:2b..."
ollama pull gemma:2b || true

echo "Initializing gemma:2b (first run)..."
# Run it once with a simple prompt, then kill (forces registration)
echo "Hello" | ollama run gemma:2b > /dev/null || true

echo "Starting Ollama server..."
exec ollama serve
