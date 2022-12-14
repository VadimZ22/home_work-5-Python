# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file4.txt', 'r') as data:
    string = data.readline().split()

new_str=[]
for i in string:
    count = 1
    for c in range(1, len(i)):
        if i[c] == i[c-1]:
            count+=1
        if i[c] != i[c-1]:
            symbol = str(count) + i[c-1]
            new_str.append(symbol)
            count = 1
        if c.__index__() == len(i) - 1:
            symbol = str(count) + i[c]
            new_str.append(symbol)
    if len(string) > 1 and string.index(i) != len(string) - 1:
        new_str.append(' ')
print(''.join(new_str))

with open('file4.txt', 'a') as data:
    data.write('\n' + ''.join(new_str))



with open('file4.txt', 'r') as data:
    data.readline()
    string2 = data.readline()

new_str2=[]
count = 0
for i in string2:
    for c in i:
        if c.isalpha():
            symbol = count * c
            new_str2.append(symbol)
            count = 0
        elif c == ' ': new_str2.append(c)
        else:
            count += int(c)
print(''.join(new_str2))

with open('file4.txt', 'a') as data:
    data.write('\n' + ''.join(new_str2))


