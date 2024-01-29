from main import app
from fastapi.testclient import TestClient
from authenticator import authenticator
from pydantic import BaseModel
from queries.companies import CompanyIn, CompanyOut, CompanyRepo

client = TestClient(app)


class EmptyCompanyRepo:
    def get_companies(self):
        return []

    def create(self, company: CompanyIn) -> CompanyOut:
        return CompanyOut(
            id=1,
            company_name=company.company_name,
            company_logo=company.company_logo,
        )


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


class AccountOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str


def fake_get_current_account_data():
    return AccountOut(
        id=1, username="happy_coding", first_name="happy", last_name="coding"
    )


def test_create_company():
    overrides = {
        CompanyRepo: EmptyCompanyRepo,
        authenticator.get_current_account_data: fake_get_current_account_data,
    }
    app.dependency_overrides = overrides
    company = {"company_name": "TestCompany", "company_logo": "Logo"}
    expected = {
        "id": 1,
        "company_name": "TestCompany",
        "company_logo": "Logo",
    }

    response = client.post("/companies", json=company)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected
