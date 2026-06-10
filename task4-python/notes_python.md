# Конспект по изучению Python

## Модуль 1: Основы Python

### Переменные и типы данных
```python
name = "Виктория"     # str (строка)
age = 20              # int (целое число)
height = 1.75         # float (дробное)
is_student = True     # bool (логический)
Операторы
Арифметические:
+ сложение
- вычитание
* умножение
/ деление
// целочисленное деление
% остаток от деления
** возведение в степень
Сравнения:
== равно
!= не равно
> больше
< меньше
>= больше или равно
<= меньше или равно
Логические:
and — И
or — ИЛИ
not — НЕ
Ввод/вывод
print("Привет!")           # Вывод
name = input("Имя: ")      # Ввод

## Модуль 2: Управляющие конструкции
"""
Мини-проект: Калькулятор рентабельности
Автор: Калачева Виктория
Дата: 10.06.2026
Описание: Программа вычисляет прибыль и рентабельность продаж компании,
          выводит структурированный отчёт с качественной оценкой.
"""


def calculate_profit(revenue, costs):
    """
    Вычисляет прибыль компании.
    
    Args:
        revenue (float): Выручка
        costs (float): Затраты
    
    Returns:
        float: Прибыль
    """
    return revenue - costs


def calculate_profitability(profit, revenue):
    """
    Вычисляет рентабельность продаж в процентах.
    
    Args:
        profit (float): Прибыль
        revenue (float): Выручка
    
    Returns:
        float: Рентабельность в процентах
    """
    if revenue == 0:
        return 0
    return (profit / revenue) * 100


def get_profitability_level(profitability):
    """
    Определяет уровень рентабельности.
    
    Args:
        profitability (float): Рентабельность в процентах
    
    Returns:
        str: Уровень рентабельности
    """
    if profitability > 20:
        return "высокая рентабельность"
    elif profitability >= 10:
        return "средняя рентабельность"
    else:
        return "низкая рентабельность"


def main():
    """Главная функция программы"""
    print("=== Калькулятор рентабельности ===\n")
    
    # Ввод данных
    company_name = input("Введите наименование компании: ")
    revenue = float(input("Введите выручку (руб.): ").replace(',', '.'))
    costs = float(input("Введите затраты (руб.): ").replace(',', '.'))
    
    # Вычисления
    profit = calculate_profit(revenue, costs)
    profitability = calculate_profitability(profit, revenue)
    level = get_profitability_level(profitability)
    
    # Вывод отчёта
    print("\n" + "=" * 40)
    print(f"Отчёт по компании: {company_name}")
    print("=" * 40)
    print(f"Выручка:          {revenue:>12.2f} руб.")
    print(f"Затраты:          {costs:>12.2f} руб.")
    print(f"Прибыль:          {profit:>12.2f} руб.")
    print(f"Рентабельность:   {profitability:>11.2f} %")
    print(f"Оценка:           {level}")
    print("=" * 40)


if __name__ == "__main__":
    main()
elif age >= 14:
    print("Подросток")
else:
    print("Ребенок")
### Цикл for
for i in range(5):
    print(i)
### Цикл while
count = 0
while count < 5:
    print(count)
    count += 1 

## Модуль 3: Функции и структуры данных

### Функции
def greet(name):
    return f"Привет, {name}!"
### Списки (list)
fruits = ["яблоко", "банан"]
fruits.append("груша")
### Словари (dict)
user = {"name": "Виктория", "age": 20}
### Обработка исключений
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Деление на ноль!")
