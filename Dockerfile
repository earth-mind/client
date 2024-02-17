# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
# We're combining the Poetry installation commands to reduce the image layers
RUN pip install --no-cache-dir poetry

# Copy the Poetry configuration files into the container
COPY pyproject.toml poetry.lock* /app/

# Disable virtualenv creation by Poetry
# This is recommended when using Poetry inside Docker
# to ensure the packages are installed globally in the container
RUN poetry config virtualenvs.create false

# Install project dependencies using Poetry
# The --no-root option tells Poetry to not install the project package itself
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the code into the container
COPY . /app

# Command to run the application
CMD ["python", "app.py"]
