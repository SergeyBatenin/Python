# Напишите программу, удаляющую из текста все слова содержащие "абв",
# которое регистронезависимо. Используйте знания с последней лекции.
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

def remove_word(data, value):
    new_data = data.split()
    result = []
    for item in new_data:
        if value not in item.lower():
           result.append(item)
    return " ".join(result)


text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
target = "абв"
edited_text = remove_word(text, target)
print(edited_text)