# models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = "tb_Produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)

class Categoria(Base):
    __tablename__ = "tb_Categoria"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
