from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import date
from queries.pool import pool
from fastapi import HTTPException


class Error(BaseModel):
    message: str


class ReviewIn(BaseModel):
    anonymous: bool
    salary: Optional[int]
    job_title: str
    location: Optional[str]
    body: str
    account_id: int
    company_id: int


class ReviewOut(BaseModel):
    id: int
    anonymous: bool
    salary: float
    job_title: str
    location: Optional[str]
    body: str
    account_id: int
    company_id: int
    date_created: date
    company_name: str
    company_logo: str
    username: str
    first_name: str
    last_name: str


class ReviewRepository:
    def create(self, review: ReviewIn) -> ReviewOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO reviews
                            (anonymous,
                            salary, job_title,
                            location, body,
                            account_id,
                            company_id)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s)
                            RETURNING id;
                        """,
                        [
                            review.anonymous,
                            review.salary,
                            review.job_title,
                            review.location,
                            review.body,
                            review.account_id,
                            review.company_id,
                        ],
                    )
                    record = result.fetchone()
                    id = record[0]
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            reviews.*,
                            companies.company_name,
                            companies.company_logo,
                            accounts.username,
                            accounts.first_name,
                            accounts.last_name
                        FROM reviews
                        INNER JOIN companies ON
                            companies.id = reviews.company_id
                        INNER JOIN accounts ON
                            accounts.id = reviews.account_id
                        WHERE reviews.id = %s
                        ORDER BY date_created;
                        """,
                        [
                            id,
                        ],
                    )
                    review = result.fetchone()
                    print(review)
                    r = ReviewOut(
                        id=review[0],
                        anonymous=review[1],
                        salary=review[2],
                        job_title=review[3],
                        location=review[4],
                        body=review[5],
                        account_id=review[6],
                        company_id=review[7],
                        date_created=review[8],
                        company_name=review[9],
                        company_logo=review[10],
                        username=review[11],
                        first_name=review[12],
                        last_name=review[13],
                    )
                    return r
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=e.args,
            )

    def get_all(self, company_id: int) -> Union[List[ReviewOut], dict]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            reviews.*,
                            companies.company_name,
                            companies.company_logo,
                            accounts.username,
                            accounts.first_name,
                            accounts.last_name
                        FROM reviews
                        INNER JOIN companies ON
                            companies.id = reviews.company_id
                        INNER JOIN accounts ON
                            accounts.id = reviews.account_id
                        WHERE company_id = %s
                        ORDER BY date_created;
                        """,
                        [company_id],
                    )

                    record = result.fetchall()
                    print(record)
                    reviews = []
                    for review in record:
                        r = ReviewOut(
                            id=review[0],
                            anonymous=review[1],
                            salary=review[2],
                            job_title=review[3],
                            location=review[4],
                            body=review[5],
                            account_id=review[6],
                            company_id=review[7],
                            date_created=review[8],
                            company_name=review[9],
                            company_logo=review[10],
                            username=review[11],
                            first_name=review[12],
                            last_name=review[13],
                        )
                        reviews.append(r)
                    return reviews
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=e.args,
            )
