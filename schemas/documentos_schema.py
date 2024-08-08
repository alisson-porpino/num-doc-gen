from typing import Optional

from pydantic import BaseModel


class DocumentosSchema(BaseModel):
    id: Optional[int] = None
    num_reg: str
    objeto: str
    origem: str
    tipo_doc: str
    # date_created: Optional[int] = None
    tipo_destino: str
    # requester: Optional[str] = None
    criador_id: Optional[int]

    class Config:
        from_attributes = True

class DocumentosCreateSchema(BaseModel):
    objeto: str
    origem: str
    tipo_doc: str
    tipo_destino: str
    criador_id: int

    class Config:
        from_attributes = True