import time
from concurrent.futures import ThreadPoolExecutor


# Определяем формулы
def formula_1(x):
    return x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x


def formula_2(x):
    return x + x


def compute(iterations):
    start_time = time.time()

    # Параллельные вычисления для формул 1 и 2
    with ThreadPoolExecutor() as executor:
        results_1 = list(executor.map(formula_1, range(iterations)))
        time_formula_1 = time.time() - start_time

        start_time = time.time()
        results_2 = list(executor.map(formula_2, range(iterations)))
        time_formula_2 = time.time() - start_time

        # Вычисление результата формулы 3
        start_time = time.time()
        total_result = sum(results_1) + sum(results_2)
        time_formula_3 = time.time() - start_time

    # Вывод результатов
    print(f"Iterations: {iterations}")
    print(f"Time for formula 1: {time_formula_1:.4f} seconds")
    print(f"Time for formula 2: {time_formula_2:.4f} seconds")
    print(f"Time for formula 3: {time_formula_3:.4f} seconds")
    print(f"Total result: {total_result}\n")


# Выполнение вычислений для 10,000 и 100,000 итераций
compute(10000)
compute(100000)

