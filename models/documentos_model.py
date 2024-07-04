from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from core.configs import settings


class DocumentosModel(settings.DBBaseModel):
    __tablename__: str = 'documentos'

    id_doc: str = Column(Integer, primary_key=True, autoincrement=True)
    num_reg: str = Column(String(100), unique=True, nullable=False)
    nome_doc: str = Column(String(120), nullable=False)
    # Vai existir uma lista suspensa
    tipo_doc: str = Column(String(120), nullable=False)
    descricao: str = Column(String(120), nullable=False)
    setor_origem: str = Column(String(255), nullable=False)
    # requester: str = Column(String, default=datetime.now, onupdate=datetime.now, nullable=True)
    # destino: str = Column(String(255), nullable=False)
    date_created: str = Column(String, default=datetime.now, nullable=False)
    last_update: str = Column(String, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    criador_id: int = Column(Integer, ForeignKey('usuarios.id_user'))

    criador: str = relationship("UsuarioModel", back_populates='documentos', lazy='joined')

    __allow_unmapped__ = True

