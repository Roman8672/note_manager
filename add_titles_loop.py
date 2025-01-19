# Grade 1. Этап 2: Задание 1

print("        Заметки           ")
note = {}
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например: 'Активна', 'Выполнена', 'Отложено'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
# создание списка заголовков
note["titles"] = []
# Создание заголовков
while True:
    title = input("Введите заголовок (для завершения напишите стоп или оставьте поле пустым): ")
# Завершение сбора заметок и проверка на повторения
    if title.strip() == "стоп" or title == "":
        break
    if title in note["titles"]:
            print(f"Заголовок '{title}' уже существует. Введите другой заголовок.")
            continue

    note["titles"].append(title)
# Вывод информации
print("Собранная информация о заметке:",
      f"Имя пользователя: {note["username"]}",
      sep='\n')
print("Заголовки заметки:")
for title in note["titles"]:
    print("*", title)
print(f"Описание заметки: {note["content"]} ",
      f"Статус заметки: {note["status"]}",
      f"Дата создания заметки: {note["created_date"][0:5]}",
      f"Дата истечения заметки: {note["issue_date"][0:5]}",
      sep='\n')
# print("Заголовки заметки:")
# for title in note["titles"]:
#     print("*", title)