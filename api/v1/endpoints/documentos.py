from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.documentos_model import DocumentosModel
from models.usuarios_model import UsuarioModel
from schemas.documentos_schema import DocumentosSchema, DocumentosCreateSchema
from core.deps import get_session, get_current_user

from sqlalchemy import select, func


router = APIRouter()


#Função para calcular e gerar número de registro.
async def calcular_num_reg(db, tipo_destino: str):
    
    # Obtém o ano atual
    ano_atual = datetime.now().year

    # Obtém a quantidade de dados da tabela de acordo com um filtro.
    # Esse filtro é o nome do próprio dado contido na coluna "tipo_destino"
    stmt = select(func.count()).select_from(DocumentosModel).where(DocumentosModel.tipo_destino == tipo_destino)
    total_linhas = await db.scalar(stmt)

    # Gera e formata o num_reg como três dígitos, seguido pelo ano atual
    num_reg = f"{total_linhas + 1:03d}/{ano_atual}"
    return num_reg


# POST Documentos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=DocumentosSchema)
async def post_documento(documento: DocumentosCreateSchema, usuario_logado:UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):

    num_reg_calculado = await calcular_num_reg(db, documento.tipo_destino)

    novo_documento: DocumentosModel = DocumentosModel(
        num_reg=num_reg_calculado, objeto=documento.objeto, origem=documento.origem, tipo_doc=documento.tipo_doc, tipo_destino=documento.tipo_destino, criador_id=usuario_logado.id_user)

    db.add(novo_documento)
    await db.commit()
    await db.refresh(novo_documento)

    return novo_documento


# GET Documentos
@router.get('/', response_model=List[DocumentosSchema])
async def get_documentos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DocumentosModel)
        result = await session.execute(query)
        documentos: List[DocumentosModel] = result.scalars().unique().all()

        return documentos
    
# GET Documento
@router.get('/{documento_id}', response_model=DocumentosSchema, status_code=status.HTTP_200_OK)
async def get_documento(documento_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DocumentosModel).filter(DocumentosModel.id_doc == documento_id)
        result = await session.execute(query)
        documento: DocumentosModel = result.scalars().unique().one_or_none()

        if documento:
            return documento
        else:
            raise HTTPException(detail='Documento não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# # PUT Documento (Não utilizavel)
# @router.put('/{documento_id}', response_model=DocumentosSchema, status_code=status.HTTP_202_ACCEPTED)
# async def put_documento(documento_id: int, documento: DocumentosSchema, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
#     async with db as session:
#         query = select(DocumentosModel).filter(DocumentosModel.id_doc == documento_id)
#         result = await session.execute(query)
#         documento_update: DocumentosModel = result.scalars().unique().one_or_none()

#         if documento_update:
#             if documento.num_reg:
#                 documento_update.num_reg = documento.num_reg
#             if documento.objeto:
#                 documento_update.objeto = documento.objeto
#             if documento.tipo_doc:
#                 documento_update.tipo_doc = documento.tipo_doc
#             if documento.tipo_destino:
#                 documento_update.tipo_destino = documento.tipo_destino
#             if usuario_logado.id_user != documento_update.criador_id:
#                 documento_update.usuario_id = usuario_logado.id_user

#             await session.commit()

#             return documento_update
#         else:
#             raise HTTPException(detail='Documento não encontrado',
#                                 status_code=status.HTTP_404_NOT_FOUND)


# DELETE Documento
@router.delete('/{documento_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_documento(documento_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(DocumentosModel).filter(DocumentosModel.id_doc == documento_id).filter(
            DocumentosModel.criador_id == usuario_logado.id_user)
        result = await session.execute(query)
        documento_del: DocumentosModel = result.scalars().unique().one_or_none()

        if documento_del:
            await session.delete(documento_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Documento não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
