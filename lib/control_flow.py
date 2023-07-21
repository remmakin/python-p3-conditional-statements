def admin_login(username, password):
    # your code here
    pass
    if (username.lower() == "admin") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

result = admin_login("admin", 12345)
print(result)

# pass


def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 60:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    # pass


def fizzbuzz(num):
    # your code here
    pass
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


result = fizzbuzz(27)
print(result)


# pass


def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")


result = calculator("+", 5, 3)
print(result)
