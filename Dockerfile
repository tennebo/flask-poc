
FROM python:3.5

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy over all the Python code
COPY *.py ./

ENV \
    DEBUG=True \
    HOST=0.0.0.0 \
    PORT=8080

EXPOSE ${PORT}

ENTRYPOINT ["python", "service.py"]
