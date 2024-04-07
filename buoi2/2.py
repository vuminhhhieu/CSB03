
# def count_occurrences(string, char):
#     count = 0
#     for c in string:
#         if c == char:
#             count += 1
#     return count

# input_string = "Python là một ngôn ngữ lập trình phổ biến"
# character_to_count = "n"
# count = count_occurrences(input_string, character_to_count)
# print(f"Số lần ký tự '{character_to_count}' xuất hiện trong chuỗi là {count}")

a = str(input("Nhap chuoi: "))
b = str(input("Nhap ki tu can dem: "))
c = a.count(b)
print(c)