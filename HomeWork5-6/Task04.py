# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(item):
    result = ""
    prev_symbol = ""
    count = 1
    for symbol in item:
        if prev_symbol == "":
            prev_symbol = symbol
            continue

        if symbol == prev_symbol:
            count += 1
        else:
            result += str(count) + prev_symbol
            prev_symbol = symbol
            count = 1
    result += str(count) + prev_symbol
    return result


def uncompression(item):
    result = ""
    count = ""
    for symbol in item:
        if symbol.isdigit():
            count += symbol
        else:
            result += symbol * int(count)
            count = ""

    return result


text = "aabbbcdddde"
comp_text = compression(text)
#print(comp_text)
uncomp_text = uncompression(comp_text)
#print(uncomp_text)
print(text == uncomp_text)