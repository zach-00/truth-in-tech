from fastapi import APIRouter, Depends, status, HTTPException, Response
from pydantic import BaseModel
from queries.companies import CompanyRepo, CompaniesOut, CompanyOut, Error
from typing import List, Union


router = APIRouter()



@router.get("/companies", response_model=Union[CompaniesOut, Error])
def get_companies(repo: CompanyRepo = Depends()):
    return {"companies": repo.get_companies()}
