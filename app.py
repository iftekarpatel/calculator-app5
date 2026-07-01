from calc_func import add, subtract

def main():
    print("""Select the function from the given options:
1. Add
2. Subtract""")
    
    choice = input("Select the function (1 or 2): ")
    
    if choice == "1":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of addition is: {add(a, b)}")
    elif choice == "2":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"The result of subtraction is: {subtract(a, b)}")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()

    