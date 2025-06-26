string = input("Give me your string: ")
print("Your string is " + string)
n=len(string)
z=0
#for c in string:
#    print("one letter: " + c)
a=string[0:]
b=string[::-1]
for x in a:
    print(x)
    if x == b[z]:
        z=z+1

if z==n:
    print("palindrome")
