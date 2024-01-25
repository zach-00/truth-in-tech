from fastapi import APIRouter, Depends, Response
from queries.companies import (
    CompanyRepo,
    CompaniesOut,
    CompanyOut,
    Error,
    CompanyIn,
    CompanyOutWithReviewCount,
)
from typing import Union, List
from authenticator import authenticator


router = APIRouter()


@router.get("/companies/top10", response_model=List[CompanyOutWithReviewCount])
def get_top_10_companies(repo: CompanyRepo = Depends()):
    return repo.get_top_10_companies()


@router.delete("/companies/{company_id}", response_model=bool)
async def delete_company(
    company_id: int,
    repo: CompanyRepo = Depends(),
    company_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete(company_id)


@router.get("/companies/{company_id}", response_model=Union[CompanyOut, Error])
def get_one_company(
    company_id: int,
    response: Response,
    repo: CompanyRepo = Depends(),
):
    return repo.get_one_company(company_id)


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


@router.put(
    "/companies/update/{company_id}", response_model=Union[CompanyOut, Error]
)
def update_company(
    company_id: int,
    company: CompanyIn,
    response: Response,
    repo: CompanyRepo = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.update_company(company_id, company)
