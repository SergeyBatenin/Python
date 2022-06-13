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


# Работает, но выглядит страшно =(
def remove_word1(data, value):
    return " ".join(list(filter(lambda x: x.lower().find(value) < 0, data.split())))


# Работает, но выглядит страшно =( №2
def remove_word2(data, value):
    return " ".join([i for i in data.split() if i.lower().find('абв') < 0])


text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
target = "абв"
edited_text = remove_word(text, target)
print(edited_text)
print(edited_text == remove_word1(text, target)) # True
print(edited_text == remove_word2(text, target)) # True