n= input("enter your word: ")
v=input("enter your character: ")
c=0
number=0
while(c<len(n)):
    if(n[c]==v):
      number=number+1
    c=c+1
print("the total number of times", v, "has occured= ", number)
