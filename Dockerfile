FROM python:3.9

# Set up the secure, non-root user HF requires
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Copy requirements and install them securely
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all your physics models, images, and code
COPY --chown=user . /app

# Flask typically runs on port 5000, but HF expects 7860
# This environment variable tells Flask to use the right port
ENV FLASK_RUN_PORT=7860
ENV FLASK_RUN_HOST=0.0.0.0

# Start the application
# If you use 'python app.py', ensure your app.py ends with: 
# app.run(host='0.0.0.0', port=7860)
CMD ["python", "app.py"]
