# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
print(contacts_list)

phonebook = []
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
for i in contacts_list:
    # Собираем ФИО в 3 отдельных поля
    fio = " ".join(i[:3])
    contact = fio.split(" ")[:3]
    # Добавляем организацию и должность как ест
    contact = contact + i[3:5]
    # Разбираем и преобразуем телефон
    phone_pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(?:\s*\(?(доб\.)\s*(\d{4})\)?)?"
    # Шаблон для замены: +7(код)цифры-цифры-цифры
    replacement_pattern = r"+7(\2)\3-\4-\5\6\7"
    contact.append(re.sub(phone_pattern, replacement_pattern, i[5]))
    # Добавляем почту как есть
    contact.append(i[6])
    phonebook.append(contact)

print(phonebook)

# Теперь очистим получившийся список от дубликатов, при этом будем объединять информацию из разных карточек
# Для этого создадим словарь, где ключом будет кортеж из имени и фамилии
merged = {}

for c in phonebook[1:]:
    key = (c[0], c[1]) # Фамилия и Имя
    if key not in merged:
        # Если мы впервые встретили такое сочетание - добавляем в словарь как есть
        merged[key] = c
    else:
        # Склеиваем: берем значение из существующей записи,
        # а если оно пустое — подставляем из новой
        merged[key] = [old if old!='' else new for old, new in zip(merged[key], c)]

result = [phonebook[0]]+list(merged.values())
#print(result)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)