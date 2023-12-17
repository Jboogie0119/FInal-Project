###The purpose of this program is a to create a weather simulation to show temperatures and average precipitation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This is weather data from different cities
weather_data = {
    "city": ["CityAA", "CityBB", "CityCC", "CityDD", "CityEE"],
    "temperature": [22, 30, 28, 18, 25],
    "humidity": [80, 65, 70, 90, 75],
    "precipitation": [5, 12, 8, 20, 7]
}

# This converts the data 
weather_df = pd.DataFrame(weather_data)

# This is statistical analysis using numpy
temperatures = np.array(weather_df["temperature"])
humidity = np.array(weather_df["humidity"])
precipitation = np.array(weather_df["precipitation"])

print("Average Temperature:", np.mean(temperatures))
print("Maximum Humidity:", np.max(humidity))
print("Total Precipitation:", np.sum(precipitation))

#This columns states what the water feels like eventhough it might not be the exact temperature
weather_df["feels_like"] = weather_df["temperature"] - 0.7 * (100 - weather_df["humidity"]) / 100
#this filters the cities with high precipitation
high_precipitation_df = weather_df[weather_df["precipitation"] > 10]
# Writes the data to a CSV file
high_precipitation_df.to_csv("high_precipitation_cities.csv", index=False)

# This creates a visulization using matplotlib
# Bar graph
plt.bar(weather_df["city"], weather_df["temperature"])
plt.title("City Temperatures")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.show()

# A scatter plot showing humidity
plt.scatter(weather_df["city"], weather_df["humidity"])
plt.title("City Humidity")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.show()

# A line plot showing what it feels like
plt.plot(weather_df["city"], weather_df["feels_like"], marker='o')
plt.title("Feels Like Temperature in Cities")
plt.xlabel("City")
plt.ylabel("Feels Like Temperature (°C)")
plt.show()
