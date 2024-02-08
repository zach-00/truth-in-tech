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
    company_id: int


class ReviewInUpdate(BaseModel):
    anonymous: bool
    salary: Optional[int]
    job_title: str
    location: Optional[str]
    body: str


class ReviewOutPlus(BaseModel):
    id: int
    anonymous: bool
    salary: float
    job_title: str
    location: Optional[str]
    body: str
    account_id: int
    company_id: int
    date_created: date
    likes: int
    company_name: str
    company_logo: str
    username: str
    first_name: str
    last_name: str


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


class ReviewOut10(BaseModel):
    id: int
    salary: float
    job_title: str
    location: Optional[str]
    body: str
    username: str
    company_name: str
    company_logo: str
    date_created: date


class ReviewRepository:
    def create(self, review: ReviewIn, account_id: int) -> ReviewOutPlus:
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
                            account_id,
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
                    r = ReviewOutPlus(
                        id=review[0],
                        anonymous=review[1],
                        salary=review[2],
                        job_title=review[3],
                        location=review[4],
                        body=review[5],
                        account_id=review[6],
                        company_id=review[7],
                        date_created=review[8],
                        likes=review[9],
                        company_name=review[10],
                        company_logo=review[11],
                        username=review[12],
                        first_name=review[13],
                        last_name=review[14],
                    )
                    return r
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def get_one_review(self, review_id: int) -> ReviewOutPlus:
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
                        WHERE reviews.id = %s
                        """,
                        [review_id],
                    )
                    review = result.fetchone()

                    return ReviewOutPlus(
                        id=review[0],
                        anonymous=review[1],
                        salary=review[2],
                        job_title=review[3],
                        location=review[4],
                        body=review[5],
                        account_id=review[6],
                        company_id=review[7],
                        date_created=review[8],
                        likes=review[9],
                        company_name=review[10],
                        company_logo=review[11],
                        username=review[12],
                        first_name=review[13],
                        last_name=review[14],
                    )
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def get_all(self, company_id: int) -> Union[List[ReviewOutPlus], dict]:
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
                        ORDER BY reviews.id DESC;
                        """,
                        [company_id],
                    )
                    record = result.fetchall()
                    print(record)
                    reviews = []
                    for review in record:
                        r = ReviewOutPlus(
                            id=review[0],
                            anonymous=review[1],
                            salary=review[2],
                            job_title=review[3],
                            location=review[4],
                            body=review[5],
                            account_id=review[6],
                            company_id=review[7],
                            date_created=review[8],
                            likes=review[9],
                            company_name=review[10],
                            company_logo=review[11],
                            username=review[12],
                            first_name=review[13],
                            last_name=review[14],
                        )
                        reviews.append(r)
                    return reviews
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def get_top_10_reviews(self) -> Union[List[ReviewOut10], None]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM top_ten;
                        """,
                    )
                    reviews = result.fetchall()
                    print(reviews)
                    top_10_list = []
                    for i in reviews:
                        review = ReviewOut10(
                            id=i[0],
                            salary=i[1],
                            job_title=i[2],
                            location=i[3],
                            body=i[4],
                            username=i[5],
                            company_name=i[6],
                            company_logo=i[7],
                            date_created=i[8],
                        )
                        top_10_list.append(review)
                    return top_10_list
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def update_review(
        self, review_id: int, review: ReviewInUpdate, account_id: int
    ):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE reviews
                        SET anonymous = %s,
                            salary = %s,
                            job_title = %s,
                            location = %s,
                            body = %s
                        WHERE id = %s
                        AND account_id = %s
                        RETURNING id,
                            anonymous,
                            salary,
                            job_title,
                            location,
                            body,
                            account_id,
                            company_id,
                            date_created;
                        """,
                        [
                            review.anonymous,
                            review.salary,
                            review.job_title,
                            review.location,
                            review.body,
                            review_id,
                            account_id,
                        ],
                    )
                    (
                        id,
                        anonymous,
                        salary,
                        job_title,
                        location,
                        body,
                        account_id,
                        company_id,
                        date_created,
                    ) = result.fetchone()
                    return ReviewOut(
                        id=id,
                        anonymous=anonymous,
                        salary=salary,
                        job_title=job_title,
                        location=location,
                        body=body,
                        account_id=account_id,
                        company_id=company_id,
                        date_created=date_created,
                    )
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def delete_review(self, review_id: int, account_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        DELETE FROM reviews
                        WHERE id = %s
                        AND account_id = %s
                        RETURNING id;
                        """,
                        [review_id, account_id],
                    )

                    if result.fetchone()[0]:
                        return True

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def add_like(self, review_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE reviews
                        SET likes = likes + 1
                        WHERE id = %s
                        RETURNING id;
                        """,
                        [review_id],
                    )

                    if result.fetchone()[0]:
                        return True

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
