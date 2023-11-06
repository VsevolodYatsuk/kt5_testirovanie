# test_petstore.py
import allure
import pytest
import requests
from models import Pet

petstore_api_url = "https://petstore.swagger.io/v2/pet"

@allure.title("Создание питомца")
def test_create_pet():
    with allure.step("Шаг 1: Создание питомца"):
        pet_data = {
            "id": 1,
            "category": {"id": 1, "name": "dogs"},
            "name": "Buddy",
            "photoUrls": ["https://example.com/buddy.jpg"],
            "tags": [{"id": 1, "name": "friendly"}],
            "status": "available"
        }

        response = requests.post(petstore_api_url, json=pet_data)

    with allure.step("Шаг 2: Проверка статуса ответа"):
        assert response.status_code == 200

@allure.title("Получение питомца по ID")
def test_get_pet_by_id():
    pet_id = 1

    with allure.step(f"Шаг 1: Получение питомца с ID {pet_id}"):
        response = requests.get(f"{petstore_api_url}/{pet_id}")

    with allure.step("Шаг 2: Проверка статуса ответа"):
        assert response.status_code == 200
        pet = Pet(**response.json())
        assert pet.id == pet_id

@allure.title("Удаление питомца")
def test_delete_pet():
    pet_id = 1

    with allure.step(f"Шаг 1: Удаление питомца с ID {pet_id}"):
        response = requests.delete(f"{petstore_api_url}/{pet_id}")

    with allure.step("Шаг 2: Проверка статуса ответа"):
        assert response.status_code == 200
