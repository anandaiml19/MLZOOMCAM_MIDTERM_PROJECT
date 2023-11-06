FROM python:3.10.12-buster


WORKDIR /app
COPY . /app

COPY requirementsy.txt .


RUN pip install -r requirementsy.txt

EXPOSE 9696

CMD ["gunicorn", "--bind","0.0.0.0:9696","deploy:app"]


