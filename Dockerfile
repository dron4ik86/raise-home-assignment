# Use Python 3.13 as the base image
FROM python:3.13-slim

# Set the working directory inside the container to /opt/api-automation
WORKDIR /opt/raise-home-assignment

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy the requirements.txt file from your local host to the present location
COPY requirements.txt .

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application's source code from your local host to the filesystem of the container at the working directory
COPY . /opt/raise-home-assignment
