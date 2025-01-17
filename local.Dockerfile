FROM python:3.12-slim-bookworm

# OS Dependencies
RUN apt-get update \
    && apt-get install -y libmariadb-dev-compat libmariadb-dev gcc locales \
    default-libmysqlclient-dev build-essential pkg-config libssl-dev libffi-dev \
    python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 wkhtmltopdf \
    && apt-get clean

# Setup python locales
RUN echo "es_CL.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen es_CL.UTF-8 && \
    update-locale LANG=es_CL.UTF-8
ENV LANG es_CL.UTF-8
ENV PYTHONUNBUFFERED 1
RUN locale -a

# Setup project
RUN mkdir /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Setup entrypoint
COPY ./entrypoint-dev.sh /app/entrypoint-dev.sh
RUN chmod +x /app/entrypoint-dev.sh

# To the moon
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint-dev.sh"]
