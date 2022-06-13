# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# def compression(item):
#     result = ""
#     prev_symbol = ""
#     count = 1
#     for symbol in item:
#         if prev_symbol == "":
#             prev_symbol = symbol
#             continue

#         if symbol == prev_symbol:
#             count += 1
#         else:
#             result += str(count) + prev_symbol
#             prev_symbol = symbol
#             count = 1
#     result += str(count) + prev_symbol
#     return result


# def uncompression(item):
#     result = ""
#     count = ""
#     for symbol in item:
#         if symbol.isdigit():
#             count += symbol
#         else:
#             result += symbol * int(count)
#             count = ""

#     return result


# text = "aabbbcdddde"
# comp_text = compression(text)
# #print(comp_text)
# uncomp_text = uncompression(comp_text)
# #print(uncomp_text)
# print(text == uncomp_text)


def compress(path):
    with open(path, "r", encoding="utf_8") as data:
        input_value = data.read()
    separator = "#"
    output_value = ""
    prev_symbol = ""
    count = 1
    for symbol in input_value:
        if prev_symbol == "":
            prev_symbol = symbol
            continue

        if symbol == prev_symbol:
            count += 1
        else:
            if count < 4:
                if prev_symbol == separator:
                    output_value += separator + chr(count) + prev_symbol
                    prev_symbol = symbol
                    count = 1
                else:
                    output_value += prev_symbol * count
                    prev_symbol = symbol
                    count = 1
            else:
                output_value += separator + chr(count) + prev_symbol
                prev_symbol = symbol
                count = 1
    if count < 4:
        if prev_symbol == separator:
            output_value += separator + chr(count) + prev_symbol
        else:
            output_value += prev_symbol * count
    else:
        output_value += separator + chr(count) + prev_symbol
    #print(output_value)
    with open("compressFile.txt", "a", encoding="utf_8") as data:
        data.writelines(f"{output_value}\n")


def decompress(path):
    with open(path, "r", encoding="utf_8") as data:
        input_value = data.readlines()
    for item in input_value:
        output_value = ""
        next_point = -1 #Костыль
        for i in range(len(item) - 1):
            if i < next_point:
                continue
            symbol = item[i]
            if symbol != "#":
                output_value += symbol
            else:
                curr_value = ord(item[i + 1]) * item[i + 2]
                #print(f"current_value = {curr_value}")
                output_value += curr_value
                next_point = i + 3
            #print(f" current_point = {i}, output_value = {output_value}")
        print(output_value)




path1 = "input1.txt"
path2 = "input2.txt"
path3 = "input3.txt"
decompress_path = "CompressFile.txt"
# compress(path1)
# compress(path2)
# compress(path3)
decompress(decompress_path)