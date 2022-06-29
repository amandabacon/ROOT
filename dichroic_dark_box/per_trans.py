#!/usr/bin/python3

def double_ratio(x, y, r, t):
    return ((x / y) / (r / t))

num1 = float(input("Enter first number (dir/refl): "))
num2 = float(input("Enter second number (norm): "))
num3 = float(input("Enter third number (dir/refl): "))
num4 = float(input("Enter fourth number (norm): "))
print("(",num1,"/",num2,")","/","(",num3,"/",num4,")","=",double_ratio(num1,num2,num3,num4))
print(double_ratio(num1,num2,num3,num4)*100)
