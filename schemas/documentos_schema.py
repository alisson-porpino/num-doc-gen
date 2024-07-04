from typing import Optional

from pydantic import BaseModel


class DocumentosSchema(BaseModel):
    id: Optional[int] = None
    num_reg: int
    nome_doc: str
    tipo_doc: str
    descricao: str
    # date_created: Optional[int] = None
    setor_origem: Optional[str] = None
    # requester: Optional[str] = None
    criador_id: Optional[int]

    class Config:
        from_attributes = True
