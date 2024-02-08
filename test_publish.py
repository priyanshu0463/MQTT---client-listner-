import requests

# Replace 'http://localhost:8000/mqtt-view/' with your actual URL
url = 'http://localhost:8000/mqtt_view/'

# Specify the client ID in the headers
headers = {'HTTP_CLIENT_ID': 'client-01'}

# Define the message payload
data = {'message': 'Hello from client-01'}

# Send a POST request to the Django server
response = requests.post(url, data=data, headers=headers)

print(response.json())