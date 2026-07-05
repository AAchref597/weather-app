import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("City not found.")
        return

    data = response.json()

    print("\n====== Weather Report ======")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Condition: {data['weather'][0]['description']}")
    print("============================")

while True:
    city = input("\nEnter city name (or type 'exit'): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break

    get_weather(city)
