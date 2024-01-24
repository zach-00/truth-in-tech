from queries.pool import pool
from pydantic import BaseModel
from typing import List, Union
from fastapi import HTTPException


class CompanyIn(BaseModel):
    company_name: str
    company_logo: str


class CompanyOut(BaseModel):
    id: int
    company_name: str
    company_logo: str


class CompaniesOut(BaseModel):
    companies: list[CompanyOut]


class Error(BaseModel):
    message: str


class CompanyRepo:
    def get_companies(self) -> Union[List[CompanyOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM companies;
                        """,
                    )

                    companies = result.fetchall()
                    companies_list = []

                    for record in companies:
                        company = CompanyOut(
                            id=record[0],
                            company_name=record[1],
                            company_logo=record[2],
                        )
                        companies_list.append(company)

            return companies_list

        except Exception:
            return {"message": "Unable to retrieve all companies"}

    def create(self, company: CompanyIn) -> Union[CompanyOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO companies
                            (company_name, company_logo)
                        VALUES
                            (%s, %s)
                        RETURNING id;
                        """,
                        [
                            company.company_name,
                            company.company_logo,
                        ],
                    )
                    id = result.fetchone()[0]
                    return self.company_in_to_out(id, company)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=e.args,
            )

    def company_in_to_out(self, id: int, company: CompanyIn):
        old_data = company.dict()
        return CompanyOut(id=id, **old_data)
