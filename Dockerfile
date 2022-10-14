FROM python:3.8-slim-buster
EXPOSE 8000
ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ]