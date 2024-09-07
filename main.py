print("we will make a pyramid by using *")
n=int(input("enter the number of rows u want"))
for i in range(n):
    for x in range(i+1):
        print("* ",end="")
    print()