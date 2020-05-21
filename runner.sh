#!/bin/bash
echo "Starting script"
while true
do
	python3 forecast_weather.py
    python3 real_weather.py
    sleep 15
done
