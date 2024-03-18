import requests

# Definir la consulta GraphQL
query1 = """
    {
        hello
    }
"""
query2 = """
    {
        goodbye
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query1})
print(response.text)
response = requests.post(url, json={'query': query2})
print(response.text)
