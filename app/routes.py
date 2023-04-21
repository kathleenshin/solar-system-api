from flask import Blueprint, jsonify, abort, make_response

class Planet():
    def __init__(self, id, name, description, x_parameter):
        self.id = id
        self.name = name
        self.description = description
        self.x_parameter = x_parameter

planets = [
    Planet(1, "Mars", "red", "something"),
    Planet(2, "Neptune", "blue", "something"),
    Planet(3, "Saturn", "dark blue", "something"),
    Planet(4, "Venus", "yellowish", "something"),
    Planet(5, "Earth", "blue/green", "something"),
    Planet(6, "Mercury", "red", "something"),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['GET'])
def handle_planets():
    planets_as_dict = [vars(planet) for planet in planets]
    return jsonify(planets_as_dict), 200

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
        "x_parameter": planet.x_parameter
    }