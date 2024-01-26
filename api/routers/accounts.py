# router.py
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Response,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel
import asyncio

from queries.accounts import (
    AccountIn,
    AccountOut,
    AccountRepo,
    DuplicateAccountError,
    BaseExceptionError,
)


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.put("/accounts/{account_id}", response_model=AccountOut | HttpError)
async def update_account(
    account_id: int,
    new_info: AccountIn,
    repo: AccountRepo = Depends(),
):
    try:
        updated_account = repo.update(
            account_id, new_info
        )  # cannot await repo.update directly becuse its not

        if asyncio.iscoroutine(
            updated_account
        ):  # checks if updated_account is coroutine using asyncio.iscoroutine
            updated_account = (
                await updated_account
            )  # awaits when if statement comes back true

        if updated_account:
            return updated_account
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found",
            )
    except BaseExceptionError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: AccountOut = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


@router.delete("/accounts", response_model=bool | HttpError)
async def delete_account(
    request: Request,
    response: Response,
    session_getter=Depends(authenticator.get_session_getter),
    jwt: dict = Depends(authenticator._try_jwt),
    account_info: dict = Depends(authenticator.try_get_current_account_data),
    repo: AccountRepo = Depends(),
) -> bool:
    try:
        await authenticator.logout(request, response, session_getter, jwt)
        return repo.delete(account_info["id"])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/accounts", response_model=AccountToken | HttpError)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    repo: AccountRepo = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = repo.create(info, hashed_password)
        form = AccountForm(username=info.username, password=info.password)
        token = await authenticator.login(response, request, form, repo)
        return AccountToken(account=account, **token.dict())

    except DuplicateAccountError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
