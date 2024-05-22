from flask import Blueprint, request, jsonify
from models.libro_model import Libro
from views.libro_view import render_libro_list, render_libro_detail

libro_bp = Blueprint("libro", __name__)


@libro_bp.route("/libros", methods=["GET"])
def get_libros():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))


@libro_bp.route("/libros/<int:id>", methods=["GET"])
def get_libro(id):
    libro = Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "Libro no encontrado"}), 404



@libro_bp.route("/libros", methods=["POST"])
def create_libro():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")

    # Validación simple de datos de entrada
    if not title or not edition or not availability or author is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    libro = Libro(title=title,author=author,edition=edition,availability=availability)
    libro.save()

    return jsonify(render_libro_detail(libro)), 201


@libro_bp.route("/libros/<int:id>", methods=["PUT"])
def update_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.json
    title = data.get("title")
    author = data.get("author")
    edition = data.get("edition")
    availability = data.get("availability")
    libro.update(title=title,author=author,edition=edition ,availability=availability)

    return jsonify(render_libro_detail(libro))


@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204