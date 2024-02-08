from fastapi import (
    APIRouter,
    Depends,
)

from typing import List, Union
from queries.reviews import (
    ReviewIn,
    ReviewInUpdate,
    ReviewOut,
    ReviewOutPlus,
    ReviewOut10,
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


@router.get("/reviews/{review_id}", response_model=ReviewOutPlus)
def get_one_review(
    review_id: int,
    repo: ReviewRepository = Depends(),
):
    return repo.get_one_review(review_id)


@router.get(
    "/reviews/companies/{company_id}", response_model=List[ReviewOutPlus]
)
def get_company_reviews(
    company_id: int,
    repo: ReviewRepository = Depends(),
):
    return repo.get_all(company_id)


@router.get("/reviews/top10/", response_model=List[ReviewOut10])
def get_top_10_reviews(repo: ReviewRepository = Depends()):
    return repo.get_top_10_reviews()


@router.put("/reviews/{review_id}/like")
def add_like(
    review_id: int,
    repo: ReviewRepository = Depends(),
):
    return repo.add_like(review_id)


@router.put("/reviews/{review_id}", response_model=Union[ReviewOut, Error])
async def update_review(
    review_id: int,
    review: ReviewInUpdate,
    repo: ReviewRepository = Depends(),
    account_info: dict = Depends(authenticator.get_current_account_data),
):
    return repo.update_review(review_id, review, account_info["id"])


@router.delete("/reviews/{review_id}")
def delete_review(
    review_id,
    account_info: dict = Depends(authenticator.get_current_account_data),
    repo: ReviewRepository = Depends(),
):
    return repo.delete_review(review_id, account_info["id"])
