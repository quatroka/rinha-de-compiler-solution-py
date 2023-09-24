FROM python:3.12-rc-slim

WORKDIR /usr/src/app

COPY /src /usr/src/app/src
COPY main.py /usr/src/app

ENTRYPOINT [ "python", "-m", "main" ]
CMD [ "python", "-m", "main" ]
