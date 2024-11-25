import pytest
from invoice import calcularInvoice, InvalidProductException

def test_sem_desconto():
    prod = [
        {"name": "Gaita de boca", "price": 100.0, "quantity": 2},
    ]
    desc = 0
    assert calcularInvoice(prod, desc) == 200.0

def test_com_desconto_normal():
    prod = [
        {"name": "Gaita de boca", "price": 100.0, "quantity": 2},
    ]
    desc = 10
    assert calcularInvoice(prod, desc) == 180.0

def test_price_maior_que_mil():
    prod = [
        {"name": "violino", "price": 600.0, "quantity": 1},
        {"name": "violão meio capenga", "price": 200.0, "quantity": 1},
        {"name": "cajon", "price": 500.0, "quantity": 1}
    ]
    desc = 10
    assert calcularInvoice(prod, desc) == 1070.0

def test_price_negativo():
    prod = [
        {"name": "Piano quebrado", "price": -100.0, "quantity": 2},
        {"name": "Flauta doce", "price": 50.0, "quantity": 4},
    ]
    desc = 10
    with pytest.raises(InvalidProductException):
        calcularInvoice(prod, desc)

def test_quantity_negativo():
    prod = [
        {"name": "Piano de brinquedo", "price": 100.0, "quantity": 2},
        {"name": "Flauta doce", "price": 50.0, "quantity": -4},
    ]
    desc = 10
    with pytest.raises(InvalidProductException):
        calcularInvoice(prod, desc)