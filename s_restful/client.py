import requests
url = "http://localhost:8000/"
# GET
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST 
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET with Query pharams
ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# DELETE
ruta_get = url + "estudiantes"
delete_response = requests.request(method="DELETE", url=ruta_get)
print(delete_response.text)