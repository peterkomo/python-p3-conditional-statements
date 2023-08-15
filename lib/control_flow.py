#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username =="admin" or username =="ADMIN" and password=="12345":
        print("Access granted")
    else: 
        print("Access denied")   
    

def hows_the_weather(temperature):
    if temperature < 40:
        print("brisk")
    elif temperature >=40 and temperature<=65:
        print("a little chilly")
    elif temperature >85:
        print("too dang hot")
    else : 
        print("perfect")


    # your code here
    

def fizzbuzz(num):
    if num  %3==0 and num %5==0:
        print("FizzBuzz")
    elif num  %3==0:
        print("Fizz")
    elif num %5==0:
        print("Buzz")
    else:
        print(num) 
    
    

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

    
