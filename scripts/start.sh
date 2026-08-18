#!/bin/bash
# Start the Aion server
PORT=${1:-3000}

# Kill any existing server on that port
fuser -k $PORT/tcp 2>/dev/null
sleep 0.5

cd "$(dirname "$0")/.."
echo "Starting Aion on http://localhost:$PORT"
python3 -m http.server $PORT &
echo "PID: $!"
echo "Stop with: ./scripts/stop.sh"
