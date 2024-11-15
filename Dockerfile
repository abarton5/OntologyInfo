FROM python:3.13-alpine

COPY GetOntologyInfo.py .

RUN pip install requests

CMD ["python", "GetOntologyInfo.py"]

