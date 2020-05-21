from config import API, API_KEY, CITY
import requests
import graphyte


def get_real_weather():
    request = "{}/{}".format(API, "weather")
    response = requests.get(
        request,
        {"q": CITY, "appid": API_KEY, "units": "metric"}
    ).json()
    return response


def get_wind_speed(weather):
    return weather["wind"]["speed"]


def get_temperature(weather):
    return weather["main"]["temp"]


def get_humidity(weather):
    return weather["main"]["humidity"]


def send_real_weather(weather):
    sender = graphyte.Sender("graphite", prefix="weather")
    sender.send("real.temperature", get_temperature(weather))
    sender.send("real.wind_speed", get_wind_speed(weather))
    sender.send("real.humidity", get_humidity(weather))


if __name__ == "__main__":
    send_real_weather(get_real_weather())
