from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.documents_model import DocumentsModel
from schemas.documents_schema import DocumentsSchema
from core.deps import get_session



router = APIRouter()


# POST Documentos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=DocumentsSchema)
async def post_documento(documento: DocumentsSchema, db: AsyncSession = Depends(get_session)):
    novo_documento: DocumentsModel = DocumentsModel(nome_doc=documento.nome_doc, tipo=documento.tipo, origem=documento.origem)

    db.add(novo_documento)
    await db.commit()

    return novo_documento


# GET Documentos
@router.get('/', response_model=List[DocumentsSchema])
async def get_documentos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DocumentsModel)
        result = await session.execute(query)
        documentos: List[DocumentsModel] = result.scalars().unique().all()

        return documentos


# # GET Documento
# @router.get('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_200_OK)
# async def get_artigo(artigo_id: int, db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(ArtigoModel).filter(ArtigoModel.id == artigo_id)
#         result = await session.execute(query)
#         artigo: ArtigoModel = result.scalars().unique().one_or_none()

#         if artigo:
#             return artigo
#         else:
#             raise HTTPException(detail='Artigo não encontrado',
#                                 status_code=status.HTTP_404_NOT_FOUND)


# # PUT Documento
# @router.put('/{artigo_id}', response_model=ArtigoSchema, status_code=status.HTTP_202_ACCEPTED)
# async def put_artigo(artigo_id: int, artigo: ArtigoSchema, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
#     async with db as session:
#         query = select(ArtigoModel).filter(ArtigoModel.id == artigo_id)
#         result = await session.execute(query)
#         artigo_up: ArtigoModel = result.scalars().unique().one_or_none()

#         if artigo_up:
#             if artigo.titulo:
#                 artigo_up.titulo = artigo.titulo
#             if artigo.descricao:
#                 artigo_up.descricao = artigo.descricao
#             if artigo.url_fonte:
#                 artigo_up.url_fonte = artigo.url_fonte
#             if usuario_logado.id != artigo_up.usuario_id:
#                 artigo_up.usuario_id = usuario_logado.id

#             await session.commit()

#             return artigo_up
#         else:
#             raise HTTPException(detail='Artigo não encontrado',
#                                 status_code=status.HTTP_404_NOT_FOUND)


# # DELETE Documento
# @router.delete('/{artigo_id}', status_code=status.HTTP_204_NO_CONTENT)
# async def delete_artigo(artigo_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
#     async with db as session:
#         query = select(ArtigoModel).filter(ArtigoModel.id == artigo_id).filter(
#             ArtigoModel.usuario_id == usuario_logado.id)
#         result = await session.execute(query)
#         artigo_del: ArtigoModel = result.scalars().unique().one_or_none()

#         if artigo_del:
#             await session.delete(artigo_del)
#             await session.commit()

#             return Response(status_code=status.HTTP_204_NO_CONTENT)
#         else:
#             raise HTTPException(detail='Artigo não encontrado',
#                                 status_code=status.HTTP_404_NOT_FOUND)
