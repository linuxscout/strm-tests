import os
import sys
import pytest
from fastapi.testclient import TestClient
from web.app import app, quiz_builder, Submission

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

    response = client.post("/submit", json={"command": "random", "category": "random", 'args': {}})
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

    response = client.post("/submit", json={"command": "random", "category": "random", 'args': {}})
    assert response.status_code == 200
    assert "question" in response.text
    assert "answer" in response.text


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_valid_specific_command(client):
    """Test submitting a valid specific command."""
    args = {"float":{"float":'15'}}
    response = client.post("/submit", json={"command": "float", "category": "encoding", "args":args})
    assert response.status_code == 200
    assert "question" in response.text
    assert "answer" in response.text


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_invalid_category(client):
    """Test submitting with an invalid category."""
    response = client.post("/submit", json={"command": "float", "category": "not_a_category", "args":{}})
    assert response.status_code == 400
    assert "Invalid category" in response.json()["detail"]


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_invalid_command(client):
    """Test submitting with an invalid command."""
    response = client.post("/submit", json={"command": "not_a_command", "category": "encoding", "args":{}})
    assert response.status_code == 400
    assert "Invalid command" in response.json()["detail"]


# @pytest.mark.skip(reason="To be implemented later")
def test_submit_command_not_in_category(client):
    """Test submitting a valid command but wrong category."""
    # Example: "float" belongs to "encoding", not "boolean algebra"
    response = client.post("/submit", json={"command": "float", "category": "boolean algebra", "args":{}})
    assert response.status_code == 400
    assert "does not belong to category" in response.json()["detail"]


# @pytest.mark.skip(reason="Manual run: test all commands through FastAPI /submit endpoint")
def test_all_commands_via_api_simple(client: TestClient, builder):
    """
    Iterate over all commands in quiz_builder and ensure
    that POST /submit runs without errors for each.
    """
    commands = builder.get_commands_list()
    assert commands, "No commands available in quiz_builder."

    for cmd in commands:
        response = client.post(
            "/submit",
            json={"command": cmd, "category": "","args":{}},  # category left blank
        )
        assert response.status_code == 200, f"/submit failed for command '{cmd}', status code {response.status_code} details:{response.text}"
        assert "question" in response.text.lower(), f"No question rendered for command '{cmd}', status code {response.status_code} details:{response.text}"
        assert "answer" in response.text.lower(), f"No answer rendered for command '{cmd}', status code {response.status_code} details:{response.text}"


# @pytest.mark.skip(reason="Manual run: test all category-command pairs through FastAPI /submit endpoint")
def test_all_commands_via_api(client: TestClient, builder):
    """
    Iterate over all commands in quiz_builder and ensure
    that POST /submit runs without errors for each.
    Collect all failing commands instead of failing fast.
    """
    commands = builder.get_commands_list()
    assert commands, "No commands available in quiz_builder."
    default_args = builder.get_loaded_args()
    failed = []  # collect failures here

    for cmd in commands:
        response = client.post(
            "/submit",
            json={"command": cmd, "category": "","args":default_args},  # category left blank
        )

        # Check status
        if response.status_code != 200:
            failed.append((cmd, f"status={response.status_code}, details={response.text}"))
            continue

        # Check for question/answer presence
        if "question" not in response.text.lower():
            failed.append((cmd, "Missing 'question' in response"))
        if "answer" not in response.text.lower():
            failed.append((cmd, "Missing 'answer' in response"))

        # Check for generation errors
        if "error generating question" in response.text.lower():
            failed.append((cmd, "Contains 'Error generating question'"))

    # If any failures, raise with summary
    if failed:
        msg = "\n".join([f"Command '{cmd}' failed: {reason}" for cmd, reason in failed])
        pytest.fail(f"The following commands failed:\n{msg}")


# @pytest.mark.skip(reason="Manual run: test all category-command pairs through FastAPI /submit endpoint")
def test_all_category_command_pairs_via_api(client: TestClient, builder):
    """
    Iterate over all (category, command) pairs in quiz_builder and ensure
    that POST /submit runs without errors and category consistency is valid.
    """
    categories = builder.get_categories()
    assert categories, "No categories available in quiz_builder."

    for cat, meta in categories.items():
        commands = [c["name"] for c in meta["commands"]]
        assert commands, f"No commands found for category '{cat}'"

        for cmd in commands:
            response = client.post(
                "/submit",
                json={"command": cmd, "category": cat,"args":{}},
            )
            if response.status_code != 200:
                try:
                    details = response.json()
                except Exception:
                    details = response.text
                pytest.fail(f"/submit failed for category '{cat}', command '{cmd}', "
                            f"status={response.status_code}, details={details}")

            assert "question" in response.text.lower(), f"No question rendered for category '{cat}', command '{cmd}', status code {response.status_code} details:{response.text}"
            assert "answer" in response.text.lower(), f"No answer rendered for category '{cat}', command '{cmd}', status code {response.status_code} details:{response.text}"


if __name__ == "__main__":
    pytest.main()

