from sqlalchemy import Integer, String, Column, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

from core.configs import settings


class DocumentosModel(settings.DBBaseModel):
    __tablename__: str = 'documents'

    id: str = Column(Integer, primary_key=True, autoincrement=True)
    num_reg: str = Column(String(100), unique=True, nullable=False)
    nome_doc: str = Column(String(120), unique=True, nullable=False)
    #objeto: str = Column(String(120), unique=True, nullable=False)
    date_created: str = Column(String, default=datetime.now, nullable=False)
    last_update: str = Column(String, default=datetime.now, onupdate=datetime.now, nullable=True)
    #requester: str = Column(String, default=datetime.now, onupdate=datetime.now, nullable=True)
    #criador: str = relationship("UsuarioModel", back_populates='artigos', lazy='joined')
    tipo: str = Column(String(255), nullable=False)
    setor_origem: str = Column(String(255), nullable=False)
    #destino: str = Column(String(255), nullable=False)
