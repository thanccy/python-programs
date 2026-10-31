
import json
import pandas as pd

# Sample JSON weather dataset
weather_data = """
{
    "weather": [
        {
            "location": {
                "city": "Kochi",
                "country": "India"
            },
            "temperature": {
                "value": 30,
                "unit": "Celsius"
            },
            "humidity": 75
        },
        {
            "location": {
                "city": "Delhi",
                "country": "India"
            },
            "temperature": {
                "value": 35,
                "unit": "Celsius"
            },
            "humidity": 60
        },
        {
            "location": {
                "city": "Mumbai",
                "country": "India"
            },
            "temperature": {
                "value": 32,
                "unit": "Celsius"
            },
            "humidity": 80
        }
    ]
}
"""

# Parse JSON data
data = json.loads(weather_data)

# Extract weather information
weather_list = []

for item in data["weather"]:
    city = item["location"]["city"]
    country = item["location"]["country"]
    temperature = item["temperature"]["value"]
    humidity = item["humidity"]

    weather_list.append({
        "City": city,
        "Country": country,
        "Temperature (C)": temperature,
        "Humidity (%)": humidity
    })

# Convert data into a table
df = pd.DataFrame(weather_list)

# Display weather information
print("Weather Information:")
print(df)

# Generate summarized weather report
print("\nWeather Summary Report")

print("Average Temperature:",
      df["Temperature (C)"].mean(), "°C")

print("Average Humidity:",
      df["Humidity (%)"].mean(), "%")

# Display weather details for each city
for index, row in df.iterrows():
    print("\nCity:", row["City"])
    print("Temperature:", row["Temperature (C)"], "°C")
    print("Humidity:", row["Humidity (%)"], "%")

# Find the hottest city
hottest_city = df.loc[df["Temperature (C)"].idxmax()]

print("\nHottest City:", hottest_city["City"])
print("Temperature:", hottest_city["Temperature (C)"], "°C")
