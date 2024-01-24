from fastapi import APIRouter, Depends, Response
from queries.companies import (
    CompanyRepo,
    CompaniesOut,
    CompanyOut,
    Error,
    CompanyIn,
)
from typing import Union
from authenticator import authenticator


router = APIRouter()


@router.get("/companies", response_model=Union[CompaniesOut, Error])
def get_companies(repo: CompanyRepo = Depends()):
    return {"companies": repo.get_companies()}


@router.post("/companies", response_model=Union[CompanyOut, Error])
async def create_company(
    company: CompanyIn,
    response: Response,
    repo: CompanyRepo = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(company)
