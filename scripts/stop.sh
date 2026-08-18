#!/bin/bash
# Stop all Aion servers
pkill -f "http.server" 2>/dev/null
echo "All servers stopped."
