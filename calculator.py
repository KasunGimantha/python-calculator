print(f"{'*'*10}Welcome to Python Calculator{'*'*10}")

print("-"*50)
print('Enter + for addition')
print('Enter - for subtraction')
print('Enter * for multiplication')
print('Enter / for division')
print("Enter % for modulus")
print("Enter ** for exponentiation")
print("Enter // for integer division")
print("-"*50)

out = None

while (out != 'Y'):
    first_num = float(input("Enter first Number: "))
    second_num = float(input("Enter second Number: "))
    operator = input("Enter your operation: ")
    print('-'*50)
    if operator == '+':
        print(f"Addition:{first_num+second_num}")

    elif operator == '-':
        print(f"Subtraction:{first_num-second_num}")

    elif operator == '*':
        print(f"Multiplication:{first_num*second_num}")

    elif operator == '/':
        if (second_num == 0):
            print("Division by zero error!")
        else:
            print(f"Division:{first_num/second_num}")

    elif operator == '%':
        print(f"Modulus:{first_num % second_num}")

    elif operator == '**':
        print(f"exponentiation:{first_num**second_num}")

    elif operator == '//':
        print(f"Integer division:{first_num//second_num}")

    else:
        print("Invalid operator!")
    print('-'*50)
    out = input("Do you want to Exit(Y/N):")
    print('-'*50)
print("Have a nice day!")
