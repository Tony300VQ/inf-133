import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
ruta_get = url + "estudiantes/carreras"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
ruta_get = url + "estudiantes/economistas"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
nuevo_estudiante1 = {
    "nombre": "Luis",
    "apellido": "Coca",
    "carrera": "Economía",
}
nuevo_estudiante2 = {
    "nombre": "Evo",
    "apellido": "Ayma",
    "carrera": "Economía",
}
post_response = requests.request(method="POST",url=ruta_post,json=nuevo_estudiante1)
print(post_response)
post_response = requests.request(method="POST",url=ruta_post,json=nuevo_estudiante2)
print(post_response)






# DELETE elimina todos los estudiantes por la ruta /estudiantes
#ruta_eliminar = url + "estudiantes"
#eliminar_response = requests.request(method="DELETE", 
 #                                   url=ruta_eliminar)
#print(eliminar_response.text)

#post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
#print(post_response.text)

# GET busca a un estudiante por id /estudiantes/{id}
#ruta_filtrar_nombre = url + "estudiantes/1"
#filtrar_nombre_response = requests.request(method="GET", 
 #                               url=ruta_filtrar_nombre)
#print(filtrar_nombre_response.text)

# PUT actualiza un estudiante por la ruta /estudiantes
#ruta_actualizar = url + "estudiantes"
#estudiante_actualizado = {
#    "id": 1,
#    "nombre": "Juan",
#    "apellido": "Pérez",
#    "carrera": "Ingeniería Agronomica",
#}
#put_response = requests.request(
 #   method="PUT", url=ruta_actualizar, 
  #  json=estudiante_actualizado
#)
#print(put_response.text)
