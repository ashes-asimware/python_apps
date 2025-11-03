import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

latitude = 40.7128
longitude = -74.0060

weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto&start_date={start_date}&end_date={end_date}"

response = requests.get(weather_api_url)
data = response.json()

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

daily_data = data['daily']

df = pd.DataFrame(daily_data)
print(df)

df['date'] = pd.to_datetime(df['time'])
print(df)

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temperature_2m_max'], marker="o", label='Max Temperature (°C)')
plt.plot(df['date'], df['temperature_2m_min'], marker="o", label='Min Temperature (°C)')

plt.title('Daily Max and Min Temperatures Over the Past Week')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('temperature_plot.png')
plt.show()

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/weather_data.csv', index=False)







