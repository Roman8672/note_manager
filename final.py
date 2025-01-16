# ЗАДАНИЕ 5 ГРЕЙТ 1

#переменные
note = {}
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

subtitles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    subtitles.append(title)

note["subtitles"] = subtitles

print("Собранная информация о заметке:")
print(f"Имя пользователя: {note['username']}")
print(f"Описание заметки: {note['content']}")
print(f"Статус заметки: {note['status']}")
print(f"Дата создания заметки: {note['created_date']}")
print(f"Дата истечения заметки: {note['issue_date']}")
print(f"Заголовки заметки:")
for title in note["subtitles"]:
     print("-", title)