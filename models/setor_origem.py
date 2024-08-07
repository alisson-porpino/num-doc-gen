from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from core.configs import settings


class SetorModel(settings.DBBaseModel):
    __tablename__: str = 'setor_origem'

    id: str = Column(Integer, primary_key=True)
    nome: str = Column(String(100), unique=True, nullable=False)
    descricao: str = Column(String(120), nullable=True)

    __allow_unmapped__ = True


    def __repr__(self):
	    return self.name
