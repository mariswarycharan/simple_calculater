# a=float(input("enter your first number:"))
# b=float(input("enter your second number:"))

from email.charset import add_charset


while True:
    print("""simple calcalator select your option which operation do you want do
        option 1 = To add two numbers
        option 2 = To sub two numbers 
        option 3 = To multiple two numbers
        option 4 = To divide two numbers
        option 5 = To divide two numbers and give quotient as answer
        option 6 = To divide two numbers and give quotient as answer    
        option 7 = To power two numbers
        option 8 = To squaring the number, give a value only and enter b value as 0
        option 9 = To cubing numbers , give a value only and enter b value as 0 """) 
    c=int(input("enter your option:"))
    a=float(input("enter your first number:"))
    b=float(input("enter your second number:"))
     
# To add two numbers          
    def add(a,b):
        return a+b
# To sub two numbers    
    def sub(a,b):
        return a-b
# To multiple two numbers    
    def multiple(a,b):
        return a*b
# To divide two numbers    
    def div(a,b):
        return a+b
# To divide two numbers and give remainder as answer    
    def remainder(a,b):
        return a%b
# To divide two numbers and give quotient as answer    
    def quotient(a,b):
        return a/b
# To power two numbers
    def power(a,b):
        return a**b
# To squaring the number    
    def square(a):
        return a**2
# To cubing the numbers
    def cube(a):
        return a**3
    

    # c=int(input("enter your option:"))
    if c < 0:
        print("enter your option correctly and entered option is not suitable ")
        break
    if c == 1:
        print("answer:",add(a,b))
    elif c == 2:
        print("answer:",sub(a,b))
    elif c == 3:
        print("answer:",multiple(a,b))
    elif c == 4:
        print("answer:",div(a,b))
    elif c == 5:
        print("answer:",remainder(a,b))
    elif c == 6:
        print("answer:",quotient(a,b))
    elif c == 7:
        print("answer:",power(a,b))
    elif c == 8:
        print("answer:",square(a)) 
    elif c == 9:
        print("answer:",cube(a)) 
        
    print()                  
                                 
         
     
    
    
    
        
    
        