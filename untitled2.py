# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 08:34:47 2022

@author: Ilya
"""

balance = 42 #the outstanding balance on the credit card
annualInterestRate = 0.2 #annual interest rate as a decimal
monthlyPaymentRate = 0.04 #minimum monthly payment rate as a decimal

def credit_card_balance(b = balance, 
                        aInterest = annualInterestRate,
                        mPaymentRate = monthlyPaymentRate) :
    """
    Calculates credit card balance
    """
    
    payment = b * mPaymentRate
    unBalance = b - payment
    balance = unBalance + aInterest/12 * unBalance
    return balance
    
def year_credit_card_balance(balance):
    """
    Calculates credit card balance 
    in the end of year
    """
    b = balance
    for m in range(12):
        b = credit_card_balance(b)
    return round(b, 2)

print("Remaining balance: " + str(year_credit_card_balance(balance)))