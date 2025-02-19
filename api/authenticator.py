# authenticator.py
import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from typing import Optional
from queries.accounts import AccountRepo, AccountOut, AccountOutWithPassword


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        accounts: AccountRepo,
    ) -> Optional[AccountOutWithPassword]:
        # Use your repo to get the account based on the
        # username (which could be an email)
        try:
            account = accounts.get(username)
            if account:
                return account
        except Exception as e:
            print(f"Error in get account: {e}")
        return None

    def get_account_getter(
        self,
        accounts: AccountRepo = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOutWithPassword):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.username, AccountOut(**account.dict())


authenticator = MyAuthenticator(os.environ.get("SIGNING_KEY"))
