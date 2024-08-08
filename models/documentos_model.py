from sqlalchemy import Integer, String, Column, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from core.configs import settings


class DocumentosModel(settings.DBBaseModel):
    __tablename__: str = 'documentos'

    id_doc: str = Column(Integer, primary_key=True, autoincrement=True)
    num_reg: str = Column(String(100), unique=False, nullable=False)
    objeto: str = Column(String(100), unique=False, nullable=False)
    origem: str = Column(String(100), unique=False, nullable=False)
    tipo_doc: str = Column(String(120), nullable=False)
    tipo_destino: str = Column(String(255), nullable=False) # Interno, Externo, etc.
    destino: str = Column(String(255), nullable=True)
    date_created: str = Column(DateTime, default=datetime.now, nullable=False)
    last_update: str = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    criador_id: int = Column(Integer, ForeignKey('usuarios.id_user'))
    
    criador: str = relationship("UsuarioModel", back_populates='documentos', lazy='joined')

    __allow_unmapped__ = True

