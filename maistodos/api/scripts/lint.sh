#!/usr/bin/env bash

current_dir=$(pwd)

linter() {
    set -x

    mypy app
    black app --check
    isort --recursive --check-only app
    flake8 -v
}

if [ "$(basename "$current_dir")" = "maistodos" ]; then
    linter
else
    cd maistodos
    linter
fi
