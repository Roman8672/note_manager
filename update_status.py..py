note = {}
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
current_status = input("Введите статус заметки. например: 'Активна', 'Выполнена', 'Отложено' - ")
note["created_status"] = [current_status]
print(f"Текущий статус: {current_status}")
print("Для изменения статуса введите число из списка предложенных вариантов")

# Создаём словарь для статусов
statuses = {
    1: "Выполнено",
    2: "Активна",
    3: "Отложено"
}

# Выводим доступные статусы
for key, value in statuses.items():
    print(f"{key}. {value}")

# Создаем список возможных статусов для проверки
status_options = list(statuses.keys())

# Ввод нового статуса
while True:
    try:
        new_status = int(input("Введите число - "))
        if new_status in status_options:
            current_status = statuses[new_status]  # Изменяем статус
            print(f"Статус заметки изменён на: {current_status}")
            break  # Выход из цикла после успешного изменения статуса
        else:
            print("Некорректный статус. Выберите число из списка.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите число.")

print(f"\nОбновлённый статус заметки: {current_status}.")