import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# === CONFIG ===
API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your OpenWeatherMap API key
CITY = 'London'
UNITS = 'metric'  # Use 'imperial' for Fahrenheit

# === Fetch weather data from API ===
def fetch_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units={UNITS}&appid={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# === Process data: extract timestamps and temperatures ===
def process_data(data):
    timestamps = []
    temperatures = []
    for entry in data['list']:
        timestamps.append(datetime.fromtimestamp(entry['dt']))
        temperatures.append(entry['main']['temp'])
    return timestamps, temperatures

# === Plot line chart of temperature trend ===
def plot_weather(timestamps, temperatures, city):
    sns.set(style='whitegrid')
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, temperatures, marker='o', color='blue', linewidth=2)
    plt.title(f'5-Day Temperature Forecast for {city}', fontsize=16)
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# === Main execution ===
if __name__ == "__main__":
    print(f"Fetching weather data for {CITY}...")
    weather_data = fetch_weather(CITY)
    timestamps, temperatures = process_data(weather_data)
    plot_weather(timestamps, temperatures, CITY)
