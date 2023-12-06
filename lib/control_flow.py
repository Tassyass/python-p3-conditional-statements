#!/usr/bin/env python3

def admin_login(username, password):
   password= "12345"
print(f"Access granted")

def hows_the_weather(temperature):
   if temperature == "33":
      print(f"Brisk !")
   if temperature == "99":
      print (f"Too dang hot")
   if temperature == "75":
      print (f"Perfect !")
         
hows_the_weather("33")

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print (f"FizzBuzz")
    if num % 3 == 0 :
         print (f"Fizz")
    if num % 5 == 0 :
        print (f"Buzz") 

fizzbuzz(9)           

def calculator(operation, num1, num2):
    if operation == "+":
      print(num1 + num2)
    if operation == "-":
       print(num1 - num2)
    if operation == "*":
        print(num1 * num2)
    if operation == "/":
        print(num1 / num2)

calculator("+", 2, 5)                      