import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def parse_data(data):
    descriptions = []
    for index, row in data.iterrows():
        name = row['name']
        gender = row['sex']
        age = row['age']
        device = row['device_type']
        browser = row['browser']
        amount = row['bill']
        region = row['region']

        # Формирование текстового описания
        description = (f"Пользователь {name} {gender} пола, {age} лет "
                       f"совершила покупку на {amount} у.е. с мобильного браузера {browser}. "
                       f"Регион, из которого совершалась покупка: {region}.")

        descriptions.append(description)

    return descriptions


def write_to_file(descriptions, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for desc in descriptions:
            f.write(desc + '\n')


def main(input_file, output_file):
    data = load_data(input_file)
    descriptions = parse_data(data)
    write_to_file(descriptions, output_file)
    print(f"Описание покупателей записано в файл: {output_file}")


input_file = 'web_clients_correct.csv'
output_file = 'customer_descriptions.txt'

main(input_file, output_file)
