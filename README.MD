docker build -t justinas/skelbiu.lt:latest .  
docker run --rm -it  justinas/skelbiu.lt:latest
docker run justinas/skelbiu.lt:latest python ./script.py $USERNAME $PASSWORD