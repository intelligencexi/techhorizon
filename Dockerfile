FROM python:3.13-slim

LABEL MAINTAINER="Intelligence Ezemonye"

WORKDIR /app

COPY requirements.txt .


RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*


COPY . .

EXPOSE 2806

# Run database migrations and start the server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:2806"]
