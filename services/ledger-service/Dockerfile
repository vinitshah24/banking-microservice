FROM python:3.12-slim
WORKDIR /app
COPY requirements/base.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY shared/python /shared/python
RUN pip install -e /shared/python
COPY services/ledger-service /app
CMD ["sh","/app/entrypoint.sh"]
