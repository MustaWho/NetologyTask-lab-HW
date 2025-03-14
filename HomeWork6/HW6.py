import csv

# Словарь с категориями покупок
purchase_categories = {
    '1840e0b9d4': 'Продукты',
    '4e4f90fcfb': 'Электроника',
    # Добавьте другие user_id и соответствующие категории
}

# Открываем файл visit_log.csv для чтения и funnel.csv для записи
with open('visit_log.csv', 'r', encoding='utf-8') as visit_file:
    with open('funnel.csv', 'w', newline='', encoding='utf-8') as funnel_file:
        # Создаем объект csv.reader для чтения visit_log
        visit_reader = csv.reader(visit_file)

        # Создаем объект csv.writer для записи в funnel.csv
        funnel_writer = csv.writer(funnel_file)

        # Записываем заголовок в funnel.csv
        funnel_writer.writerow(['user_id', 'source', 'category'])

        # Пропускаем заголовок visit_log.csv
        next(visit_reader)

        # Обрабатываем каждую строку из visit_log.csv
        for row in visit_reader:
            user_id, source = row[0], row[1]

            # Проверяем, есть ли категория для данного user_id
            if user_id in purchase_categories:
                category = purchase_categories[user_id]
                # Записываем строку в funnel.csv
                funnel_writer.writerow([user_id, source, category])

print("Файл funnel.csv успешно создан.")

