import requests

r = requests.get("https://naas.isalman.dev/no")
r.raise_for_status()  # optional but recommended

response = r.json()

print(response)

