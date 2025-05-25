#!/bin/bash

# Start JupyterLab in background
jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --NotebookApp.token='' \
    --NotebookApp.allow_origin='*' \
    --NotebookApp.allow_remote_access=True \
    --allow-root &

# Start Dash app and log output
echo "Starting Dash app on port 8050..."
python dashboard/dash_app.py

# Keep container alive if Dash crashes
tail -f /dev/null
