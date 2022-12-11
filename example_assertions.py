def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'],("Price after applying discount is equal or less than zero,\nor greater or equal to product's price.")
    return price

def apply_discount_data_validation(product, discount):
    price = int(product['price'] * (1.0 - discount))
    if not (price > 0):
        raise ValueError("Price after applying discount is {0},\nWhich is equal or less than zero.".format(price))
    if not (price <= product['price']):
        raise ValueError("Price after applying discount is {0},\nWhich is greater than the price of product.".format(price))
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(shoes, 0.25))
print(apply_discount_data_validation(shoes, -1.0))

