#!/bin/sh
set -e

# Start Ollama server in background
ollama serve &

# Wait until Ollama server responds
echo "Waiting for Ollama server..."
until curl -sSf http://localhost:11434/api/tags >/dev/null 2>&1; do
  sleep 1
done

# If model not present, pull it in background (non-blocking)
if ! ollama list | grep -q "gemma:2b"; then
  echo "Pulling gemma:2b in background..."
  ollama pull gemma:2b || true &
fi

# Keep container alive (wait for any background job)
wait -n
