FROM python:3.9-slim-buster

WORKDIR /app

# Install Robot Framework and required libraries
RUN pip install -r requirements.txt

# Copy the entrypoint script and keyword files to the container
COPY entrypoint.sh /app/
COPY keywords/ /app/keywords/

# Set the entrypoint script as executable
RUN chmod +x entrypoint.sh

# Set up a volume for the test cases
VOLUME /app/tests

# Set the entrypoint for the container
ENTRYPOINT ["/app/entrypoint.sh"]
