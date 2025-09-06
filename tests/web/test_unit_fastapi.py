import os
import sys
import pytest
from fastapi.testclient import TestClient
from web.app import app, quiz_builder

@pytest.fixture
def client():
    return TestClient(app)
@pytest.fixture
def builder():
    # You may need to pass a templates_dir if question_builder expects it
    return quiz_builder

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


# @pytest.mark.skip(reason="Skipping quiz submission test for now")
def test_get_random_commands(client):
    response = client.get("/api/random-commands")
    assert response.status_code == 200
    assert "commands_list" in response.json()  # Check if the response contains 'commands_list'

    response = client.get("/api/random-commands?n=5")
    assert response.status_code == 200
    assert "commands_list" in response.json()  # Check if the response contains 'commands_list'



# @pytest.mark.skip(reason="To be implemented later")
def test_submit_valid_random_command(client):
    """Test submitting with random command and random category."""
    response = client.post("/submit", data={"command": "random", "category": "random"})
    assert response.status_code == 200
    assert "question" in response.text
    assert "answer" in response.text


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_valid_specific_command(client):
    """Test submitting a valid specific command."""
    response = client.post("/submit", data={"command": "float", "category": "encoding"})
    assert response.status_code == 200
    assert "question" in response.text
    assert "answer" in response.text


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_invalid_category(client):
    """Test submitting with an invalid category."""
    response = client.post("/submit", data={"command": "float", "category": "not_a_category"})
    assert response.status_code == 400
    assert "Invalid category" in response.json()["detail"]


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_invalid_command(client):
    """Test submitting with an invalid command."""
    response = client.post("/submit", data={"command": "not_a_command", "category": "encoding"})
    assert response.status_code == 400
    assert "Invalid command" in response.json()["detail"]


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_command_not_in_category(client):
    """Test submitting a valid command but wrong category."""
    # Example: "float" belongs to "encoding", not "boolean algebra"
    response = client.post("/submit", data={"command": "float", "category": "boolean algebra"})
    assert response.status_code == 400
    assert "does not belong to category" in response.json()["detail"]


# @pytest.mark.skip(reason="Manual run: test all commands through FastAPI /submit endpoint")
def test_all_commands_via_api(client: TestClient, builder):
    """
    Iterate over all commands in quiz_builder and ensure
    that POST /submit runs without errors for each.
    """
    commands = builder.get_commands_list()
    assert commands, "No commands available in quiz_builder."

    for cmd in commands:
        response = client.post(
            "/submit",
            data={"command": cmd, "category": ""},  # category left blank
        )
        assert response.status_code == 200, f"/submit failed for command '{cmd}', status code {response.status_code} details:{response.text}"
        assert "question" in response.text.lower(), f"No question rendered for command '{cmd}', status code {response.status_code} details:{response.text}"
        assert "answer" in response.text.lower(), f"No answer rendered for command '{cmd}', status code {response.status_code} details:{response.text}"


if __name__ == "__main__":
    pytest.main()

