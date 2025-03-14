def min_breaks(n, m, memo=None):
    # Инициализация мемоизации
    if memo is None:
        memo = {}

    # Если шоколадка уже 1x1, разломов не требуется
    if n == 1 and m == 1:
        return 0

    # Проверка на наличие результата в кэше
    if (n, m) in memo:
        return memo[(n, m)]

    # Минимальное количество разломов
    breaks = float('inf')

    # Разделение по вертикали
    for i in range(1, n):
        breaks = min(breaks, min_breaks(i, m, memo) + min_breaks(n - i, m, memo) + 1)

    # Разделение по горизонтали
    for j in range(1, m):
        breaks = min(breaks, min_breaks(n, j, memo) + min_breaks(n, m - j, memo) + 1)

    # Сохраняем результат в кэше
    memo[(n, m)] = breaks
    return breaks


# Тестирование функции
print(min_breaks(2, 3))  # Должно вывести 5
print(min_breaks(3, 3))  # Должно вывести 8
print(min_breaks(1, 1))  # Должно вывести 0
