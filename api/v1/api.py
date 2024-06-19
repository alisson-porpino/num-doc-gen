from fastapi import APIRouter

#from api.v1.endpoints import artigo
#from api.v1.endpoints import usuario
from api.v1.endpoints import documents


api_router = APIRouter()

api_router.include_router(documents.router, prefix='/documents', tags=['documents'])
#api_router.include_router(artigo.router, prefix='/artigos', tags=['artigos'])
#api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])
