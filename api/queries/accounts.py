from fastapi import HTTPException
from pydantic import BaseModel
from queries.pool import pool
from typing import Union


class BaseExceptionError(BaseException):
    message: str


class DuplicateAccountError(BaseExceptionError):
    def __init__(self, message: str):
        self.message = message


class AccountIn(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: str


class AccountOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountRepo:
    def update(
        self, account_id: int, new_info: AccountIn
    ) -> Union[AccountOut, DuplicateAccountError]:
        try:
            from authenticator import (
                authenticator,
            )  # do this to keep from getting circular error,

            # since we already import quaries.accounts.py into authenticator//

            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET username = %s,
                            first_name = %s,
                            last_name = %s,
                            hashed_password = %s,
                            email = %s
                        WHERE id = %s
                        RETURNING id,
                            username,
                            first_name,
                            last_name,
                            email;
                        """,
                        [
                            new_info.username,
                            new_info.first_name,
                            new_info.last_name,
                            authenticator.hash_password(new_info.password),
                            new_info.email,
                            account_id,
                        ],
                    )
                    (
                        id,
                        username,
                        first_name,
                        last_name,
                        email,
                    ) = result.fetchone()
                    if result:
                        return AccountOut(
                            id=id,
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                        )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get(
        self, username: str
    ) -> Union[AccountOutWithPassword, DuplicateAccountError]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        "SELECT * FROM accounts WHERE username = %s",
                        [username],
                    )
                    result = db.fetchone()
                    if result:
                        if len(result) == 6:
                            (
                                id,
                                username,
                                first_name,
                                last_name,
                                hashed_password,
                                email,
                            ) = result
                            return AccountOutWithPassword(
                                id=id,
                                username=username,
                                first_name=first_name,
                                last_name=last_name,
                                hashed_password=hashed_password,
                                email=email,
                            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def delete(self, account_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                            DELETE FROM accounts
                            WHERE id = %s
                            RETURNING id;
                            """,
                        [account_id],
                    )
                    if result.fetchone()[0]:
                        return True
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def create(
        self, info: AccountIn, hashed_password: str
    ) -> Union[AccountOutWithPassword, DuplicateAccountError]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO accounts
                            (username,
                            first_name,
                            last_name,
                            hashed_password,
                            email)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING
                        id,
                        username,
                        first_name,
                        last_name,
                        hashed_password;
                        """,
                        [
                            info.username,
                            info.first_name,
                            info.last_name,
                            hashed_password,
                            info.email,
                        ],
                    )
                    (
                        id,
                        username,
                        first_name,
                        last_name,
                        hashed_password,
                    ) = result.fetchone()
                    return AccountOutWithPassword(
                        id=id,
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        hashed_password=hashed_password,
                    )
        except Exception:
            raise DuplicateAccountError(
                message="Cannot create an account with those credentials"
            )
