# Base image belirleme
FROM python:3.8

# Uygulama kodunu çalıştıracağımız dizini belirleme
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu ekleme
COPY  . .

# Uygulamayı başlatma
CMD ["python", "app.py"]
