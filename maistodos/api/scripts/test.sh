#!/usr/bin/env bash



test(){
    set -e
    set -x

    pytest --cov=app --cov-report=term-missing tests "${@}"
}

if [ "$(basename "$current_dir")" = "maistodos" ]; then
    test
else
    cd maistodos/api
    test
fi
