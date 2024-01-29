from main import app
from fastapi.testclient import TestClient
from queries.companies import CompanyRepo


client = TestClient(app)


class EmptyCompanyRepo:
    def get_companies(self):
        return []


def test_get_companies():
    # Arrange
    app.dependency_overrides[CompanyRepo] = EmptyCompanyRepo

    # Act
    response = client.get("/companies")
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == {"companies": []}

    # Reset
    app.dependency_overrides.clear()
