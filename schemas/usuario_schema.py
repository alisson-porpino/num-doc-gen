from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.documentos_schema import DocumentosSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    username: str
    email: EmailStr
    eh_admin: bool = False
    #date_created: Optional[str] = None
    #last_update: Optional[str] = None
    #recovery_code: Optional[str] = None

    class Config:
        from_attributes = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaDocumentos(UsuarioSchemaBase):
    documentos: Optional[List[DocumentosSchema]]


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    username: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]
