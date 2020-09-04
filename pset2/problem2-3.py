# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:53:57 2019

@author: guill
"""

def fasterPayCardPayment(balance, annualInterestRate):
    """
    int or float balance, float annualInterestRate
    pay off the debt in 12 months
    lowest possible payment to the cent
    """
    
    monthlyInterestRate = annualInterestRate/12
    updatedBalance = balance #To not overwrite balance
    
    #Use the bisection search algorithm
    lower = balance/12 #lowest possible monthly payment if no interests
    upper = (balance*(1+monthlyInterestRate)**12)/12 #payment if everything is paid at the end of the 12 months
    monthlyPayment = (lower + upper)/2 #guess the first monthly payment
    
    while abs(updatedBalance) > 0.005:
        updatedBalance = balance
        for nMonths in range(12):
            monthlyUnpaidBalance = updatedBalance - monthlyPayment
            updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        if updatedBalance > 0.005: #didnt pay enough
            lower = monthlyPayment
            monthlyPayment = (lower + upper)/2
        elif updatedBalance < 0.005: #paid too much
            upper = monthlyPayment
            monthlyPayment = (lower + upper)/2
        else:
            break
    
    return round(monthlyPayment,2)

print("Lowest payment:", fasterPayCardPayment(999999,0.18))
    
            
            
            
            
            
            
            
            