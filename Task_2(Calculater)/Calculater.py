def options():
    print("""Below are the Options to perform Basic Arithmetic Operations         
        1. Addition
        2. Multiplication
        3. Subtraction
        4. Division 
        For Exit press 0""")
    global operation
    operation=input("Enter the operation number(1/2/3/4) ")
def addition():
    add_accumulater=0
    numbers=int(input("Enter the numbers you want to add:"))
    for i in range(1,numbers+1):
        num=float(input(f"Enter the num{i}: "))
        add_accumulater+=num
    return numbers,add_accumulater
def subtraction():
    num1=float(input("Enter the value of num1:"))
    num2=float(input("Enter the value of num2:"))
    subtract=num1-num2
    return subtract
def multiplication():
    product=1
    numbers=int(input("Enter the numbers you want to product:"))
    for i in range(1,numbers+1):
        num=float(input(f"Enter the num {i}: "))
        product*=num
    return numbers,product    
def division():
    num1=float(input("Enter the value of num1:"))
    num2=float(input("Enter the value of num2:"))
    while True:
        try:
            divide=num1/num2
            return divide
        except:
            print("Error!!!, cannot divide by zero")
            num2=float(input("Enter the value of num2 again:")) 
def main():
    
    options()
        
    if operation=="1":
        result=addition()
        print(f"The addition of {result[0]} numbers is:{result[1]}")
               
    elif operation=="2":
        result=multiplication()
        print(f"The product of {result[0]} numbers is :{result[1]}")
                
    elif operation=="3":
        print(f"The result is:{subtraction()}")
                
    elif operation=="4":
        print(f"The result is:{division()}")
                
    else:
        print("Enter a valid input!")
                
main()
permission=input("To continue the calculater press Y and press N for stop:").upper()
while permission=="Y":
    main()
    permission=input("To continue the calculater press Y and press N for stop:")
if permission=="N":
    print("DONE!!")
    