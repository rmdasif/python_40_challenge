num = int(input("Enter your num: "))
print("Your num is " + str(num))
y=[]
x = range(1, num +1)
for elem in x:
    print(elem)
    print("Your elem is " + str(elem +1))
    if num % elem ==0:
        print("final is " + str(elem))
        y.append(elem)

print(y)



