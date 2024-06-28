from typing import Optional

from pydantic import BaseModel


class DocumentosSchema(BaseModel):
    id: Optional[int] = None
    nome_doc: str
    tipo: Optional[str]
    origem: Optional[str]

    class Config:
        orm_mode = True
