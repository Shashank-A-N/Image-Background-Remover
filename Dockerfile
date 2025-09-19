# 1. Use an official Python runtime as a parent image
FROM python:3.10-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code into the container
COPY . .

# 5. Expose the port that Gunicorn will run on.
EXPOSE 5001

# 6. Define the command to run the application (UPDATED LINE)
# This "shell form" correctly substitutes the $PORT environment variable.
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 server:app
