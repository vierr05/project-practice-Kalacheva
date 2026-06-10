# Задание 1: Функция calculate_profit()

def calculate_profit(revenue, costs):
    """
    Вычисляет прибыль предприятия.

    Args:
        revenue (float): Выручка
        costs (float): Затраты

    Returns:
        float: Прибыль
    """
    return revenue - costs


# Вызов функции с тремя различными наборами данных
print("Расчёт прибыли:")
print("-" * 30)

profit1 = calculate_profit(100000, 75000)
print(f"Набор 1: Прибыль = {profit1:.2f} руб.")

profit2 = calculate_profit(250000, 280000)
print(f"Набор 2: Прибыль = {profit2:.2f} руб.")

profit3 = calculate_profit(500000, 350000)
print(f"Набор 3: Прибыль = {profit3:.2f} руб.")