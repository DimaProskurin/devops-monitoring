FROM python:3.6

RUN apt-get update && apt-get install -y vim curl jq
RUN pip3 install requests graphyte
RUN mkdir /code

COPY real_weather.py /code/real_weather.py
COPY forecast_weather.py /code/forecast_weather.py
COPY config.py /code/config.py
COPY runner.sh /code/runner.sh

WORKDIR /code
CMD ["./runner.sh"]