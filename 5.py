#Вариант 6
#Для "а" из русского алфавита
new_string = input("Введите строку: ")
count = new_string.lower().count('а')
print(f"Редактированная строка: {new_string.lower().replace('а', '')}")
print(f"Количество удаленных символов: {count}")