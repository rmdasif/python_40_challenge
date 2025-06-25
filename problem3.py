a = [1,2, 3, 5, 8, 13]
x=[]
for element in a:
  if element < 5:
      print(element)
      x.append(element)


print(x)
for element in x:
    print(element)

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
z=[]
num=int(input("enter number:"))
for element in a:
  if element < num:
      print(element)
      z.append(element)

print(z)
for element in z:
    print(element)

