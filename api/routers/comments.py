from fastapi import APIRouter, Depends

from typing import List
from queries.comments import (
    CommentIn,
    CommentOut,
    CommentOutPlus,
    CommentRepository,
    CommentInUpdate,
)

from authenticator import authenticator

router = APIRouter()


@router.post("/reviews/{review_id}/comments", response_model=CommentOut)
async def create_comment(
    comment: CommentIn,
    review_id: int,
    repo: CommentRepository = Depends(),
    account_info: dict = Depends(authenticator.get_current_account_data),
):
    result = repo.create(comment, review_id, account_info["id"])
    return result


@router.get(
    "/reviews/{review_id}/comments", response_model=List[CommentOutPlus]
)
def get_review_comments(
    review_id: int,
    repo: CommentRepository = Depends(),
):
    return repo.get_all(review_id)


@router.put("/comments/{comment_id}", response_model=CommentOut)
async def update_comment(
    comment: CommentInUpdate,
    comment_id: int,
    repo: CommentRepository = Depends(),
    account_info: dict = Depends(authenticator.get_current_account_data),
):
    return repo.update_comment(comment, comment_id, account_info["id"])


@router.delete("/comments/{comment_id}")
def delete_comment(
    comment_id,
    account_info: dict = Depends(authenticator.get_current_account_data),
    repo: CommentRepository = Depends(),
):
    return repo.delete_review(comment_id, account_info["id"])
