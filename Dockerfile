FROM python:3.13.0

LABEL MAINTAINER="Intelligence Ezemonye"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 2806

CMD ["python", "manage.py", "runserver", "0.0.0.0:2806"]
