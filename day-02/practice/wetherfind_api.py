import requests

API_KEY = "5d677fb6eae5853671bfb7b1b0c7370d"

api_url = f"https://api.weatherstack.com/current?access_key={API_KEY}"

querysring = {"query":"New Delhi"}

response = requests.get(api_url, params=querysring)

print(response.json())
