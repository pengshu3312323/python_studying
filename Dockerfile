# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r req.txt

# Make port 80 available to the meetpencil outside this container
EXPOSE 8000

# Define environment variable
ENV NAME meetpencil
# ENV http_proxy 0.0.0.0:80
# ENV https_proxy 0.0.0.0:443


# Run app.py when the container launches
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--workers=4", "--env", "DJANGO_SETTINGS_MODULE=meetpencil.settings", "meetpencil.wsgi"]
