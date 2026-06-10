# Задание 2: Функция calculate_vat()

def calculate_vat(price, vat_rate=20):
    """
    Вычисляет сумму НДС.

    Args:
        price (float): Цена товара
        vat_rate (float): Ставка НДС в процентах (по умолчанию 20)

    Returns:
        float: Сумма налога
    """
    return price * vat_rate / 100


# Вызов функции с явно заданной ставкой
vat1 = calculate_vat(1000, 10)
print(f"Цена: 1000 руб., НДС 10%: {vat1:.2f} руб.")

# Вызов функции со значением по умолчанию
vat2 = calculate_vat(1000)
print(f"Цена: 1000 руб., НДС 20% (по умолчанию): {vat2:.2f} руб.")

vat3 = calculate_vat(2500, 20)
print(f"Цена: 2500 руб., НДС 20%: {vat3:.2f} руб.")