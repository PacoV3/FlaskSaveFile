FROM python:alpine3.7
WORKDIR /app

RUN pip install flask flask-restful werkzeug

EXPOSE 5001
CMD [ "python", "./app.py" ]
