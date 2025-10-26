import requests

url = "http://localhost:9696/predict"
# url = 'https://mlzoomcamp-flask-uv.fly.dev/predict'

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
}

response = requests.post(url, json=client)
predictions = response.json()

print(predictions)
