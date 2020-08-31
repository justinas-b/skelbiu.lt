# To run on Synology NAS on schedule

![a](./resources/1. Control Panel.png)


# To run this on demoand

docker build -t justinasb/skelbiu.lt:latest .
docker run --rm -it justinas/skelbiu.lt:latest
docker run justinasb/skelbiu.lt:latest python ./script.py $USERNAME $PASSWORD