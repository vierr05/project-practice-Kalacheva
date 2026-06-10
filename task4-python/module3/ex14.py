# Задание 4: Функция compound_interest()

def compound_interest(capital, rate, years):
    """
    Вычисляет итоговую сумму по формуле сложного процента.

    Args:
        capital (float): Начальный капитал
        rate (float): Процентная ставка
        years (int): Срок в годах

    Returns:
        float: Итоговая сумма
    """
    return capital * (1 + rate / 100) ** years


# Вызов для сроков 3, 5 и 10 лет
capital = 100000
rate = 10

print(f"Начальный капитал: {capital} руб.")
print(f"Процентная ставка: {rate}%")
print("-" * 40)

for years in [3, 5, 10]:
    final_amount = compound_interest(capital, rate, years)
    print(f"Срок {years} года(лет): {final_amount:.2f} руб.")