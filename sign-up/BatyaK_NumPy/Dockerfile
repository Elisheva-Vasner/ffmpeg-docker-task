FROM python:3.12
RUN apt-get update && apt-get install -y \
    ca-certificates \
    libgl1 \
    && update-ca-certificates
ADD main.py flower.jpg requirements.txt ./data/
RUN pip install -r data/requirements.txt
VOLUME /data/save 
CMD ["python", "data/main.py"]
