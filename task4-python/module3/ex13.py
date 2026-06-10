# Задание 3: Функция get_business_category()

def get_business_category(annual_revenue):
    """
    Определяет категорию бизнеса по годовой выручке.

    Args:
        annual_revenue (float): Годовая выручка

    Returns:
        str: Категория бизнеса
    """
    if annual_revenue <= 1_000_000:
        return "Микробизнес"
    elif annual_revenue <= 10_000_000:
        return "Малый бизнес"
    elif annual_revenue <= 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"


# Тестирование на четырёх значениях
print("Классификация предприятий:")
print("-" * 40)

revenues = [500000, 5000000, 50000000, 500000000]

for revenue in revenues:
    category = get_business_category(revenue)
    print(f"Выручка: {revenue:>12} руб. → {category}")