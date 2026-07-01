 
from calc_func import add, subtract, divide,multiply,calculate_area

def main():
    print("""Select the function from the given options:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Calculate Area of Rectangle""")

    
    choice = input("Select the function (1, 2, 3, 4, or 5): ")
    
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
    elif choice == "5":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print(f"The area of the rectangle is: {calculate_area(length, width)}")
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

        

if __name__ == "__main__":
    main()

    