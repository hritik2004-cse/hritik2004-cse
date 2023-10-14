#simple calculator using python using if else statement :)
print("'python calculator'\n")
print("\nchoose any operations from below :-\n")
print("1.addition of two num\n2.subtraction of two nums\n3.multiplication of two num\n4.divide of two num\n5.remander of two num\n6.squareroot of a num\n7.square of a num\n8.cube of a num\n9.cube root of a num")

option = int(input("\nenter a valid option : " ))

if (option==1):
     num1=int(input("\nenter first number :"))
     num2=int(input("enter second number :"))
     print("\nresult of ",num1,"+",num2,"=",num1+num2)

elif (option==2):
     num1=int(input("\nenter first number :"))
     num2=int(input("enter second number :"))
     print("\nresult of ",num1,"-",num2,"=",num1-num2)

elif (option==3):
     num1=int(input("\nenter first number :"))
     num2=int(input("enter second number :"))
     print("\nresult of ",num1,"x",num2,"=",num1*num2)

elif (option==4):
     num1=int(input("\nenter first number :"))
     num2=int(input("enter second number :"))
     print("\nresult of ",num1,"/",num2,"=",num1/num2)

elif (option==5):
     num1=int(input("\nenter first number :"))
     num2=int(input("enter second number :"))
     print("\nresult of ",num1,"%",num2,"=",num1%num2)
     
elif (option==6):
    num=int(input("\nenter a number :"))
    num1=num**(1/2)
    print("\nthe square root of ",num,"is",num1)

elif (option==7):
    num=int(input("\nenter a number :"))
    num1=num*num
    print("\nsquare of ",num ,"is",num1)
    
elif (option==8):
    num=int(input("\nenter a number :"))
    num1=num*num*num
    print("\ncube of ",num ,"is",num1)  
    
elif (option==9):
    num=int(input("\nenter a number :"))
    num1=num**(1/3)
    print("\ncuberoot of ",num ,"is",num1)      
    
else:
    print("invalid option ")    
