#!/usr/bin/env bash
set -euo pipefail

script_dir="$(dirname "${BASH_SOURCE[0]}")"
cd "$script_dir"

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ -f 'env.sh' ]; then
    . env.sh
fi

waitress-serve --port="${PORT-5000}" 'hooks:app'
