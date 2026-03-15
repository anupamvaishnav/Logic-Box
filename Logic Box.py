while True:
    
    print("Welcome to the Pattern Generator and Number Analyzer!")

    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice=int(input("Enter Your Choice "))

    match choice:
        case 1:
            n=int(input("Enter Number Of Rows You Want "))
            for i in range (n):
                for j in range (0,i):
                    print("*", end=" ")
                print()    
        case 2:
            s=int(input("Enter the start of the range:"))
            e=int(input("Enter the end of the range:"))
            start=s 
            sum=0
            while s<=e:
                if s%2==0:
                    print(f"Number {s} is Even")
                else:
                    print(f"Number {s} is Odd")
                sum=(sum+s)
                s+=1
            print(f"Sum of all numbers from {start} to {e} is: {sum}")    
        case 3:
            print("Exiting The Program. Goodbye!")
            break
        case _:
            print("Invalid input")            
