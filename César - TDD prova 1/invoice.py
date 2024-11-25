class InvalidProductException(Exception):
    pass

def calcularInvoice(prod, desc):
    for p in prod:
        if p["price"] < 0 or p["quantity"] < 0:
            raise InvalidProductException("Produto inválido! Preço ou quantidade negativos.")

    total = sum(p["price"] * p["quantity"] for p in prod)

    totalComDesconto = total * (1 - desc / 100)

    if total > 1000.0:
        totalComDesconto -= 100.0

    return totalComDesconto
