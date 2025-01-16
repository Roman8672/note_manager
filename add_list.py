# ЗАДАНИЕ 4 ГРЕЙТ 1

# создание словаря и сбор данных пользователя

note = {}
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# ввод заголовков заметки
subtitles = []
for i in range(3):
     subtitle = input(f"Введите заголовок заметки {i + 1}: ")
     subtitles.append(subtitle)

note["subtitles"] = subtitles

#вывод переменных

print("Собранная информация о заметке:"
      f"Имя пользователя: {note['username']}",
      f"Описание заметки: {note['content']} ",
      f"Статус заметки: {note['status']}",
      f"Дата создания заметки: {note["created_date"][0:5]}",
      f"Дата истечения заметки: {note["issue_date"][0:5]}",
      f"Заголовки заметки: {note["subtitles"]}",
      sep='\n'
      )
