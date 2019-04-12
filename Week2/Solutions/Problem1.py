# -*- coding: utf-8 -*-

#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
	      # Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print"Remaining balance:", round(balance, 2)
