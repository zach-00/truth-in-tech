from fastapi import (
    APIRouter,
    Depends,
)

from typing import List, Union
from queries.reviews import (
    ReviewIn,
    ReviewInUpdate,
    ReviewOut,
    ReviewRepository,
    Error,
)

from authenticator import authenticator

router = APIRouter()


@router.post("/reviews", response_model=ReviewOut)
async def create_review(
    review: ReviewIn,
    repo: ReviewRepository = Depends(),
    account_info: dict = Depends(authenticator.get_current_account_data),
):
    result = repo.create(review, account_info["id"])
    return result


@router.get(
    "/reviews/{company_id}", response_model=Union[List[ReviewOut], None]
)
def get_company_reviews(
    company_id: int,
    repo: ReviewRepository = Depends(),
):
    return repo.get_all(company_id)


@router.put("/reviews/{review_id}", response_model=Union[ReviewOut, Error])
def update_review(
    review_id: int,
    review: ReviewInUpdate,
    repo: ReviewRepository = Depends(),
    account_info: dict = Depends(authenticator.get_current_account_data),
):
    return repo.update_review(review_id, review, account_info["id"])
