# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Install required packages
RUN apt-get update \
    && apt-get install -y wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for ChromeDriver and Chrome
ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver
ENV CHROME_BIN=/usr/bin/google-chrome

# Copy the custom ChromeDriver binary to the container
COPY chromedriver /usr/local/bin/chromedriver
# chromedriver issue is not resolved only use 

# Mount the local test and results directories to the container
VOLUME ["/app/Tests", "/app/Results", "/app/Resources"]

# Set the entry point command to run Robot Framework Parallel
CMD ["pabot", "--processes", "3", "--verbose", "/app/Tests"]
# Without pabot
#CMD ["robot", "--outputdir", "/app/Results", "/app/Test"]
