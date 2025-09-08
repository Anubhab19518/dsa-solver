# Dockerfile

# Step 1: Use the official Docker image as a base.
FROM docker:latest

# Step 2: Install system-level build tools using the apk package manager.
# This is the new line that fixes the installation error.
RUN apk add --no-cache build-base python3-dev

# Step 3: Set the working directory inside the container.
WORKDIR /app

# Step 4: Copy and install your Python dependencies.
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code into the container.
COPY . .

# Step 6: Expose the port Streamlit runs on.
EXPOSE 8501

# Step 7: The command to start your Streamlit app.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]