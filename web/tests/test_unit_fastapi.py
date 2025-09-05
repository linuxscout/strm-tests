import os
import sys
import pytest
from fastapi.testclient import TestClient
from web.app import app

@pytest.fixture
def client():
    return TestClient(app)

# @pytest.mark.skip(reason="Skipping home page test for now")
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "base.html" in response.text  # Check if the template is rendered

# @pytest.mark.skip(reason="Skipping quiz generation test for now")
def test_get_quiz(client):
    response = client.get("/quiz")
    assert response.status_code == 200
    assert "quiz.html" in response.text  # Check if the quiz template is rendered

# @pytest.mark.skip(reason="Skipping quiz submission test for now")
def test_submit_quiz(client):
    # Mocking the quiz_builder methods for testing
    # You may need to use a mocking library like unittest.mock to mock the behavior of QuizBuilder
    response = client.post("/submit", data={"command": "random", "category": "random"})
    assert response.status_code == 200
    assert "result.html" in response.text  # Check if the result template is rendered

# @pytest.mark.skip(reason="Skipping quiz submission test for now")
def test_get_categories(client):
    response = client.get("/api/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Check if the response is a dictionary

# @pytest.mark.skip(reason="Skipping quiz submission test for now")
def test_get_commands(client):
    response = client.get("/api/commands")
    assert response.status_code == 200
    assert isinstance(response.json(), dict), f"The result type is {type(response.json())}"  # Check if the response is a dictionary

    # Test with a category filter
    response = client.get("/api/commands?category=some_category")  # Replace 'some_category' with an actual category
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Check if the response is a dictionary


@pytest.mark.skip(reason="Skipping quiz submission test for now")
def test_get_random_commands(client):
    response = client.get("/api/random-commands")
    assert response.status_code == 200
    assert "commands_list" in response.json()  # Check if the response contains 'commands_list'

    response = client.get("/api/random-commands?n=5")
    assert response.status_code == 200
    assert "commands_list" in response.json()  # Check if the response contains 'commands_list'

if __name__ == "__main__":
    pytest.main()

