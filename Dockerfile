FROM python:3.10

RUN apt-get update && apt-get install -y git

RUN mkdir -p /project/src
WORKDIR /project/src

COPY . ./

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

CMD ["bash"]

