a = [9, 3, 5, -12, 10, 25]
s = 0
k = 0
for i in range(len(a)):
    if a[i] % 3 == 0:
        s += a[i]
        k += 1
s_avg = s/k
print(s_avg)
