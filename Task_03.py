#Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - 
#определять количество вхождений одной строки в другой. 
#COUNT или FIND или SPLIT нельзя юзать! говорил же на семинаре.

string1 = (input('Введите полную фразу '))
string2 = (input('Введите ортезок фразы '))
results = 0
sub_len = len(string2)
for i in range(len(string1)):
    if string1[i:i+sub_len] == string2:
        results += 1
print(results)
