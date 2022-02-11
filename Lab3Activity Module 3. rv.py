Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Roxana Villagomez
#Module 3 Lab Activity

#Problem 1
print("Hello World")
Hello World
#Problem 2
input("Hello, what is your name?")
name=input("Enter your name here:")
print("Hi," +name)      
#Problem 3
if name == "susan" or name == "kelly":
    print('Hello, ' + name)

#Problem 4
if name == "susan" or name == "kelly":
    print('Hello, ' + name)

#Problem 5
miles = float(input("How many miles does the car have?"))
gallons = float(input("How many gallons of gas was used?"))

mpg = (miles / gallons)
print("You used", mpg, "thus far this week.")
                      
print("Sounds good, your car is still running well")
#Problem6
celsius = float(input("Enter temp in celsius:"))
fahrenheit = (celsius*5/9)+2
fahrenheit = round(fahrenheit,2)
print(celsius,'Celsius would be:', fahrenheit,'Fahrenheit')
#Problem 7
day_index= [0,1,2,3,4,5,6]
name_day= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday",
           "Saturday","Sunday"]
print("When are you leaving for the holidays?")
x=input("enter the day number (from 0 to 6):")
y=input("how many nights before you return home?")
z=input(int(x) + int(y)) / 7
print("Your coming back on the day number")
print=(z)

