FROM selenium/standalone-chrome:latest

USER root

# Instalar dependências
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    wget unzip curl ca-certificates gnupg \
    allure \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v", "--alluredir=allure-results"]
