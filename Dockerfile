
FROM python:3.9-slim

WORKDIR /APP

COPY app.py .

CMD ["python", "app.py"]
