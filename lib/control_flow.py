def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        print("Access granted")
        return "Access granted"
    else:
        print("Access denied")
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        print("It's brisk out there!")
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        print("It's a little chilly out there!")
        return "It's a little chilly out there!"
    elif temperature > 85:
        print("It's too dang hot out there!")
        return "It's too dang hot out there!"
    else:
        print("It's perfect out there!")
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        return "FizzBuzz"
    elif num % 3 == 0:
        print("Fizz")
        return "Fizz"
    elif num % 5 == 0:
        print("Buzz")
        return "Buzz"
    else:
        print(num)
        return num

def calculator(operation, num1, num2):
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
        return None


    
