print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("Select an option: ")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Choose a pattern type: ")
        print("1. Right - angled triangle")
        print("2. Pyramid")
        print("3. Left - angled triangle")
        
        choiceP = int(input("Enter your pattern choice: "))
        
        if choiceP == 1:
            pRow = int(input("Enter the numbers of rows for the pattern : "))
            print("Pattern")
            for i in range(1,pRow+1):
                for j in range(1,i+1):
                    print("*",end=" ")
                print()
        elif choiceP == 2:
            pRow = int(input("Enter the numbers of rows for the pattern : "))
            print("Pattern")
            for i in range(1,pRow+1):
                for k in range(pRow, i-1, -1):
                    print(" ",end = " ")
                for j in range(1,i+1):
                    print("*",end=" ")
                for l in range(1,i):
                    print("*",end = " ")
                print()
        elif choiceP == 3:
            pRow = int(input("Enter the numbers of rows for the pattern : "))
            print("Pattern")
            for i in range(1,pRow+1):
                for k in range(pRow, i-1, -1):
                    print(" ",end = " ")
                for j in range(1,i+1):
                    print("*",end=" ")
                print()
        else:
            print("Invalid choice pattern!")
    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        sum = 0
        if start <= end:
            for i in range(start,end+1):
                if i % 2 == 0:
                    print("Number "+str(i),"is Even")
                else:
                    print("Number "+str(i),"is Odd")
                sum = sum + i
            print("Sum of all numbers from " + str(start), "to "+ str(end),"is: "+str(sum))
        else:
            for i in range(start,end-1,-1):
                if i % 2 == 0:
                    print("Number "+str(i),"is Even")
                else:
                    print("Number "+str(i),"is Odd")
                sum = sum + i
            print("Sum of all numbers from " + str(start), "to "+ str(end),"is: "+str(sum))
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice!")
