# Пользователь задает две строки. Определить количество вхождений
# одной строки в другой

def countRepeat(strokaMalaya, strokaBolshaya):
    lenMin = len(strokaMalaya)
    limit = len(strokaBolshaya) - lenMin + 1
    count = 0
    for i in range(0, limit):
        if strokaBolshaya[i:i+lenMin] == strokaMalaya:
            count += 1
    return count

text1 = "is"
text2 = "python is a disgusting programming language"
#text1 = input()
#text2 = input()

print(countRepeat(text1, text2))