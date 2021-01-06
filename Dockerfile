FROM python:3.9

WORKDIR /lab1/code

COPY lab1.py .

CMD [ "python", "./lab1.py" ]