# Base image: Python 3.12 slim, as it is a lightweight application
FROM python:3.12-slim

# As we are using slim image, we have to install git using Debian package manager
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/mireiaacss/study_bingo.git .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Command to run the game
CMD ["python", "src/game.py"]
