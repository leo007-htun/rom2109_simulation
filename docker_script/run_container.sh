#!/usr/bin/bash 
if [ $# -ne 2 ]
then
	echo "Usage: run_container [image] [name]"
	exit
fi
echo "$1"
xhost +local:root 
docker run -it --network='host' \
--env='DISPLAY' \
--env='QT_X11_NO_MITSHM=1' \
--volume='/tmp/.X11-unix:/tmp/.X11-unix:rw' \
--name $2 $1 bash

xhost -local:root
docker rm $2
