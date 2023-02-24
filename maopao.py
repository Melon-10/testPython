li = [7, 6, 3, 9, 1]
lenth = len(li)
print(lenth)
for i in range(lenth-1):
    for j in range(lenth - i - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
print(li)