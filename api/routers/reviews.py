from fastapi import (
    APIRouter,
    Depends,
)

from typing import List, Union
from queries.reviews import ReviewIn, ReviewOut, ReviewRepository, Error
from authenticator import authenticator

router = APIRouter()


@router.post("/reviews", response_model=ReviewOut)
async def create_review(
    review: ReviewIn,
    repo: ReviewRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    result = repo.create(review)
    return result


@router.get(
    "/reviews/{company_id}", response_model=Union[List[ReviewOut], None]
)
def get_company_reviews(
    company_id: int,
    repo: ReviewRepository = Depends(),
):
    return repo.get_all(company_id)
