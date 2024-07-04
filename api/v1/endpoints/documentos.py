from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.documentos_model import DocumentosModel
from models.usuarios_model import UsuarioModel
from schemas.documentos_schema import DocumentosSchema
from core.deps import get_session, get_current_user


router = APIRouter()


# POST Documentos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=DocumentosSchema)
async def post_documento(documento: DocumentosSchema, usuario_logado:UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    novo_documento: DocumentosModel = DocumentosModel(
        num_reg=documento.num_reg, nome_doc=documento.nome_doc, tipo_doc=documento.tipo_doc, descricao=documento.descricao, setor_origem=documento.setor_origem, criador_id=usuario_logado.id_user)

    db.add(novo_documento)
    await db.commit()

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


# PUT Documento
@router.put('/{documento_id}', response_model=DocumentosSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_documento(documento_id: int, documento: DocumentosSchema, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(DocumentosModel).filter(DocumentosModel.id_doc == documento_id)
        result = await session.execute(query)
        documento_update: DocumentosModel = result.scalars().unique().one_or_none()

        if documento_update:
            if documento.num_reg:
                documento_update.num_reg = documento.num_reg
            if documento.nome_doc:
                documento_update.nome_doc = documento.nome_doc
            if documento.tipo_doc:
                documento_update.tipo_doc = documento.tipo_doc
            if documento.descricao:
                documento_update.descricao = documento.descricao
            if documento.setor_origem:
                documento_update.setor_origem = documento.setor_origem
            if usuario_logado.id_user != documento_update.criador_id:
                documento_update.usuario_id = usuario_logado.id_user

            await session.commit()

            return documento_update
        else:
            raise HTTPException(detail='Documento não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


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
