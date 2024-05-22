import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "chocolate_type":"tablet",
    "weight":"2gr",
    "flavor":"durazno",
    "stuffed":None
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type":"truffle",
    "weight":"2gr",
    "flavor":"frutilla",
    "stuffed":"chocolate"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{vehicle_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "flavor": "apple"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{vehicle_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())