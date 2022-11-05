FROM python:3.8.15-slim-bullseye
WORKDIR /FileManager/src
ADD /FileManager /FileManager
RUN apt-get update
RUN apt-get install -y awscli
RUN pip install -r requirements.txt
CMD ["python","main.py"]
