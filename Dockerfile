FROM python:3.8.15-slim-bullseye
WORKDIR /FileManager/src
ADD /FileManager /FileManager
RUN pip install -r requirements.txt
CMD ["python","main.py"]