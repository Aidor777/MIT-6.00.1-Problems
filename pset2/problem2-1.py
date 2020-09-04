# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:27:45 2019

@author: guill
"""

def cardPayment(balance, annualInterestRate, monthlyPaymentRate):
    """
    int or float balance, float annualInterestRate
    pay off the debt in 12 months
    """
    
    monthlyInterestRate = annualInterestRate/12
    updatedBalance = balance #To not overwrite balance
    
    for nMonths in range(12):
        minimumMonthlyPayment = monthlyPaymentRate*updatedBalance
        monthlyUnpaidBalance = updatedBalance - minimumMonthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        
        print("Month", nMonths+1, "Remaining balance:", round(updatedBalance,2))
        
    return round(updatedBalance,2)

print("Remaining balance:", cardPayment(42,0.2,0.04))
    
    
    