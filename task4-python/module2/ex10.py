# Задание 5: Анализ ценового диапазона

# Задание списка из пяти цен товаров
prices = [150.50, 280.00, 95.75, 420.30, 175.25]

# Вычисление средней цены
average_price = sum(prices) / len(prices)

# Вывод заголовка
print(f"Анализ ценового диапазона (средняя цена: {average_price:.2f} руб.):")
print("-" * 50)

# Цикл for для вывода каждой цены с пометкой
for price in prices:
    if price > average_price:
        print(f"{price:.2f} руб. — ВЫШЕ СРЕДНЕГО")
    else:
        print(f"{price:.2f} руб.")