def render_libro_list(libros):

    return [
        {
            "id": libro.id,
            "title": libro.title,
            "autor": libro.author,
            "edicion": libro.edition,
            "disponibilidad": libro.availability,
        }
        for libro in libros
    ]


def render_libro_detail(libro):

    return {
            "id": libro.id,
            "title": libro.title,
            "autor": libro.author,
            "edicion": libro.edition,
            "disponibilidad": libro.availability,
    }