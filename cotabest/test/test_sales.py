from flask import url_for
from unittest.mock import patch
from .mocks import MockSales, MockCart

mock_sales = MockSales()
mock_cart = MockCart()


@patch("flask_sqlalchemy._QueryProperty.__get__")
@patch("src.models.cart.db.session.delete")
@patch("src.models.cart.db.session.commit")
def test_create_sales_order(mock_commit, mock_delete, mock_get, client):
    mock_get.return_value.filter_by.return_value.first_or_404.return_value = mock_cart.cart_user
    mock_get.return_value.filter_by.return_value.all.return_value = mock_cart.cart_items

    response = client.post(url_for("sales_order.create_sales"), json=mock_sales.create_sales)
    assert response.status_code == 201
    mock_delete.assert_called()
    mock_commit.assert_called_once()



@patch("flask_sqlalchemy._QueryProperty.__get__")
def test_create_sales_order_with_amount_below_minimun(mock_get, client):
    mock_get.return_value.filter_by.return_value.first_or_404.return_value = mock_cart.cart_user
    mock_get.return_value.filter_by.return_value.all.return_value = mock_cart.cart_items_error_minimun

    response = client.post(url_for("sales_order.create_sales"), json=mock_sales.create_sales)
    assert response.status_code == 406



@patch("flask_sqlalchemy._QueryProperty.__get__")
def test_create_sales_order_with_amount_above_max_availability(mock_get, client):
    mock_get.return_value.filter_by.return_value.first_or_404.return_value = mock_cart.cart_user
    mock_get.return_value.filter_by.return_value.all.return_value = mock_cart.cart_items_error_max_availability

    response = client.post(url_for("sales_order.create_sales"), json=mock_sales.create_sales)
    assert response.status_code == 406
