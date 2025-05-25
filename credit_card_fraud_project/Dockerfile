# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install notebook jupyterlab

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose ports
EXPOSE 8888
EXPOSE 8050

# Run the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
