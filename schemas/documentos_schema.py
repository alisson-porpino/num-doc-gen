from typing import Optional

from pydantic import BaseModel


class DocumentosSchema(BaseModel):
    id: Optional[int] = None
    num_reg: str
    objeto: str
    tipo_doc: str
    descricao: str
    # date_created: Optional[int] = None
    setor_origem: str
    # requester: Optional[str] = None
    criador_id: Optional[int]

    class Config:
        from_attributes = True

class DocumentosCreateSchema(BaseModel):
    objeto: str
    tipo_doc: str
    descricao: str
    setor_origem: str
    criador_id: int

    class Config:
        from_attributes = True