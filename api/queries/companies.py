from queries.pool import pool
from pydantic import BaseModel
from typing import List, Union



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
                            company_logo=record[2]
                        )
                        companies_list.append(company)

            return companies_list

        except Exception as e:
            return {"message": "Unable to retrieve all companies"}
