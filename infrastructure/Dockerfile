FROM python:3.12-slim

WORKDIR /fop

RUN apt-get update && apt-get dist-upgrade -y && apt-get clean && \
    /usr/local/bin/pip install --no-cache-dir --upgrade pip && /usr/local/bin/pip install --no-cache-dir pipenv

COPY ./application/Pipfile /fop/Pipfile
COPY ./application /fop/application
COPY ./tests /fop/tests
COPY ./infrastructure/docker/application/entrypoint.sh /fop/infrastructure/entrypoint.sh

RUN /usr/local/bin/pipenv install --skip-lock --system

ENTRYPOINT ["/fop/infrastructure/entrypoint.sh"]
