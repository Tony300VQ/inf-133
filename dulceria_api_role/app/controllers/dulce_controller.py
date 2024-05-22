from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_list, render_dulce_detail
from utils.decorators import jwt_required, roles_required
dulce_bp = Blueprint("dulce", __name__)


@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulces():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces))


@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "Dulce no encontrado"}), 404



@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_dulce():
    data = request.json
    brand = data.get("brand")
    weight=data.get("weight")
    flavor=data.get("flavor")
    origin=data.get("origin")

    # Validación simple de datos de entrada
    if not brand or not weight or not flavor or origin is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    dulce=Dulce(brand=brand,weight=weight,flavor=flavor,origin=origin)
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201


@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_dulce(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "Dulce no encontrado"}), 404

    data = request.json
    brand = data.get("brand")
    weight=data.get("weight")
    flavor=data.get("flavor")
    origin=data.get("origin")
    dulce.update(brand=brand,weight=weight,flavor=flavor,origin=origin)

    return jsonify(render_dulce_detail(dulce))


@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_dulce(id):
    dulce =Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "Dulce no encontrado"}), 404
    dulce.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204