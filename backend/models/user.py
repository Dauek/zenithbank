from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

# Tabela de usuarios do banco
# Toda classe que representa uma tabela tem que herdar de Base
class User(Base):
    __tablename__ = "users"  # nome da tabela no banco

    # id único de cada usuário, gerado automaticamente
    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    # preenchido automaticamente pelo banco na hora que o usuario é criado
    created_at = Column(DateTime(timezone=True), server_default=func.now())