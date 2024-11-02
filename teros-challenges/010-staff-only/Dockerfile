FROM python:bookworm

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./staff-only.py"]