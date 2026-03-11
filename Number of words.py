
s = input("Введіть текст: ")
k = 1
n = len(s)

for i in range(n):
    l = str(s[i])
    if l == ' ':
        k+=1

print(k)

'''
s = input("Введіть текст: ")
k = 1

for i in s:

    if i == ' ':
        k+=1
print(k)
'''