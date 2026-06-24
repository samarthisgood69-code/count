l=int(input("enter l range: "))
u=int(input("enter u range: "))
print("Prime numbers between", l, "and", u, "are:")
for number in range(l, u+1):
    if number>1:
        for p in range(2, number):
           if(number % p)==0:
               break
        else:
            print(number)
