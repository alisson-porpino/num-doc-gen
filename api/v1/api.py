from fastapi import APIRouter

from api.v1.endpoints import documentos
from api.v1.endpoints import usuario

api_router = APIRouter()

api_router.include_router(documentos.router, prefix='/documentos', tags=['documentos'])
api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])
