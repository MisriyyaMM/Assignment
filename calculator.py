print("CALCULATOR \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Divition ")
n=int(input("Enter your Choice(1-4) : "))
if n==1:
    a=int(input("Enter First no :"))
    b=int(input("Enter Second no : "))
    c=a+b
    print("Answer = ",c)
elif n==2:
    a = int(input("Enter First no :"))
    b = int(input("Enter Second no : "))
    c = a-b
    print("Answer = ",c)
elif n==3:
    a = int(input("Enter First no :"))
    b = int(input("Enter Second no : "))
    c = a*b
    print("Answer = ",c)
elif n==4:
    a = int(input("Enter First no :"))
    b = int(input("Enter Second no : "))
    c = a/b
    print("Answer = ",c)
else:
    print("Invalid Choice!")
