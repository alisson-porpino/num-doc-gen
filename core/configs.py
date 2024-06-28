from typing import List

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações Gerais Usadas na Aplicação.
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'sqlite+aiosqlite:///./teste.db/'
    #DB_URL: str = 'postgresql+asyncpg://postgres:1212@localhost:5432/postgres'
    DBBaseModel: DeclarativeMeta = declarative_base()

    #JWT_SECRET: str = 'ixJcMwpQ8MJRgF6cXofC8lKo4a2t0LdRUbkNcQTV2PA'
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    token
    """
    #ALGORITHM: str ='HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    #ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


    class config:
        case_sensitive = True




settings: Settings = Settings()
