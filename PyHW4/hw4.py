# получаем данные от пользователя
def get_initial_conditions():
    while True:
        try:
            num_pegs = int(input("Введите количество стержней (не менее 3): "))
            if num_pegs < 3:
                raise ValueError("Количество стержней должно быть не менее 3.")
            num_disks = int(input("Введите количество дисков (не менее 1): "))
            if num_disks < 1:
                raise ValueError("Количество дисков должно быть не менее 1.")
            return num_pegs, num_disks
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")


# алгоритм решения
def solve_hanoi(num_disks, from_peg, to_peg, aux_pegs, move_list):
    if num_disks == 1:
        # перемещаем один диск
        move_list.append((num_disks, from_peg, to_peg))
    else:
        # используем вспомогательный стержень
        aux_peg = aux_pegs[0]
        remaining_aux_pegs = aux_pegs[1:]
        solve_hanoi(num_disks - 1, from_peg, aux_peg, remaining_aux_pegs + [to_peg], move_list)
        move_list.append((num_disks, from_peg, to_peg))
        solve_hanoi(num_disks - 1, aux_peg, to_peg, remaining_aux_pegs + [from_peg], move_list)


# отображение действий
def display_solution(move_list):
    for move in move_list:
        disk, from_peg, to_peg = move
        print(f"Блин {disk}: Стержень {from_peg} -> Стержень {to_peg}.")


# запись действий в файл
def write_solution_to_file(move_list):
    with open("решение.txt", "w", encoding="utf-8") as file:
        for move in move_list:
            disk, from_peg, to_peg = move
            file.write(f"Блин {disk}: Стержень {from_peg} -> Стержень {to_peg}.\n")
    print("Решение записано в файл 'решение.txt'.")


# основная функция программы
def main():
    # ввод условий
    num_pegs, num_disks = get_initial_conditions()

    # размещаем диски на первый стержень
    pegs = {i: [] for i in range(1, num_pegs + 1)}
    pegs[1] = list(range(num_disks, 0, -1))

    # список для хранения шагов перемещения
    move_list = []

    # определяем целевой стержень (по умолчанию последний)
    to_peg = num_pegs

    # вспомогательные стержни
    aux_pegs = list(range(2, num_pegs))

    # решение задачи
    solve_hanoi(num_disks, 1, to_peg, aux_pegs, move_list)

    # ввод решения на экран
    display_solution(move_list)

    # запись решения в файл
    write_solution_to_file(move_list)


# запуск программы
if __name__ == "__main__":
    main()
