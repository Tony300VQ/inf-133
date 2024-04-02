import requests
url = 'http://localhost:8000/graphql'
# Definir la consulta GraphQL
query1 = """
    {
        plantas{
            id
            nombre_comun
            especie
            edad
            altura
            frutos
        }
    }
"""
response = requests.post(url, json={'query': query1})
print(response.text)
