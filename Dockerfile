FROM python:3.8-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .
COPY .env .

# Expose the port the app runs on
EXPOSE 8010

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
