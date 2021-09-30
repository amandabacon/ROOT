import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

data0 = np.loadtxt('0_deg.txt')
data1 = np.loadtxt('5_deg.txt')
data2 = np.loadtxt('10_deg.txt')
data3 = np.loadtxt('15_deg.txt')
data4 = np.loadtxt('20_deg.txt')
data5 = np.loadtxt('25_deg.txt')
data6 = np.loadtxt('30_deg.txt')
data7 = np.loadtxt('35_deg.txt')
data8 = np.loadtxt('ref.txt')

x0 = data0[:, 0]
y0 = data0[:, 1]
x1 = data1[:, 0]
y1 = data1[:, 1]
x2 = data2[:, 0]
y2 = data2[:, 1]
x3 = data3[:, 0]
y3 = data3[:, 1]
x4 = data4[:, 0]
y4 = data4[:, 1]
x5 = data5[:, 0]
y5 = data5[:, 1]
x6 = data6[:, 0]
y6 = data6[:, 1]
x7 = data7[:, 0]
y7 = data7[:, 1]
x8 = data8[:, 0]
y8 = data8[:, 1]

number = '385.003'
number1 = '405.189'
number2 = '450.178'
number3 = '505.134'
number4 = '525.063'
number5 = '555.022'
number6 = '590.192'

print('0 degrees')
with open('0_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('5 degrees')
with open('5_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('10 degrees')
with open('10_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('15 degrees')
with open('15_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('20 degrees')
with open('20_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('25 degrees')
with open('25_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('30 degrees')
with open('30_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('35 degrees')
with open('35_deg.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('Ref')
with open('ref.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number1:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number2:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number3:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number4:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number5:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

        if data[0] == number6:
            print('Wavelength:', data[0])
            print('Intensity:', data[1])

print('')
print('TEST')
with open('test.txt', "r") as f:
    for row in f:
        data = row.split()
        if data[0] == number:
            print(float(data[0]))
            print(float(data[1]))

        if data[0] == number1:
            print(float(data[0]))
            print(float(data[1]))

        if data[0] == number2:
            print(float(data[0]))
            print(float(data[1]))

        if data[0] == number3:
            print(float(data[0]))
            print(float(data[1]))

        if data[0] == number4:
            print(float(data[0]))
            print(float(data[1]))

        if data[0] == number5:
            print(float(data[0]))
            print(float(data[1]))

        if data[0] == number6:
            print(float(data[0]))
            print(float(data[1]))

print('')
print('test.csv')
data = pd.read_csv("test.csv")
np.array(data.values)
#print(np.array(data.values))
print(number)
print('0 deg')
print(np.array(data.values[973-2][1]))
print('5 deg')
print(np.array(data.values[4621-2][1]))
print('10 deg')
print(np.array(data.values[8269-2][1]))
print('15 deg')
print(np.array(data.values[11917-2][1]))
print('20 deg')
print(np.array(data.values[15565-2][1]))
print('25 deg')
print(np.array(data.values[19213-2][1]))
print('30 deg')
print(np.array(data.values[22861-2][1]))
print('35 deg')
print(np.array(data.values[26509-2][1]))
print('ref')
print(np.array(data.values[30157-2][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[973-2][1])/np.array(data.values[30157-2][1]))*100)
print('5 deg/ref')
print((np.array(data.values[4621-2][1])/np.array(data.values[30157-2][1]))*100)
print('10 deg/ref')
print((np.array(data.values[8269-2][1])/np.array(data.values[30157-2][1]))*100)
print('15 deg/ref')
print((np.array(data.values[11917-2][1])/np.array(data.values[30157-2][1]))*100)
print('20 deg/ref')
print((np.array(data.values[15565-2][1])/np.array(data.values[30157-2][1]))*100)
print('25 deg/ref')
print((np.array(data.values[19213-2][1])/np.array(data.values[30157-2][1]))*100)
print('30 deg/ref')
print((np.array(data.values[22861-2][1])/np.array(data.values[30157-2][1]))*100)
print('35 deg/ref')
print((np.array(data.values[26509-2][1])/np.array(data.values[30157-2][1]))*100)

print('')
print(number1)
print('0 deg')
print(np.array(data.values[1070-2][1]))
print('5 deg')
print(np.array(data.values[4718-2][1]))
print('10 deg')
print(np.array(data.values[8366-2][1]))
print('15 deg')
print(np.array(data.values[12014-2][1]))
print('20 deg')
print(np.array(data.values[15662-2][1]))
print('25 deg')
print(np.array(data.values[19310-2][1]))
print('30 deg')
print(np.array(data.values[22958-2][1]))
print('35 deg')
print(np.array(data.values[26606-2][1]))
print('ref')
print(np.array(data.values[30254-2][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[1070-2][1])/np.array(data.values[30254-2][1]))*100)
print('5 deg/ref')
print((np.array(data.values[4718-2][1])/np.array(data.values[30254-2][1]))*100)
print('10 deg/ref')
print((np.array(data.values[8366-2][1])/np.array(data.values[30254-2][1]))*100)
print('15 deg/ref')
print((np.array(data.values[12014-2][1])/np.array(data.values[30254-2][1]))*100)
print('20 deg/ref')
print((np.array(data.values[15662-2][1])/np.array(data.values[30254-2][1]))*100)
print('25 deg/ref')
print((np.array(data.values[19310-2][1])/np.array(data.values[30254-2][1]))*100)
print('30 deg/ref')
print((np.array(data.values[22958-2][1])/np.array(data.values[30254-2][1]))*100)
print('35 deg/ref')
print((np.array(data.values[26606-2][1])/np.array(data.values[30254-2][1]))*100)

print('')
print(number2)
print('0 deg')
print(np.array(data.values[(1070-2)+218][1]))
print('5 deg')
print(np.array(data.values[(4718-2)+218][1]))
print('10 deg')
print(np.array(data.values[(8366-2)+218][1]))
print('15 deg')
print(np.array(data.values[(12014-2)+218][1]))
print('20 deg')
print(np.array(data.values[(15662-2)+218][1]))
print('25 deg')
print(np.array(data.values[(19310-2)+218][1]))
print('30 deg')
print(np.array(data.values[(22958-2)+218][1]))
print('35 deg')
print(np.array(data.values[(26606-2)+218][1]))
print('ref')
print(np.array(data.values[(30254-2)+218][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[(1070-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('5 deg/ref')
print((np.array(data.values[(4718-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('10 deg/ref')
print((np.array(data.values[(8366-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('15 deg/ref')
print((np.array(data.values[(12014-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('20 deg/ref')
print((np.array(data.values[(15662-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('25 deg/ref')
print((np.array(data.values[(19310-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('30 deg/ref')
print((np.array(data.values[(22958-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)
print('35 deg/ref')
print((np.array(data.values[(26606-2)+218][1])/np.array(data.values[(30254-2)+218][1]))*100)

print('')
print(number3)
print('0 deg')
print(np.array(data.values[(1070-2)+488][1]))
print('5 deg')
print(np.array(data.values[(4718-2)+488][1]))
print('10 deg')
print(np.array(data.values[(8366-2)+488][1]))
print('15 deg')
print(np.array(data.values[(12014-2)+488][1]))
print('20 deg')
print(np.array(data.values[(15662-2)+488][1]))
print('25 deg')
print(np.array(data.values[(19310-2)+488][1]))
print('30 deg')
print(np.array(data.values[(22958-2)+488][1]))
print('35 deg')
print(np.array(data.values[(26606-2)+488][1]))
print('ref')
print(np.array(data.values[(30254-2)+488][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[(1070-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('5 deg/ref')
print((np.array(data.values[(4718-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('10 deg/ref')
print((np.array(data.values[(8366-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('15 deg/ref')
print((np.array(data.values[(12014-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('20 deg/ref')
print((np.array(data.values[(15662-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('25 deg/ref')
print((np.array(data.values[(19310-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('30 deg/ref')
print((np.array(data.values[(22958-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)
print('35 deg/ref')
print((np.array(data.values[(26606-2)+488][1])/np.array(data.values[(30254-2)+488][1]))*100)

print('')
print(number4)
print('0 deg')
print(np.array(data.values[(1070-2)+587][1]))
print('5 deg')
print(np.array(data.values[(4718-2)+587][1]))
print('10 deg')
print(np.array(data.values[(8366-2)+587][1]))
print('15 deg')
print(np.array(data.values[(12014-2)+587][1]))
print('20 deg')
print(np.array(data.values[(15662-2)+587][1]))
print('25 deg')
print(np.array(data.values[(19310-2)+587][1]))
print('30 deg')
print(np.array(data.values[(22958-2)+587][1]))
print('35 deg')
print(np.array(data.values[(26606-2)+587][1]))
print('ref')
print(np.array(data.values[(30254-2)+587][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[(1070-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('5 deg/ref')
print((np.array(data.values[(4718-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('10 deg/ref')
print((np.array(data.values[(8366-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('15 deg/ref')
print((np.array(data.values[(12014-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('20 deg/ref')
print((np.array(data.values[(15662-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('25 deg/ref')
print((np.array(data.values[(19310-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('30 deg/ref')
print((np.array(data.values[(22958-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)
print('35 deg/ref')
print((np.array(data.values[(26606-2)+587][1])/np.array(data.values[(30254-2)+587][1]))*100)

print('')
print(number5)
print('0 deg')
print(np.array(data.values[(1070-2)+737][1]))
print('5 deg')
print(np.array(data.values[(4718-2)+737][1]))
print('10 deg')
print(np.array(data.values[(8366-2)+737][1]))
print('15 deg')
print(np.array(data.values[(12014-2)+737][1]))
print('20 deg')
print(np.array(data.values[(15662-2)+737][1]))
print('25 deg')
print(np.array(data.values[(19310-2)+737][1]))
print('30 deg')
print(np.array(data.values[(22958-2)+737][1]))
print('35 deg')
print(np.array(data.values[(26606-2)+737][1]))
print('ref')
print(np.array(data.values[(30254-2)+737][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[(1070-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('5 deg/ref')
print((np.array(data.values[(4718-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('10 deg/ref')
print((np.array(data.values[(8366-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('15 deg/ref')
print((np.array(data.values[(12014-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('20 deg/ref')
print((np.array(data.values[(15662-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('25 deg/ref')
print((np.array(data.values[(19310-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('30 deg/ref')
print((np.array(data.values[(22958-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)
print('35 deg/ref')
print((np.array(data.values[(26606-2)+737][1])/np.array(data.values[(30254-2)+737][1]))*100)

print('')
print(number6)
print('0 deg')
print(np.array(data.values[(1070-2)+915][1]))
print('5 deg')
print(np.array(data.values[(4718-2)+915][1]))
print('10 deg')
print(np.array(data.values[(8366-2)+915][1]))
print('15 deg')
print(np.array(data.values[(12014-2)+915][1]))
print('20 deg')
print(np.array(data.values[(15662-2)+915][1]))
print('25 deg')
print(np.array(data.values[(19310-2)+915][1]))
print('30 deg')
print(np.array(data.values[(22958-2)+915][1]))
print('35 deg')
print(np.array(data.values[(26606-2)+915][1]))
print('ref')
print(np.array(data.values[(30254-2)+915][1]))

print('')
print('0 deg/ref')
print((np.array(data.values[(1070-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('5 deg/ref')
print((np.array(data.values[(4718-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('10 deg/ref')
print((np.array(data.values[(8366-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('15 deg/ref')
print((np.array(data.values[(12014-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('20 deg/ref')
print((np.array(data.values[(15662-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('25 deg/ref')
print((np.array(data.values[(19310-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('30 deg/ref')
print((np.array(data.values[(22958-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)
print('35 deg/ref')
print((np.array(data.values[(26606-2)+915][1])/np.array(data.values[(30254-2)+915][1]))*100)

# All wavelengths and not a select few
#print("y0", y0)
#print("y9", y9)
#c = y0/y9
#print(c)
#d = c*100
#print(d)

plt.figure()
plt.plot(x0, y0, 'r--')
plt.title('0 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('0_deg')

plt.figure()
plt.plot(x1, y1, 'r--')
plt.title('5 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('5_deg')

plt.figure()
plt.plot(x2, y2, 'r--')
plt.title('10 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('10_deg')

plt.figure()
plt.plot(x3, y3, 'r--')
plt.title('15 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('15_deg')

plt.figure()
plt.plot(x4, y4, 'r--')
plt.title('20 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('20_deg')

plt.figure()
plt.plot(x5, y5, 'r--')
plt.title('25 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('25_deg')

plt.figure()
plt.plot(x6, y6, 'r--')
plt.title('30 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('30_deg')

plt.figure()
plt.plot(x7, y7, 'r--')
plt.title('35 degrees')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
#plt.savefig('35_deg')

#plt.show()
