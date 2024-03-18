import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "tamaño": "Mediana",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso","Peperoni"]
}
response = requests.post(url, json=mi_pizza, headers=headers)
print(response.json())
