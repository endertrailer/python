answer_file = open("hello.txt", "a")
num1 = float(input("enter a number: "))
num2 = float(input("enter second number: "))
operator = input("enter operation: ")
write = answer_file.write
if operator == "+":
    write(", ")
    write(str(num1 + num2))
elif operator == "*":
    write(", ")
    write(str(num1 * num2))
elif operator == "-":
    write(", ")
    write(str(num1 - num2))
elif operator == "/":
    write(", ")
    write(str((num1 / num2)))
else:
    print("enter a valid operator: ")
