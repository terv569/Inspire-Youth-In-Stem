#!/usr/bin/env python3


# Python programmer to caclulate gross and net income
# Name : Tervil Moywaywa
# Email : tervilmoywaywa@gmail.com
# Date : 20th Feb 2023
# File : bank.py

# write a program that calculates 16% tax on income
# rangig between 100k---150k


#19% tax if income is between 150k----300k
# 30% tax income is above 300k
# 5% if income is less 100k

# print gross income , net income

income = input("enter your net income:")

income = int(input("Enter your income: "))

if income <= 100000:
    net_income = income*0.95
if income <  300000:
    net_income = income*0.81
else:
    net_income = income*0.7
print("Gross income: " + str(income) + " Net income: " + str(net_income))



