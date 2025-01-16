# ЗАДАНИЕ 4 ГРЕЙТ 1

print("        Заметки           ")
#переменные
username = input("Введите имя пользователя:")
title = input("Введите заголовок:")
subtitle1 = input("Введите под заголовок 1 ")
subtitle2 = input("Введите под заголовок 2 ")
subtitle3 = input("Введите под заголовок 3 ")
subtitle = [subtitle1, subtitle2, subtitle3]
content = input("Введите описание:")
status = input("Введите статус заметки. Например:"
               "Активно, "
               "в работе или "
               "выполнено. ")
created_date = int(input("Введите дату создания заметки. День, месяц, год. Пример 01.01.2024 "))
issue_date = int(input("Введите дату окончания заметки. День, месяц, год. Пример 01.01.2024 "))


#вывод переменных
print ("Имя пользователя ", username)
print("Заголовок заметки", title)
print("subtitle")
print("Описание заметки",content)
print("Статус заметки", status)
print("Дата создания заметки", created_date [0:5])
print("Дата истечения заметки ", issue_date [0:5])
