print("we will make a pyramid by using *")
n=int(input("enter the number of rows u want"))
for i in range(1,n+1):
    for x in range(1,n+1):
        if x<=i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

        