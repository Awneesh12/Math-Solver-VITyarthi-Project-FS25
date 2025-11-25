import math
import numpy as np

# Asks the feature user want to use in an infinte loop
while True:
# Greetings
    print("=== MATH SOLVER ===\n")
    feature=int(input("What feature do you want to use? \n" \
    "[1] Basic Calculation between Two Numbers \n" \
    "[2] Quadratic Equation Solver \n" \
    "[3] Two Linear Equation with Two Variables \n" \
    "[4] LCM and HCF Calculation of Two Numbers \n" \
    "[5] Prime Number Verifier and Prime Factor Calculator \n" \
    "[6] Statistics \n" \
    "[7] Area and Perimeter Calculator \n" \
    "[8] Factorial Calculator \n" \
    "[9] Matrix Operations \n" \
    "[0] Exit \n\n"
    "Please press the number key corresponding to the feature you want to use: "))

# Feature --> Exit
    if feature==0:
        input("Thank You using The Math Solver! \n" \
        "Press any key to close this Window...")
        break

# Feature 1 --> Basic Calculation between Two Numbers
    if feature==1:
        print("\n--- Basic Calculation --- \n")
        
# Sub Feature Info
        while True:
            subFeature=int(input("What type of Basic Calculation do you want to perform? \n" \
            "[1] Addition \n" \
            "[2] Subtraction \n" \
            "[3] Multiplication \n" \
            "[4] Division \n" \
            "[5] Exponential \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1,2,3,4,5]:
                print("Invalid Input. Please select a number from 1 to 5 only, or 0 to exit \n")
                continue

# Common Code
            num1=float(input("\nPlease enter the First Number: "))
            num2=float(input("Please enter the Second Number: "))

# All other Sub-Features
            if subFeature==1: # Addition
                result=num1+num2
                operation="sum"
            elif subFeature==2: #Subtraction
                result=num1-num2
                operation="difference"
            elif subFeature==3: # Multiplication
                result=num1*num2
                operation="product"
            elif subFeature==4: #Division
                if num2==0:
                    print("\nInvalid Input. Denominator cannot be zero, the answer is Infinity\n")
                    continue
                else:
                    result=num1/num2
                operation="quotient"
            elif subFeature==5: # Exponential
                result=num1**num2
                operation="exponential"

# Final Output
            print(f"\nThe {operation} of {num1} and {num2} is {result}\n")

            ASK=input("Do you want to perform another Basic Calculation? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing with Basic Calculation... \n")
                continue

# ---------- FEATURE 1 ENDS ----------

# Feature 2 --> Quadratic Equation Solver
    elif feature==2:
        print("\n--- Quadratic Equation Solver --- \n")

# Sub Feature Info
        while True:
            subFeature=int(input("What do you want to perform? \n" \
            "[1] Finding roots of a Quadratic Equation \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1]:
                print("Invalid Input. Please select a number 1 only, or 0 to exit \n")
                continue

# User Inputs
            print("\nYou'll be asked for the values of a, b, and c, in a quadratic equation ax^2 + bx + c = 0")
            a=float(input("What is the value of 'a'? "))
            if a==0: # Precaution
                print("The value of 'a' cannot be zero \n")
                continue
            else:
                b=float(input("What is the value of 'b'? "))
                c=float(input("What is the value of 'c'? "))

# Calculation and Output
            discriminant=(b**2)-(4*a*c)
            
            if discriminant<0: # No Real Roots
                print("\nThe equation has no real roots (only complex root)\n")
            elif discriminant==0: # One Real Root
                root1=-b/(2*a)
                print(f"\nThe root of the equation is {root1}\n")
            else: # Two Distint Roots
                root1=(-b+math.sqrt(discriminant))/(2*a)
                root2=(-b-math.sqrt(discriminant))/(2*a)
                print(f"\nThe roots of the equation are {root1} and {root2}\n")

            ASK=input("Do you want to find another equation's root? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing with Quadratic Equation... \n")
                continue

# ---------- FEATURE 2 ENDS ----------

# Feature 3 --> Two Linear Equation with Two Variables
    elif feature==3:
        print("\n--- Solving Two Linear Equations with Two Variables --- \n")

# Sub Feature Info
        while True:
            subFeature=int(input("What do you want to perform? \n" \
            "[1] Solving the Two Equations \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1]:
                print("Invalid Input. Please select a number 1 only, or 0 to exit \n")
                continue

# User Inputs
            print("\nYou'll be asked for the coefficients in the equations, 'a1*x + b1*y = c1' and 'a2*x + b2*y = c2' \n")
            print("First Equation (a1*x + b1*y = c1))")
            a1=float(input("Enter the value of a1: "))
            b1=float(input("Enter the value of b1: "))
            c1=float(input("Enter the value of c1: "))
            print("\nNow for the Second Equation (a2*x + b2*y = c2))")
            a2=float(input("Enter the value of a2: "))
            b2=float(input("Enter the value of b2: "))
            c2=float(input("Enter the value of c2: "))

# Calculation and Output
            determinant=(a1*b2)-(a2*b1) # To check whether the solutions is(are) no solution or infinite

            if determinant==0:
                # Calculation of Dx and Dy for secondary check
                Dx=(c1*b2)-(c2*b1)
                Dy=(a1*c2)-(a2*c1)

                if Dx==0 and Dy==0:
                    print("\nThere are Infinite Solutions. The two equations represent the same line\n")
                else:
                    print("\nThere are No Solutions. The two equations represent parallel lines\n")
            
            else:
                Dx=(c1*b2)-(c2*b1)
                Dy=(a1*c2)-(a2*c1)
                x=Dx/determinant
                y=Dy/determinant
                print(f"\nThe value for 'x' is {x} and for 'y' is {y}\n")

            ASK=input("Do you want to solve another equation? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing with Two Linear Equations... \n")
                continue

# ---------- FEATURE 3 ENDS ----------

# Feature 4 --> LCM and HCF Calculation of Two Numbers
    elif feature==4:
        print("\n--- LCM and HCF Calculation ---\n")

# Sub Feature Info
        while True:
            subFeature=int(input("What do you want to calculate? \n" \
            "[1] Least Common Multiple \n" \
            "[2] Highest Common Factor \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1,2]:
                print("Invalid Input. Please select a number 1 and 2 only, or 0 to exit \n")
                continue

# Common Code
            num1=round(float(input("\nPlease type the First Number: ")))
            num2=round(float(input("Please type the Second Number: ")))

# Precaution
            if num1<=0 or num2<=0:
                print("\nInvalid Input. Please Enter a Positive Integer\n")
                continue

# Sub-Features
            temp1=num1
            temp2=num2

            while temp2:
                temp1,temp2=temp2,temp1%temp2
            HCF=temp1

            if subFeature==1: # LCM
                LCM=(num1*num2)//HCF
                operation="LCM"
                result=LCM
            elif subFeature==2: # HCF
                operation="HCF"
                result=HCF
            
# Final Output
            print(f"\nThe {operation} of {num1} and {num2} is {result} \n")

            ASK=input("Do you want to find another LCM or HCF? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing with LCM and HCF... \n")
                continue

# ---------- FEATURE 4 ENDS ----------

# Feature 5 --> Prime Number Verifier and Prime Factor Calculator
    elif feature==5:
        print("\n--- Prime Number Verifier and Prime Factor Calculator ---\n")

# Sub Feature Info
        while True:
            subFeature=int(input("What do you want to do? \n" \
            "[1] Prime Number Verifyer \n" \
            "[2] Prime Factor Calculator \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))
        
# Sub Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1,2]:
                print("Invalid Input. Please select a number 1 and 2 only, or 0 to exit \n")
                continue

# Common Code
            num=round(float(input("\nPlease type a number: ")))

            if num<=0:
                print("\nInvalid Input. Please Enter a Positive Integer\n")
                continue

# Sub-Feature 1 --> Prime Number Verifier
            if subFeature==1:
                prime=True
                limit=int(num**0.5)

                if num>3 and (num%2==0 or num%3==0):
                    prime=False
                elif num==1:
                    prime=False
                else:
                    for i in range(2, limit+1):
                        if num%i==0:
                            prime=False
                        else:
                            prime=True
                
                if prime:
                    print(f"\n{num} is a Prime Number\n")
                else:
                    print(f"\n{num} is not a Prime Number\n")

# Sub Feature 2 --> Prime Factors
            elif subFeature==2:
                factors=[]
                originalNum=num

                while num%2==0:
                    factors.append(2)
                    num=num//2
                
                i=3
                while i*i<=num:
                    while num%i==0:
                        factors.append(i)
                        num=num//i
                    i+=2
                
                if num>2:
                    factors.append(num)
                
                print(f"\nThe Prime Factors of {originalNum} are {factors}\n")

            ASK=input("Do you want to perform Prime Calculations again? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing Prime Calculations... \n")
                continue

# ---------- FEATURE 5 ENDS ----------

# Feature 6 --> Statistics
    elif feature==6:
        print("\n--- Statistics ---\n")
    
# Sub Feature Info
        while True:
            subFeature=int(input("What do you want to calculate? \n" \
            "[1] Mean, Median, and Mode \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break
        
# Precaution for Wrong Input
            if subFeature not in [1]:
                print("Invalid Input. Please select a numbers 1 only, or 0 to exit \n")
                continue

# Common Code
            totalElements=(int(input("\nPlease state the Number of Elements of the Data: ")))
            data=[]

            for i in range(1, totalElements+1):
                data.append(float(input(f"Please input element {i} : ")))
            
            for i in range(totalElements):
                for j in range(0, totalElements-i-1):
                    if data[j]>data[j+1]:
                        data[j], data[j+1] = data[j+1], data[j]

# Sub-Features
# Mean
            mean=sum(data)/totalElements
            
# Median
            if totalElements%2!=0:
                median=data[totalElements//2]
            else:
                mid1=data[totalElements//2-1]
                mid2=data[totalElements//2]
                median=(mid1+mid2)/2
            
# Mode
            maxFrequency = 0
            modes = []
            
            if totalElements > 0:
                currentElement = data[0]
                currentFrequency = 0
                
                for k in data:
                    if k == currentElement:
                        currentFrequency += 1
                    else:
                        if currentFrequency > maxFrequency:
                            maxFrequency = currentFrequency
                            modes = [currentElement]
                        elif currentFrequency == maxFrequency:
                            modes.append(currentElement)
                        
                        currentElement = k
                        currentFrequency = 1
                
                if currentFrequency > maxFrequency:
                    modes = [currentElement]
                elif currentFrequency == maxFrequency and currentElement not in modes:
                    modes.append(currentElement)
            
            if maxFrequency == 1 and totalElements > 1 and len(modes) == totalElements:
                modes = ["No mode"]
            
# Output
            print(f"\nThe Mean, Median, and Mode of the Data {data} is '{mean}', '{median}', and '{modes}' respectively\n")

            ASK=input("Do you want to do statistics again? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing Statistics... \n")
                continue

# ---------- FEATURE 6 ENDS ----------

# Feature 7 --> Area and Perimeter Calculator
    elif feature==7:
        print("\n--- Area and Perimeter Calculator ---\n")

#Sub Feature Info
        while True:
            subFeature=int(input("What do you want to find? \n" \
            "[1] Area and Perimeter \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1]:
                print("Invalid Input. Please select a number 1 only, or 0 to exit \n")
                continue

# Calculations
            while True:
                shape=int(input("\nWhich Shape's Area and Perimeter do you want to find? \n" \
                "[1] Square \n" \
                "[2] Rectange \n" \
                "[3] Circle \n" \
                "[4] Triangle \n" \
                "[5] Parallelogram \n" \
                "[0] Back \n\n" \
                "Please press the number key corresponding to which shape you want to find the area of: "))

                if shape==0:
                    print()
                    break
                    
                if shape not in [1,2,3,4,5]:
                    print("Invalid Input. Please select a numbers from 1 to 5 only, or 0 to exit")
                    continue

                if shape==1:
                    side=float(input("\nWhat is the length of a side (in cm)? "))
                    area=side*side
                    perimeter=4*side
                    shapeName="Square"
                elif shape==2:
                    length=float(input("\nWhat is the length of the Rectange (in cm)? "))
                    breadth=float(input("What is the breadth of the Rectange (in cm)? "))
                    area=length*breadth
                    perimeter=2*(length+breadth)
                    shapeName="Rectangle"
                elif shape==3:
                    radius=float(input("\nWhat is the radius of the Circle (in cm)? "))
                    area=math.pi*radius*radius
                    perimeter=2*math.pi*radius
                    shapeName="Circle"
                elif shape==4:
                    a=float(input("\nWhat is the length of first side (in cm)? "))
                    b=float(input("what is the length of second side (in cm)? "))
                    c=float(input("What is the length of third side (in cm)? "))
                    perimeter=a+b+c
                    semiPerimeter=perimeter/2
                    notArea=semiPerimeter*(semiPerimeter-a)*(semiPerimeter-b)*(semiPerimeter-c)
                    if notArea<0:
                        print("Please input valid sides, the sides you inputted doesn't make a Triangle")
                        continue
                    else:
                        area=math.sqrt(notArea)
                        shapeName="Triangle"
                elif shape==5:
                    knownSide=float(input("What is the length of a known side (in cm)? "))
                    adjacentToKnownSide=float(input("What is the lenght of the adjacent side of the known side (in cm)? "))
                    height=float(input("What is the height of the Parallelogram from a knwon side (in cm)? "))
                    area=knownSide*height
                    perimeter=2*(knownSide+adjacentToKnownSide)
                    shapeName="Parallelogram"

# Output
                print(f"\nThe Area and Perimeter of {shapeName} are {area} cm^2 and {perimeter} cm repectively\n")
                break
            
            ASK=input("Do you want to find Area and Perimeter again? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing Area and Perimeter... \n")
                continue

# ---------- FEATURE 7 ENDS ----------

# Feature 8 --> Factorial Calculator
    elif feature==8:
        print("\n--- Factorial Calculator ---\n")

# Sub Feature Info
        while True:
            subFeature=int(input("What do you want to do? \n" \
            "[1] Calculate Factorial \n" \
            "[0] Back to Main-Menu \n\n" \
            "Press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1]:
                print("Invalid Input. Please select number 1, or 0 to exit\n")
                continue

# Main Code and Output
            num=round(float(input("\nType a number: ")))

            while True:
                if num<0:
                    print("Invalid Integer. Please input a positive integer.")
                    break
                elif num==0 or num==1:
                    print(f"\nThe facotorial of {num} is 1")
                    break
                elif num>=2:
                    temp=1
                    fact=1
                    while temp<=num:
                        fact=fact*temp
                        temp+=1
                    print(f"\nThe factorial of {num} is {fact}\n")
                    break

            ASK=input("Do you want to find a Factorial again? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing Factorial... \n")
                continue

# ---------- FEATURE 8 ENDS ----------

# Feature 9 --> Matrix Operations
    elif feature==9:
        print("\n--- Matrix Operation --- \n")

# Sub Feature Info
        while True:
            subFeature=int(input("Which Matrix Operation do you want to perform? \n" \
            "[1] Addition of Two Matrices \n" \
            "[2] Multiplcation of Two Matrices \n" \
            "[3] Inverse of a Matrix \n" \
            "[0] Back to Main-Menu \n\n" \
            "Please press the number key corresponding to the operation you want to perform: "))

# Sub-Feature 0 --> Back to Main-Menu
            if subFeature==0:
                print()
                break

# Precaution for Wrong Input
            if subFeature not in [1,2,3]:
                print("Invalid Input. Please input a number from 1 to 3, or 0 to exit")
                continue

# Common for Sub-Feature 1 and 2
            if subFeature==1 or subFeature==2:
                while True:
                    N=int(input("What type of Matrix are both? \n" \
                    "[1] 2x2 \n" \
                    "[2] 3x3 \n" \
                    "[0] Back \n\n" \
                    "Please press a number key corresponding to the operation you want to perform: "))

                    if N==0:
                        print()
                        break

                    if N not in [1,2]:
                        print("Invalid Input. Please input number 1 and 2 only, or 0 to exit")
                        continue

                    if N==1:
                        print("\nPlease input the elements of Matrix A")
                        a=float(input("What is the Element (1,1)? "))
                        b=float(input("What is the Element (1,2)? "))
                        c=float(input("What is the Element (2,1)? "))
                        d=float(input("What is the Element (2,2)? "))
                        print()
                        print("Now you'll be asked for elements of Matrix B")
                        e=float(input("What is the Element (1,1)? "))
                        f=float(input("What is the Element (1,2)? "))
                        g=float(input("What is the Element (2,1)? "))
                        h=float(input("What is the Element (2,2)? "))

                        matrix_A=np.array([[a,b],[c,d]])
                        matrix_B=np.array([[e,f],[g,h]])

                    elif N==2:
                        print("\nPlease input the elements of Matrix A")
                        a=float(input("What is the Element (1,1)? "))
                        b=float(input("What is the Element (1,2)? "))
                        c=float(input("What is the Element (1,3)? "))
                        d=float(input("What is the Element (2,1)? "))
                        e=float(input("What is the Element (2,2)? "))
                        f=float(input("What is the Element (2,3)? "))
                        g=float(input("What is the Element (3,1)? "))
                        h=float(input("What is the Element (3,2)? "))
                        i=float(input("What is the Element (3,3)? "))
                        print()
                        print("Now you'll be asked for elements of Matrix B")
                        j=float(input("What is the Element (1,1)? "))
                        k=float(input("What is the Element (1,2)? "))
                        l=float(input("What is the Element (1,3)? "))
                        m=float(input("What is the Element (2,1)? "))
                        n=float(input("What is the Element (2,2)? "))
                        o=float(input("What is the Element (2,3)? "))
                        p=float(input("What is the Element (3,1)? "))
                        q=float(input("What is the Element (3,2)? "))
                        r=float(input("What is the Element (3,3)? "))

                        matrix_A=np.array([[a,b,c],[d,e,f],[g,h,i]])
                        matrix_B=np.array([[j,k,l],[m,n,o],[p,q,r]])

# Seperates here by the operation of Addition or Multiplication                        
                    if subFeature==1:
                        resultantMatrix=np.add(matrix_A, matrix_B)
                        matrixOperation="addition"
                    elif subFeature==2:
                        resultantMatrix=np.dot(matrix_A, matrix_B)
                        matrixOperation="multiplication"

                    print(f"\nThe {matrixOperation} of \n" \
                          f"{matrix_A} and \n" \
                          f"{matrix_B} is \n" \
                          f"{resultantMatrix}")
                    break

# Sub-Feature 3 --> Inverse of a Matrix
            else:
                while True:
                    N=int(input("What type of Matrix is it? \n" \
                    "[1] 2x2 \n" \
                    "[2] 3x3 \n" \
                    "[0] Back \n\n" \
                    "Please press a number key corresponding to the operation you want to perform: "))

                    if N==0:
                        print()
                        break

                    if N not in [1,2]:
                        print("Invalid Input. Please input number 1 and 2 only, or 0 to exit")
                        continue

                    if N==1:
                        print("\nPlease input the elements of Matrix")
                        a=float(input("What is the Element (1,1)? "))
                        b=float(input("What is the Element (1,2)? "))
                        c=float(input("What is the Element (2,1)? "))
                        d=float(input("What is the Element (2,2)? "))
                        matrix=np.array([[a,b],[c,d]])
                    
                    elif N==2:
                        print("\nPlease input the elements of Matrix A")
                        a=float(input("What is the Element (1,1)? "))
                        b=float(input("What is the Element (1,2)? "))
                        c=float(input("What is the Element (1,3)? "))
                        d=float(input("What is the Element (2,1)? "))
                        e=float(input("What is the Element (2,2)? "))
                        f=float(input("What is the Element (2,3)? "))
                        g=float(input("What is the Element (3,1)? "))
                        h=float(input("What is the Element (3,2)? "))
                        i=float(input("What is the Element (3,3)? "))
                        matrix=np.array([[a,b,c],[d,e,f],[g,h,i]])

                    if np.linalg.det(matrix)!=0:
                        inv_mat=np.linalg.inv(matrix)
                        print(f"\nThe inverse of matrix \n" \
                              f"{matrix} is \n" \
                              f"{inv_mat}\n")
                    else:
                        print("\nThe matrix is a singular matrix, therefore inverse cannot be calculated.\n")
                        continue
                    break
            
            ASK=input("Do you want to do Matrix calculations? again? [Y/N] ").upper()

            if ASK=="N":
                print()
                break
            elif ASK=="Y":
                print("Okay! \n")
            else:
                print("Invalid Input. Continuing Matrix... \n")
                continue

# ---------- FEATURE 9 ENDS ----------

# Precaution for Wrong Input
    if feature not in [1,2,3,4,5,6,7,8,9]:
        print("Invalid Input. Please input numbers from 1 to 9 only, or 0 to exit \n")
        continue
