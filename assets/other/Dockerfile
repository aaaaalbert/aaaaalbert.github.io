# Define a Python2 container with the EdgeNet echo web server inside.
#
# Dockerfile based on the "Get started with Docker" tutorials at
# https://docs.docker.com/get-started/part2/#define-a-container-with-dockerfile

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Include the echo server code
ADD ./echo_server.py .

# Make port 8000 available to the outside world. (We will remap the port
# later using Kubernetes.)
EXPOSE 8000

# Run the server when the container launches
CMD ["python", "echo_server.py"]
