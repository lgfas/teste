# test_category_manager.py

import pytest
from unittest.mock import MagicMock
from db_manager import CategoryManager
from models import Categoria


class TestCategoryManager:
    # Test for add category
    def test_insert_category_with_existing_name(self):
        session_mock = create_autospec(Session)
        category_db = CategoryManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        category_db.session = session_mock

        session_mock.query.return_value.filter_by.return_value.first.return_value = Categoria()

        categoria_sample = Categoria(nome="Categoria Teste", descricao="Descricao Teste")
        
        with pytest.raises(ValueError, match='Categoria já cadastrada'):
            category_db.insert_category(categoria_sample)

    # Test for list categories
    def test_list_categories_with_no_categories(self):
        session_mock = create_autospec(Session)
        category_db = CategoryManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        category_db.session = session_mock

        session_mock.query.return_value.all.return_value = []  # No categories in database
        
        with pytest.raises(ValueError, match='Nenhuma categoria encontrada'):
            category_db.list_categories()

    # Test for update category
    def test_update_category_with_non_existing_name(self):
        session_mock = create_autospec(Session)
        category_db = CategoryManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        category_db.session = session_mock

        session_mock.query.return_value.filter_by.return_value.first.return_value = None

        categoria_sample = Categoria(nome="Categoria Teste", descricao="Descricao Teste")
        
        with pytest.raises(ValueError, match='Categoria não encontrada'):
            category_db.update_category(categoria_sample)

    # Test for delete category
    def test_delete_category_with_non_existing_name(self):
        session_mock = create_autospec(Session)
        category_db = CategoryManager('mysql+mysqlconnector://user:password@localhost/db_produto')
        category_db.session = session_mock

        session_mock.query.return_value.filter_by.return_value.first.return_value = None
        
        with pytest.raises(ValueError, match='Categoria não encontrada'):
            category_db.delete_category("Categoria Teste")
