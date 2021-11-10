FROM python:3.7
WORKDIR /Jarvis_python
COPY . .
RUN apt-get -y update
RUN pip install -r requirements.txt
CMD [ "python","./main.py"]

