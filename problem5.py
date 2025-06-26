a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for x in a:
    print(x)
    for y in b:
        print(y)
        if y in a:
            c.append(y)

print(c)
unique_list = list(set(c))
print(unique_list)