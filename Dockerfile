FROM python:3.9-alpine

WORKDIR /app

ENV PBR_VERSION=1.0
COPY . . 
RUN pip install pyyaml==6.0.1 bandit==1.8.6 requests==2.25.1 .

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
