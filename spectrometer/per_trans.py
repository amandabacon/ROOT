#!/usr/bin/python3

def division(x, y):
    return x / y

def average(x, y):
    return x + y

def double_ratio(x, y, r, t):
    return ((x / y) / (r / t))

print("Select operation.")
print("1. Division")
print("2. Average")
print("3. Double Ratio")

choice = input("Enter choice 1, 2, or 3: ")

if choice == '1':
    num1 = float(input("Enter first number (filter/no filter): "))
    num2 = float(input("Enter second number (dir/refl): "))
    print(num1,"/",num2,"=",division(num1,num2))
    print(division(num1,num2)*100)

if choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1,"+",num2,"=",average(num1,num2))
    print(average(num1,num2)/2)

if choice == '3':
    num1 = float(input("Enter first number (dir/refl): "))
    num2 = float(input("Enter second number (norm): "))
    num3 = float(input("Enter third number (dir/refl): "))
    num4 = float(input("Enter fourth number (norm): "))
    print("(",num1,"/",num2,")","/","(",num3,"/",num4,")","=",double_ratio(num1,num2,num3,num4))
    print(double_ratio(num1,num2,num3,num4)*100)
