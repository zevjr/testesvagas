from flask import url_for
from unittest.mock import patch
from .mocks import MockProduct

mock_product = MockProduct()

@patch('flask_sqlalchemy._QueryProperty.__get__')
def test_searching_for_items_in_the_database_by_a_word(mock_get, client):
    mock_get.return_value.filter.return_value.all.return_value = mock_product.list_product
    response = client.get(url_for('product.get_search_products', name='jão'))
    assert response.status_code == 200

@patch('flask_sqlalchemy._QueryProperty.__get__')
def test_not_fount_item_product(mock_get, client):
    mock_get.return_value.filter.return_value.all.return_value = []
    response = client.get(url_for('product.get_search_products', name='test'))
    assert response.status_code == 404


@patch('src.models.product.db.session.add')
@patch('src.models.product.db.session.commit')
def test_product_creation(mock_commit, mock_add, client):
    response = client.post(url_for('product.post_product'), json=mock_product.create_product)
    assert response.status_code == 201
    assert response.json == {"message": "Product created"}
    mock_add.assert_called()
    mock_commit.assert_called_once()
