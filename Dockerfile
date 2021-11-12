FROM python:3.9

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1001 ubuntu
WORKDIR /home/ubuntu
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN jt -t monokai -m 200
USER ubuntu

CMD ["jupyter",  "lab", "--ip=0.0.0.0", "--port=8888"]






