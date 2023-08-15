#!/usr/bin/env python3

def admin_login(username, password):
    
    if username =="admin" or username =="ADMIN" and password=="12345":
         print("Access granted")
         return "Acces granted"
    else: 
         
         print("Access denied") 
         return "Acces denied"  
    

def hows_the_weather(temperature):
    if temperature < 40:
        print("brisk")
        return "brisk"
    elif temperature >= 40 and temperature <= 65:
        print("a little chilly")
        return "a little chilly"
    elif temperature > 85:
        print("too dang hot")
        return "too dang hot"
    else:
        print("perfect")
        return "perfect"



    
    

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

    
