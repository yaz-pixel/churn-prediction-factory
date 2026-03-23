# 1. Start with a tiny, clean computer that already has Python 3.11 installed
FROM python:3.11-slim

# 2. Set the working directory inside the magic box
WORKDIR /app

# 3. Copy your requirements file into the box
COPY requirements.txt .

# 4. Install all the necessary libraries inside the box
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project (src and models) into the box
COPY ./src ./src
COPY ./models ./models

# 6. Walk into the src folder (This is exactly like typing 'cd src' locally!)
WORKDIR /app/src

# 7. Turn on the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]