from .conftest import client


def test_create_feedback():
    """Тест для создания Feedback."""

    response = client.post(
        "/feedback/create/",
        json={
            "fio": "string",
            "message": "string",
            "contact_data": "string"
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "fio": "string",
        "message": "string",
        "contact_data": "string"
    }


def test_get_feedback():
    """Тест для получения Feedback."""

    response = client.get(
        "/feedback/1/",
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "fio": "string",
        "message": "string",
        "contact_data": "string"
    }


def test_update_feedback():
    """Тест для обновления Feedback."""

    response = client.put(
        "/feedback/1/update/",
        json={
            "id": 1,
            "fio": "string",
            "message": "string",
            "contact_data": "string"
        }
    )

    assert response.status_code == 204


def test_delete_feedback():
    """Тест для удаления Feedback."""

    response = client.delete(
        "/feedback/1/delete/",
    )

    assert response.status_code == 204
