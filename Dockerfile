FROM python:2.7

ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt

ENV PORT 5000
EXPOSE 5000

ENTRYPOINT ["python", "server.py"]