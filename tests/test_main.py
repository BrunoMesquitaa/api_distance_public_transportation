from api_distance_public_transportation.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_sucess():
    response = client.post(
        "/",
        json={
            "lat": -23.563949,
            "lon": -46.6568110
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "estacao_metro_km": 0.45,
        "estacao_trem_km": 3.31,
        "ponto_onibus_km": 0.26,
        "terminal_onibus_km": 2.35,
        "bicicletario_paraciclo_km": 2.25
    }


def test_lat_error_less():
    response = client.post(
        "/",
        json={
            "lat": -24.06424,
            "lon": -46.6568110
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "lat"
                ],
                "msg": "Error Latitude",
                "type": "value_error"
            }
        ]
    }


def test_lat_error_more():
    response = client.post(
        "/",
        json={
            "lat": -23.18339,
            "lon": -46.6568110
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "lat"
                ],
                "msg": "Error Latitude",
                "type": "value_error"
            }
        ]
    }


def test_lon_error_less():
    response = client.post(
        "/",
        json={
            "lat": -23.563949,
            "lon": -47.20854
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "lon"
                ],
                "msg": "Error Longitude",
                "type": "value_error"
            }
        ]
    }


def test_lon_error_more():
    response = client.post(
        "/",
        json={
            "lat": -23.563949,
            "lon": -45.69482
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "lon"
                ],
                "msg": "Error Longitude",
                "type": "value_error"
            }
        ]
    }
