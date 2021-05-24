def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    price_with_discount = price - price * discount/ 100
    if discount >= price:
        price_with_discount = price
    return price_with_discount

