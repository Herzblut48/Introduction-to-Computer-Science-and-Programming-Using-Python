# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:04:22 2022

@author: Ilya
"""

balance = 4773
annualInterestRate = 0.2

def credit_card_balance(b, aInterest, mPayment):
    """
    Calculates credit card balance
    """
    
    unBalance = b - mPayment
    balance = unBalance + aInterest/12 * unBalance
    return balance

def year_credit_card_balance(startBalance, mPayment):
    """
    Calculates credit card balance 
    at the end of year with fixed payment
    """
    b = startBalance
    for m in range(12):
        b = credit_card_balance(b,
                                annualInterestRate,mPayment)
    return round(b, 2)

def month_payment(startBalance):
    """
    Calculates fixed payment in order to
    pay off a credit card balance within 12 months
    """
    p = 10
    yearBalance = year_credit_card_balance(startBalance, p)
    while yearBalance > 0:
        p += 10
        yearBalance = year_credit_card_balance(startBalance, p)
 
    return p   

print("Lowest Payment: " + str(month_payment(balance)))

