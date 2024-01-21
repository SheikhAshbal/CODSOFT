def options():
    print("""Below are the Options to perform Basic Arithmetic Operations         
        1. Addition
        2. Multiplication
        3. Subtraction
        4. Division """)
    global operation
    while True:
        try:
            operation = int(input("Enter a operation number(1/2/3/4) and 0 for Exit : "))
            if operation<0 or operation>4:
                print("\nPlease enter a number between 1 and 4.\n")  
            elif 0<=operation<=4:
                break
        except:
            print("\nInvalid Input! Please Enter a Number Only.")
                    
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
    
    while True:
        options()
        if operation==1:
            result=addition()
            print(f"The addition of {result[0]} numbers is:{result[1]}")
               
        elif operation==2:
            result=multiplication()
            print(f"The product of {result[0]} numbers is :{result[1]}")
                
        elif operation==3:
            print(f"The result is:{subtraction()}")
                
        elif operation==4:
            print(f"The result is:{division()}")
        elif operation==0:
            print("Exiting....")
            break
        input("Press any key to continue")
        
if __name__== '__main__':
    print("\n---------> CALCULATER <-----------\n")
    main()                      
