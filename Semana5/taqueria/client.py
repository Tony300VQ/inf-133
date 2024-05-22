import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas 
mi_taco = {
    "base": "Tortilla",
    "guiso": "Carne",
    "toppings": ["Cebolla", "Queso"],
    "salsa":"Verde"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# PUT /pizzas/1
edit_taco = {
    "base": "Tortilla",
    "guiso": "Pollo",
    "toppings": ["Cebolla", "Queso"],
    "salsa":"Roja"
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# DELETE /pizzas/1

response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())