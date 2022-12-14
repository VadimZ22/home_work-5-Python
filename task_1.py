# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# абвестмри, абв, нспмвабвгане, неумпрмабв, некмвпа, екывспыв

with open('file1.txt', 'r', encoding='utf-8') as data:
    str = data.readline().split()

desired = 'абв'
print(str)
temp_str = []
for i in str:
    if desired in i:
        # print(i)
        temp_str.append(i)
print(temp_str)
result = set(str) ^ set(temp_str)
print(' '.join(result))

with open('file1.1.txt', 'w', encoding='utf-8') as data:
    data.write(' '.join(result))