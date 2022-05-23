# Пользователь задает две строки. Определить количество вхождений
# одной строки в другой

def countRepeat(value, source):
    lenMin = len(value)
    limit = len(source) - lenMin + 1
    count = 0
    for i in range(0, limit):
        if source[i:i+lenMin] == value:
            count += 1
    return count

text1 = "is"
text2 = "python is a disgusting programming language"
#text1 = input()
#text2 = input()

print(countRepeat(text1, text2))