# Dockerfile

# Step 1: Use the official Docker image as a base.
# This provides the necessary Docker client tools for your CodeExecutorAgent.
FROM docker:latest

# Step 2: Install Python and pip.
# The 'docker:latest' image is based on Alpine Linux, so we use 'apk' for installation.
RUN apk add --no-cache python3 py3-pip

# Step 3: Set the working directory inside the container.
WORKDIR /app

# Step 4: Copy and install your Python dependencies first for better caching.
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code into the container.
COPY . .

# Step 6: Expose the port Streamlit runs on.
EXPOSE 8501

# Step 7: The command to start your Streamlit app when the container launches.
# --server.headless=true is crucial for running Streamlit in a cloud environment.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]