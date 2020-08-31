FROM python:alpine

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver
# set display port to avoid crash
ENV DISPLAY=:99

WORKDIR /usr/src/skelbiu.lt
COPY . .
RUN pip install selenium

CMD [ "python", "./script.py" ]
