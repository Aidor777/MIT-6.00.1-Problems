# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:27:45 2019

@author: guill
"""

def payCardPayment(balance, annualInterestRate):
    """
    int or float balance, float annualInterestRate
    pay off the debt in 12 months
    payments in multiples of 10$
    """
    
    monthlyInterestRate = annualInterestRate/12
    updatedBalance = balance #To not overwrite balance
    monthlyPayment = 10 #Start by guessing a monthly payment of 10$
    
    while updatedBalance > 0:
        updatedBalance = balance
        for nMonths in range(12):
            monthlyUnpaidBalance = updatedBalance - monthlyPayment
            updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        monthlyPayment += 10
        
    finalMonthlyPayment = monthlyPayment - 10
    return finalMonthlyPayment

print("Lowest payment:", payCardPayment(3926,0.2))
    
    
    