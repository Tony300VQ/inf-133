import requests
url = 'http://localhost:8000/graphql'
# Definir la consulta GraphQL
query4 = """
mutation {
        createPlanta(nombre: "especie5",especie: "especie5", edad: 3, altura: 3, frutos: True) {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""
response = requests.post(url, json={'query': query4})
print(response.text)
print("//////////")
query5 = """
mutation {
        upDatePlanta(id:1, nombre: "Angel", especie: "Gomez", edad: 6, altura: 10, frutos: False) {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""
response = requests.post(url, json={'query': query5})
print(response.text)
print("//////")
query1="""
    {
        plantas
        {
            id
            nombre
        }
    }
"""
query2="""
{
    plantasPorEspecie(especie:"especie1")
    {
        id
        nombre
    }
}
"""
query3="""
{
    plantasQuePoseenFrutos
    {
        nombre
    }
}
"""
response = requests.post(url, json={'query': query1})
print(response.text)
response = requests.post(url, json={'query': query2})
print(response.text)
response = requests.post(url, json={'query': query3})
print(response.text)
query_cre = """
mutation {
        deletePlanta(id:1) {
            planta {
                nombre
            }
        }
    }
"""
response = requests.post(url, json={'query': query_cre})
print(response.text)
response = requests.post(url, json={'query': query1})
print(response.text)