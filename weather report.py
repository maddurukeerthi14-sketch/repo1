import requests

APIKEY = "36ecc1d33e87e773c326832f6019a67d"
City = input("Enter a city to get its weather report..")

data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={APIKEY}")

responseData = data.json()

print(responseData)
print()
print(f"{City} has temperature of => ",responseData["main"]["temp"],"k")
print(f"{City} has humidity of => ",responseData["main"]["humidity"],"%")

