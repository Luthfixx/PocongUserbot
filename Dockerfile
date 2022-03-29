FROM luthfixx/poconguserbot:buster

RUN git clone -b main https://github.com/Luthfixx/PocongUserbot /home/PocongUserbot/ \
    && chmod 777 /home/PocongUserbot \
    && mkdir /home/PocongUserbot/bin/

WORKDIR /home/PocongUserbot/

CMD [ "bash", "start" ]
