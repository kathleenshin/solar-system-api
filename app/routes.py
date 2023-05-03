from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        has_rings=request_body["has_rings"])
    db.session.add(new_planet)
    db.session.commit()

    # return make_response(f"Planet {new_planet.name} successfully created"), 201
    return {
        "id": new_planet.id,
        "name": new_planet.name,
        "msg": "Successfully created"
    }, 201

@planets_bp.route("", methods=['GET'])
def handle_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query).all()
    else:
        planets = Planet.query.all()
    
    planets_response = [Planet.to_dict(planet) for planet in planets]
    return jsonify(planets_response), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    
    if planet is None:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
    return planet

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "has_rings": planet.has_rings
    }


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.has_rings = request_body["has_rings"]

    db.session.commit()

    # return make_response(f"Planet #{planet_id} successfully updated")
    return jsonify(planet.to_dict()), 200

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet_id} successfully deleted")