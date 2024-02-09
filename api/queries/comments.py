from pydantic import BaseModel
from typing import List, Union
from datetime import date
from queries.pool import pool
from fastapi import HTTPException


class Error(BaseModel):
    message: str


class CommentIn(BaseModel):
    body: str


class CommentInUpdate(BaseModel):
    body: str


class CommentOutPlus(BaseModel):
    id: int
    body: str
    account_id: int
    review_id: int
    date_created: date
    reviewBody: str
    username: str
    first_name: str
    last_name: str


class CommentOut(BaseModel):
    id: int
    body: str
    account_id: int
    review_id: int
    date_created: date


class CommentRepository:
    def create(
        self, comment: CommentIn, review_id: int, account_id: int
    ) -> CommentOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO comments
                            (body,
                            account_id,
                            review_id)
                        VALUES
                            (%s, %s, %s)
                            RETURNING id;
                        """,
                        [
                            comment.body,
                            account_id,
                            review_id,
                        ],
                    )
                    record = result.fetchone()
                    id = record[0]
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            comments.*,
                            reviews.body,
                            accounts.username,
                            accounts.first_name,
                            accounts.last_name
                        FROM comments
                        INNER JOIN reviews ON
                            reviews.id = comments.review_id
                        INNER JOIN accounts ON
                            accounts.id = comments.account_id
                        WHERE comments.id = %s
                        ORDER BY comments.date_created;
                        """,
                        [
                            id,
                        ],
                    )
                    comment = result.fetchone()
                    r = CommentOutPlus(
                        id=comment[0],
                        body=comment[1],
                        account_id=comment[2],
                        review_id=comment[3],
                        date_created=comment[4],
                        reviewBody=comment[5],
                        username=comment[6],
                        first_name=comment[7],
                        last_name=comment[8],
                    )
                    return r
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def get_all(self, review_id: int) -> Union[List[CommentOutPlus], dict]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            comments.*,
                            reviews.body,
                            accounts.username,
                            accounts.first_name,
                            accounts.last_name
                        FROM comments
                        INNER JOIN reviews ON
                            reviews.id = comments.review_id
                        INNER JOIN accounts ON
                            accounts.id = comments.account_id
                        WHERE review_id = %s
                        ORDER BY comments.date_created DESC;
                        """,
                        [review_id],
                    )
                    record = result.fetchall()
                    comments = []
                    for comment in record:
                        r = CommentOutPlus(
                            id=comment[0],
                            body=comment[1],
                            account_id=comment[2],
                            review_id=comment[3],
                            date_created=comment[4],
                            reviewBody=comment[5],
                            username=comment[6],
                            first_name=comment[7],
                            last_name=comment[8],
                        )
                        comments.append(r)
                    return comments
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def update_comment(
        self,
        comment: CommentInUpdate,
        comment_id: int,
        account_id: int,
    ):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE comments
                        SET body = %s
                        WHERE id = %s
                        AND account_id = %s
                        RETURNING
                            id,
                            body,
                            account_id,
                            review_id,
                            date_created;
                        """,
                        [comment.body, comment_id, account_id],
                    )
                    (
                        id,
                        body,
                        account_id,
                        review_id,
                        date_created,
                    ) = result.fetchone()
                    return CommentOut(
                        id=id,
                        body=body,
                        account_id=account_id,
                        review_id=review_id,
                        date_created=date_created,
                    )
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

    def delete_review(self, comment_id: int, account_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        DELETE FROM comments
                        WHERE id = %s
                        AND account_id = %s
                        RETURNING id;
                        """,
                        [comment_id, account_id],
                    )

                    if result.fetchone()[0]:
                        return True

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
