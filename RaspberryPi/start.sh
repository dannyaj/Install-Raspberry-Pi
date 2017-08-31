#!/bin/bash

docker run -d \
--name iot \
--restart=unless-stopped \
-v /home/pi/RaspberryPi/iot-device:/iot-device \
--net host \
--device /dev/mem \
--cap-add SYS_RAWIO \
iot