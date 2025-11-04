# Menggunakan base image Python yang ringan (Alpine Linux)
FROM python:3.10-alpine

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file aplikasi kita ke dalam direktori kerja
COPY app.py .

# Menetapkan environment variable default
ENV GREET_NAME="Docker"

# Perintah yang akan dijalankan saat container dimulai
CMD ["python", "app.py"]
