import math

def pi_digits_generator(n_digits):
    """Генератор цифр числа π"""
    # Получаем строковое представление π без точки
    pi_str = str(math.pi).replace('.', '')
    
    # Генерируем цифры по одной
    for i in range(min(n_digits, len(pi_str))):
        digit = int(pi_str[i])
        yield digit

def main():
    # Количество цифр для обработки (ограничиваем для наглядности)
    n_digits = 10
    
    # Создаем генератор цифр π
    digits_gen = pi_digits_generator(n_digits)
    
    # Применяем map: каждая цифра делится на её квадрат (digit / digit²)
    # Для цифры 0 пропускаем операцию (деление на 0)
    processed_values = map(
        lambda d: d / (d ** 2) if d != 0 else 0,
        digits_gen
    )
    
    # Вычисляем сумму
    result = sum(processed_values)
    
    # Выводим результаты
    print("Цифры числа π (первые", n_digits, "цифр):")
    pi_digits = str(math.pi).replace('.', '')[:n_digits]
    print(" ".join(pi_digits))
    
    print(f"\nРезультат вычисления суммы (digit / digit²):")
    print(f"Сумма = {result:.6f}")

if __name__ == "__main__":
    main()