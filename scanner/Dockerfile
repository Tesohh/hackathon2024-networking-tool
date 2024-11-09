
FROM alpine:3.18 AS scanner

RUN apk update && apk add \
    python3 \
    nmap \
    py3-requests

WORKDIR /app

COPY main.py .
COPY os_detector.py .
COPY scan.py .
COPY cve/ ./cve

ENTRYPOINT [ "python3", "main.py" ]
