from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# # class Planet():
# #     def __init__(self, id, name, description, has_rings):
# #         self.id = id
# #         self.name = name
# #         self.description = description
# #         self.has_rings = has_rings

# # planets = [
# #     Planet(1, "Mars", "red", True),
# #     Planet(2, "Neptune", "blue", True),
# #     Planet(3, "Saturn", "dark blue", True),
# #     Planet(4, "Venus", "yellowish", True),
# #     Planet(5, "Earth", "blue/green", True),
# #     Planet(6, "Mercury", "red", True),
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        has_rings=request_body["has_rings"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created"), 201

@planets_bp.route("", methods=['GET'])
def handle_planets():

    planets = Planet.query.all()
    planets_response = [vars(planet) for planet in planets]
    return jsonify(planets_response), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "has_rings": planet.has_rings
    }