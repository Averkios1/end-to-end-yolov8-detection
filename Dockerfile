FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

#RUN apt update -y && apt install azure-cli -y

EXPOSE 8080

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py", "--host=0.0.0.0", "--port=8080"]
#