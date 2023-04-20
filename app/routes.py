from flask import Blueprint

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

        

