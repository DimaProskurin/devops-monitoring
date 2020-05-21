from config import API, API_KEY, CITY
from real_weather import get_temperature, get_humidity, get_wind_speed
import requests
import graphyte


def get_forecast_weather():
    request = "{}/{}".format(API, "forecast")
    response = requests.get(
        request,
        {"q": CITY, "appid": API_KEY, "units": "metric"}
    ).json()
    return response['list'][0]


def send_forecast_weather(weather):
    sender = graphyte.Sender("graphite", prefix="weather")
    sender.send("forecast.temperature", get_temperature(weather))
    sender.send("forecast.wind_speed", get_wind_speed(weather))
    sender.send("forecast.humidity", get_humidity(weather))


if __name__ == "__main__":
    send_forecast_weather(get_forecast_weather())
