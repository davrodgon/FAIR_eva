import requests

url = "https://catalogue.eucaim.cancerimage.eu"
api_url = url + "/api/metadata"

response = requests.get(api_url)
print(response)
if response.status_code == 200:
    data = response.json()
print(data)

api_url = "https://catalogue.eucaim.cancerimage.eu/api/data/EUCAIM_biobanks"

response = requests.get(api_url)
print(response)
if response.status_code == 200:
    data = response.json()
print(data)


api_url = "https://catalogue.eucaim.cancerimage.eu/api/data/EUCAIM_biobanks/CHAI-1"

response = requests.get(api_url)
print(response)
if response.status_code == 200:
    data = response.json()
print(data)

