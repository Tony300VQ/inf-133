import requests

# Definir la consulta GraphQL
query1 = """
    {
        estudiante(id: 1, nombre: "Jose"){
            nombre
        }
    }
"""
query2="""
    {
        estudiantes
        {
            nombre   
        }
    }
"""
query3="""
    {
        estudiantes
        {
            nombre
            apellido   
        }
    }
"""
query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""
query6 = """
    {
        estudiantePorNombreYApellido(nombre: "Jose", apellido: "Lopez"){
            nombre
        }
    }
"""
query7 = """
    {
        estudiantePorCarrera(carrera: "Arquitectura"){
            nombre
        }
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
print("////////////")
response = requests.post(url, json={'query': query2})
print(response.text)
response = requests.post(url, json={'query': query6})
print(response.text)
print("////////////")
response = requests.post(url, json={'query': query7})
print(response.text)
query_crear1 = """
mutation {
        crearEstudiante(nombre: "Angelito", apellido: "Gonzales", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query_crear2 = """
mutation {
        crearEstudiante(nombre: "Angela", apellido: "Loza", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query_crear3 = """
mutation {
        crearEstudiante(nombre: "Andrea", apellido: "Alcon", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query8 = """
    {
        estudiantesPorCarrera(carrera: "Arquitectura"){
            nombre
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear1})
print(response_mutation.text)
response_mutation = requests.post(url, json={'query': query_crear2})
print(response_mutation.text)
response_mutation = requests.post(url, json={'query': query_crear3})
print(response_mutation.text)
response = requests.post(url, json={'query': query8})
print(response.text)
query9 = """
mutation{
        deleteEstudiantes(carrera: "Arquitectura"){
            estudiante{
                nombre
                carrera
            }
        }
    }
"""
response = requests.post(url, json={'query': query9})
print(response.text)