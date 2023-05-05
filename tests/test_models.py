from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mars",
                    description="red",
                    has_rings = True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "red"
    assert result["has_rings"] == True

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mars",
                    description="red",
                    has_rings=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mars"
    assert result["description"] == "red"
    assert result["has_rings"] == True

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="red",
                    has_rings=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "red"
    assert result["has_rings"] == True

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mars",
                    has_rings=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["has_rings"] == True

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Mars",
        "description": "red",
        "has_rings": True
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mars"
    assert new_planet.description == "red"
    assert new_planet.has_rings == True

def test_from_dict_with_no_name():
    # Arrange
    test_data = {
        "description": "red",
        "has_rings": True
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(test_data)

def test_from_dict_with_no_description():
    # Arrange
    test_data = {
        "name": "Mars",
        "has_rings": True
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(test_data)

def test_from_dict_with_extra_keys():
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "Mars",
        "description": "red",
        "has_rings": True
    }
    
    # Act
    new_planet = Planet.from_dict(test_data)

    # Assert
    assert new_planet.name == "Mars"
    assert new_planet.description == "red"