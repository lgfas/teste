# test_product_manager.py

import pytest
from unittest.mock import MagicMock
from db_manager import ProductManager
from models import Produto


class TestProductManager:
    # Test for add product
    def test_insert_product_with_existing_name(self):
        session_mock = create_autospec(Session)
        product_db = ProductManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        product_db.session = session_mock

        session_mock.query.return_value.filter_by.return_value.first.return_value = Produto()

        produto_sample = Produto(nome="Produto Teste", descricao="Descricao Teste", valor=10.5, quantidade=5)
        
        with pytest.raises(ValueError, match='Produto já cadastrado'):
            product_db.insert_product(produto_sample)

    # Test for list products
    def test_list_products_with_no_products(self):
        session_mock = create_autospec(Session)
        product_db = ProductManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        product_db.session = session_mock

        session_mock.query.return_value.all.return_value = []  # No products in database
        
        with pytest.raises(ValueError, match='Nenhum produto encontrado'):
            product_db.list_products()

    # Test for update product
    def test_update_product_with_non_existing_name(self):
        session_mock = create_autospec(Session)
        product_db = ProductManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        product_db.session = session_mock

        session_mock.query.return_value.filter_by.return_value.first.return_value = None

        produto_sample = Produto(nome="Produto Teste", descricao="Descricao Teste", valor=10.5, quantidade=5)
        
        with pytest.raises(ValueError, match='Produto não encontrado'):
            product_db.update_product(produto_sample)

    # Test for delete product
    def test_delete_product_with_non_existing_name(self):
        session_mock = create_autospec(Session)
        product_db = ProductManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        product_db.session = session_mock

        session_mock.query.return_value.filter_by.return_value.first.return_value = None
        
        with pytest.raises(ValueError, match='Produto não encontrado'):
            product_db.delete_product("Produto Teste")
