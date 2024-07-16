# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./
COPY Errorcodes.properties ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src

# Make port 8080 available to the world outside this container
# EXPOSE 8080

# Run transform.py when the container launches
CMD ["python", "./src/ecsservice/app.py"]
