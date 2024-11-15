FROM python:3.13-alpine

RUN pip install requests

COPY GetOntologyInfo.py .

CMD ["python", "GetOntologyInfo.py"]

