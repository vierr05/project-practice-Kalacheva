# Задание 5: Функция apply_discount()

def apply_discount(price, discount_percent):
    """
    Применяет скидку к цене товара.

    Args:
        price (float): Цена товара
        discount_percent (float): Размер скидки в процентах

    Returns:
        float: Цена после применения скидки
    """
    discount_amount = price * discount_percent / 100
    return price - discount_amount


# Список из пяти товаров
products = [
    ("Товар 1", 1000),
    ("Товар 2", 2500),
    ("Товар 3", 750),
    ("Товар 4", 3200),
    ("Товар 5", 1500)
]

discount = 15  # 15% скидка

print(f"Применение скидки {discount}%:")
print("-" * 50)
print(f"{'Товар':<15} {'Исходная':<12} {'Со скидкой':<12}")
print("-" * 50)

# Применение функции в цикле for
for name, price in products:
    discounted_price = apply_discount(price, discount)
    print(f"{name:<15} {price:<12.2f} {discounted_price:<12.2f}")
