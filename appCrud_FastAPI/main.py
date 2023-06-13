# db_manager.py
from connection import Connection
from models import Produto, Categoria

class ProductManager:
    # Inicializa uma nova instância da classe ProductManager, conectando ao banco de dados
    def __init__(self, db_url):
        self.connection = Connection(db_url)

    def add_product(self, product):
        session = self.connection.get_session()
        session.add(product)
        session.commit()

    def get_product(self, product_id):
        session = self.connection.get_session()
        return session.query(Produto).filter(Produto.id == product_id).first()

    def update_product(self, product):
        session = self.connection.get_session()
        session.update(product)
        session.commit()

    def delete_product(self, product_id):
        session = self.connection.get_session()
        product = session.query(Produto).filter(Produto.id == product_id).first()
        session.delete(product)
        session.commit()

class CategoryManager:
    # Inicializa uma nova instância da classe CategoryManager, conectando ao banco de dados
    def __init__(self, db_url):
        self.connection = Connection(db_url)

    def add_category(self, category):
        session = self.connection.get_session()
        session.add(category)
        session.commit()

    def get_category(self, category_id):
        session = self.connection.get_session()
        return session.query(Categoria).filter(Categoria.id == category_id).first()

    def update_category(self, category):
        session = self.connection.get_session()
        session.update(category)
        session.commit()

    def delete_category(self, category_id):
        session = self.connection.get_session()
        category = session.query(Categoria).filter(Categoria.id == category_id).first()
        session.delete(category)
        session.commit()
