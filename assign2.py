num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

opp = input("Select which operation you want to perform (1. Sum, 2. Difference, 3. Product, 4. Quotient): ")

if opp == "1":
    sum = num1 + num2
    print(f"The sum of two numbers is {sum}")
elif opp == "2":
    difference = num1 - num2
    print(f"The difference of two numbers is {difference}")
elif opp == "3":
    product = num1 * num2
    print(f"The product of two numbers is {product}")
elif opp == "4":
    if num2 != 0:
        quotient = num1 / num2
        print(f"The quotient of two numbers is {quotient}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation selected")