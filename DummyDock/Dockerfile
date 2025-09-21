# Use the Anaconda base image
FROM continuumio/anaconda3 

# Copy the application files into the container
COPY . /usr/app/

# Set the working directory inside the container
WORKDIR /usr/app/

# Expose port 5000 for the application
EXPOSE 5000

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]