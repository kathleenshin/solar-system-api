def test_get_all_planets_with_empty_db_returns_empty_list(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_all_planets_with_populated_db(client, two_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Mars",
            "description": "red",
            "has_rings": False
        },
        {
            "id": 2,
            "name": "Venus",
            "description": "orange",
            "has_rings": False
        },
    ]

def test_get_one_planet_empty_db_returns_404(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_returns_400_with_invalid_planet_id(client):
    response = client.get("/planets/Mars")
    assert response.status_code == 400

def test_post_one_planet_creates_planet_in_db(client):
    response = client.post("/planets", json= {
        "name": "Saturn",
        "description": "blue",
        "has_rings": True
        }
    )

    response_body = response.get_json()

    assert response.status_code == 201
    assert "msg" in response_body      
    assert response_body["id"] == 1
    assert response_body["name"] == "Saturn"

def test_update_one_planet_updates_planet_in_db(client, two_planets):
    response = client.put("/planets/1", json={
        "name": "updated_name",
        "description": "updated_description",
        "has_rings": True
        }
    )

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "updated_name"
    assert response_body["description"] == "updated_description"

