# Сформировать список из N членов последовательности.
# Для N=5: 1, -3, 9, -27, 81

def list(n):
    if n < 0:
        #print("Фиг вам, а не список")
        return []
    
    kakoiToSpisok = []
    for i in range(0, n, 1):
        kakoiToSpisok.append(((-3) ** i))
    
    return kakoiToSpisok

spisok = list(5)
print(spisok)

spisok = list(-1)
print(spisok)