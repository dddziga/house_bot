FROM python:3

WORKDIR /usr/src/app

RUN pip install pyTelegramBotAPI

COPY . .

CMD [ "python3", "./titova_bot.py" ]