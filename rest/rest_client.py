import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)

# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "buscar_nombre"
get_response = requests.request(method="GETI", url=ruta_get)
print(get_response.text)
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "total_estudiantes"
get_response = requests.request(method="GETO", url=ruta_get)
print(get_response.text)
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "contar_carreras"
get_response = requests.request(method="GETU", url=ruta_get)
print(get_response.text)
#ruta_get= url+"buscar_nombre"
#get_response= requests.request(method="GET", url=ruta_get)
#print(get_response.text)