# Temperature Converter

Aplikasi sederhana untuk konversi suhu antara Celsius, Fahrenheit, dan Kelvin.

## Fitur

- Konversi Celsius ke Fahrenheit
- Konversi Fahrenheit ke Celsius  
- Konversi Celsius ke Kelvin
- Konversi Kelvin ke Celsius

## Cara Menjalankan

### Jalankan Secara Lokal

```bash
python app.py
```

### Jalankan dengan Docker

1. Build image Docker:
```bash
docker build -t app-exam/latest .
```

2. Jalankan container:
```bash
docker run -it app-exam:latest
```

## Penggunaan

Setelah menjalankan aplikasi, pilih jenis konversi (1-4) dan masukkan nilai suhu yang ingin dikonversi:

```
=== Temperature Converter ===
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
Choose conversion (1-4): 1
Enter temperature value: 25
Result: 77.00 °F
```

## Struktur File

- `app.py` - Aplikasi utama dengan fungsi konversi suhu
- `Dockerfile` - Konfigurasi untuk menjalankan aplikasi dalam container Docker
- `ci.yml` - Test stage: Syntax check pada app.py + menjalankan pytest (jika ada) dan Docker stage: Build image app-exam:latest + test container functionality
- `lint.yml` - Check code style, complexity, dan fatal errors

## CI/CD Pipeline

### Pipeline Stages

1. **Test Stage**: 
   - Syntax check dengan `py_compile`
   - Run unit tests (jika ada)
   - Validasi Python 3.10 compatibility

2. **Docker Stage**:
   - Build Docker image
   - Test basic functionality dalam container
   - Deploy ke registry (opsional)

### Local Pipeline Testing

Test pipeline secara lokal sebelum push:

```bash
# Test syntax
python -m py_compile app.py

# Test Docker build
docker build -t app-exam:test .
docker run --rm app-exam:test python -c "from app import celsius_to_fahrenheit; print(celsius_to_fahrenheit(100))"
```
