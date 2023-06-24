#!/bin/sh
set -e

# Work directory
cd "$PROJECT_PATH"

# shellcheck disable=SC2039
if [[ "$CONFIG" == "testing" ]]; then
    echo "Run testing mode"
    pytest
else
    echo "Run production mode"
    alembic upgrade head
fi

