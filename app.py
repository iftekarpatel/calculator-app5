from calc_func import add, subtract, divide,multiply

def main():
    print("""Select the function from the given options:
1. Add
2. Subtract
3. Multiply
4. Divide""")
    
    choice = input("Select the function (1, 2, 3, or 4): ")
    
    if choice == "1":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of addition is: {add(a, b)}")
    elif choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of subtraction is: {subtract(a, b)}")
    elif choice == "3":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of multiplication is: {multiply(a, b)}")
    elif choice == "4":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of division is: {divide(a, b)}")
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

    