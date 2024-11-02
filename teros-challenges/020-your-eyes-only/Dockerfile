FROM python:bookworm

EXPOSE 8000

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python ./logtin/manage.py migrate

CMD ["python", "./logtin/manage.py", "runserver", "0.0.0.0:8000"]