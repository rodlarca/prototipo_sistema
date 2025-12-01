FROM python:3.12-slim

# Evita archivos .pyc y mejora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# (Opcional) paquetes de sistema si alguna lib lo requiere
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Asegurar que exista la carpeta instance
RUN mkdir -p instance

# Variables de entorno para Flask
ENV FLASK_ENV=production

# Puerto interno de la app
EXPOSE 8080

# Comando de arranque
CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]
