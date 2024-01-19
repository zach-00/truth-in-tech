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
    def get(self, username: str) -> Union[AccountOutWithPassword, DuplicateAccountError]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute("SELECT * FROM accounts WHERE username = %s", [username])
                    result = db.fetchone()
                    if result:
                        print(result)
                        if len(result) == 6:
                            id, username, first_name, last_name, hashed_password, email = result
                            return AccountOutWithPassword(id=id, username=username, first_name=first_name, last_name=last_name, hashed_password=hashed_password, email=email)
        except Exception as e:
            print(f"Error in get account: {e}")
            return None

    def create(self, info: AccountIn, hashed_password: str) -> Union[AccountOutWithPassword, DuplicateAccountError]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO accounts
                            (username, first_name, last_name, hashed_password, email)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING id, username, first_name, last_name, hashed_password;
                        """,
                        [
                            info.username,
                            info.first_name,
                            info.last_name,
                            hashed_password,
                            info.email
                        ]
                    )
                    id, username, first_name, last_name, hashed_password = result.fetchone()
                    return AccountOutWithPassword(
                        id=id, username=username, first_name=first_name, last_name=last_name, hashed_password=hashed_password
                    )
        except Exception as e:
            print(f"Error in create account: {e}")
            raise DuplicateAccountError(message="Cannot create an account with those credentials")

    # def account_in_to_out(self, id: int, info: AccountIn):
    #     old_data = info.dict()
    #     return AccountOutWithPassword(id=id, **old_data)
