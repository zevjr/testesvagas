from flask import url_for
from unittest.mock import patch
from .mocks import MockCart

mock_cart = MockCart()


@patch("flask_sqlalchemy._QueryProperty.__get__")
@patch("src.models.cart.db.session.add")
@patch("src.models.cart.db.session.commit")
def test_card_creation(mock_commit, mock_add, mock_get, client):
    mock_get.return_value.filter_by.return_value.first.return_value = (
        mock_cart.cart_user
    )
    mock_get.return_value.get_or_404.return_value = mock_cart.cart_product
    response = client.post(url_for("cart.post_cart"), json=mock_cart.create_cart)
    assert response.status_code == 201
    assert response.json == {"message": "Cart created"}
    mock_add.assert_called()
    mock_commit.assert_called_once()



@patch("flask_sqlalchemy._QueryProperty.__get__")
def test_card_creation_error_above_amount_per_package_406(mock_get, client):
    mock_get.return_value.filter_by.return_value.first.return_value = (
        mock_cart.cart_user
    )
    mock_get.return_value.get_or_404.return_value = mock_cart.cart_product
    response = client.post(url_for("cart.post_cart"), json=mock_cart.create_cart_error)
    assert response.status_code == 406


@patch("flask_sqlalchemy._QueryProperty.__get__")
def test_get_data_cart(mock_get, client):
    mock_get.return_value.filter_by.return_value.first_or_404.return_value = mock_cart.cart_user
    mock_get.return_value.filter_by.return_value.all.return_value = mock_cart.cart_items
    mock_get.return_value.getattr.return_value.product.return_value = mock_cart.cart_product
    response = client.get(url_for("cart.get_cart", username="test"))
    assert response.status_code == 200
    assert response.json == mock_cart.cart_item_response


@patch("flask_sqlalchemy._QueryProperty.__get__")
@patch("src.models.cart.db.session.commit")
def test_update_data_cart(mock_commit, mock_get, client):
    mock_get.return_value.get.return_value = mock_cart.cart_item
    response = client.put(url_for("cart.put_cart"), json=mock_cart.cart_update)
    assert response.status_code == 200
    assert response.json == {"message": "Cart updated"}
    mock_commit.assert_called_once()



@patch("flask_sqlalchemy._QueryProperty.__get__")
@patch("src.models.cart.db.session.delete")
@patch("src.models.cart.db.session.commit")
def test_delete_data_cart(mock_commit, mock_delete, mock_get, client):
    mock_get.return_value.get.return_value = mock_cart.cart_item
    response = client.delete(url_for("cart.del_cart"), json=mock_cart.cart_delete)
    assert response.status_code == 200
    assert response.json == {"message": "Cart deleted"}
    mock_delete.assert_called()
    mock_commit.assert_called_once()
