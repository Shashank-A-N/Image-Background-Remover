# 1. Use an official Python runtime as a parent image
FROM python:3.10-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the dependencies file and install them
# This is done in a separate step to leverage Docker's layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code into the container
COPY . .

# 5. Expose the port that Gunicorn will run on.
# Railway will automatically use the PORT environment variable.
EXPOSE 5001

# 6. Define the command to run the application using Gunicorn
# Railway provides the $PORT variable. Gunicorn will bind to all network interfaces.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--workers", "2", "--threads", "4", "--timeout", "120", "server:app"]
