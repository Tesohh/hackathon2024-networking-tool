
FROM alpine:3.18 AS scanner

RUN apk update && apk add \
    python3 \
    nmap

WORKDIR /app

COPY main.py .
COPY os_detector.py .

ENTRYPOINT [ "python3", "main.py" ]
