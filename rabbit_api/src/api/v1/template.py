from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.post('/template')
async def add_template():
    return HTTPStatus.OK
