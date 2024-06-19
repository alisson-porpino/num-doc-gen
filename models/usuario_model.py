from sqlalchemy import Integer, String, Column, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

from core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__: str = 'usuarios'

    id: str = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    username: str = Column(String(40), unique=True, nullable=False)
    email: str = Column(String(120), unique=True, nullable=False)
    senha: str = Column(String(255), nullable=False)
    date_created: str = Column(String, default=datetime.now, nullable=False)
    last_update: str = Column(String, default=datetime.now, onupdate=datetime.now, nullable=True)
    #recovery_code: str = Column(String(200), nullable=True)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship(
        "ArtigoModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
