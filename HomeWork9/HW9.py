import re


def validate_car_id(car_id):
    # Регулярное выражение для проверки формата номерного знака
    pattern = r'^[АВЕКМНОРСТУХ]{1}d{3}[АВЕКМНОРСТУХ]{2}d{2,3}$'

    if re.match(pattern, car_id):
        # Если номер валиден, извлекаем номер и регион
        number = car_id[:-2]  # Все символы кроме последних двух
        region = car_id[-2:]  # Последние два символа (регион)
        return f"Номер {number} валиден. Регион: {region}."
    else:
        return "Номер не валиден."


# Примеры использования
car_id_1 = 'А222BС96'
print(validate_car_id(car_id_1))  # Номер А222BС валиден. Регион: 96.

car_id_2 = 'АБ22ВВ193'
print(validate_car_id(car_id_2))  # Номер не валиден.
