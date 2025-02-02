import requests

# Define the test URL
url = "https://httpbin.org/get"  # You can replace this with any test URL

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful!")
    print("Response JSON:", response.json())  # Prints the response in JSON format
else:
    print("Request failed with status code:", response.status_code)
