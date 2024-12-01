#!/usr/bin/env bash

set -euo pipefail
dirs="$@"

for d in "${dirs[@]}"; do
    pushd "$d" > /dev/null
    git fetch upstream
    git reset --hard upstream/master
    git push origin master --force
    popd > /dev/null
done
