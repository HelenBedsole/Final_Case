#!/usr/bin/env bash
set -euo pipefail

# run from docker/ directory
# usage: ./run.sh up|down
CMD=${1:-up}

case "$CMD" in
  up)
    docker volume create n8n_data || true
    docker-compose up -d
    echo "n8n started at http://localhost:5678"
    ;;
  down)
    docker-compose down
    echo "n8n stopped"
    ;;
  logs)
    docker-compose logs -f
    ;;
  *)
    echo "Usage: $0 {up|down|logs}"
    exit 1
    ;;
esac
