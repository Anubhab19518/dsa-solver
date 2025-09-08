# Dockerfile

# Step 1: Use the official Docker image as a base.
FROM docker:latest

# Step 2: Install system-level build tools, including C and Rust compilers.
RUN apk add --no-cache build-base python3-dev py3-pip rust cargo

# Step 3: Set the working directory inside the container.
WORKDIR /app

# Step 4: Copy and install your Python dependencies.
COPY requirements.txt .
# Add the --break-system-packages flag to bypass the new safety check.
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Step 5: Copy the rest of your application code into the container.
COPY . .

# Step 6: Expose the port Streamlit runs on.
EXPOSE 8501

# Step 7: The command to start your Streamlit app.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]