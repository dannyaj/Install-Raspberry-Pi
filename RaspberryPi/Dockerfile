FROM resin/rpi-raspbian:jessie-20170426

RUN apt-get update
RUN apt-get -y install build-essential python-dev python-pip
RUN pip install psutil
RUN pip install flask
RUN pip install requests
RUN pip install RPi.GPIO

ADD iot-device /iot-device/
WORKDIR /iot-device

CMD ["/usr/bin/python", "up.py"]