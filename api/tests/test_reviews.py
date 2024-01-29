from fastapi.testclient import TestClient
from main import app
from authenticator import authenticator
from queries.reviews import ReviewRepository

client = TestClient(app)


class FakeReviewRepo:
    def update_review(self, review_id, review, account_id):
        result = {
            "id": review_id,
            "account_id": account_id,
            "company_id": 1,
            "date_created": "2024-01-28",
        }

        result.update(review)
        return result


def fake_get_current_account_data():
    return {
        "id": 1,
        "username": "zdawg",
        "first_name": "zach",
        "last_name": "walkowiak",
    }


def test_update_review():
    # Arrange
    overrides = {
        ReviewRepository: FakeReviewRepo,
        authenticator.get_current_account_data: fake_get_current_account_data,
    }

    app.dependency_overrides = overrides

    review = {
        "anonymous": True,
        "salary": 1000,
        "job_title": "SWE",
        "location": "LA",
        "body": "stuff",
    }

    expected = {
        "id": 1,
        "anonymous": True,
        "salary": 1000,
        "job_title": "SWE",
        "location": "LA",
        "body": "stuff",
        "account_id": 1,
        "company_id": 1,
        "date_created": "2024-01-28",
    }

    # Act
    review_id = 1
    response = client.put(f"/reviews/{review_id}", json=review)
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == expected
