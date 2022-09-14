# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:34:39 2022

@author: Ilya
"""

balance = 999999
annualInterestRate = 0.18

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

def sign_function(x):
    """
    Parameters
    ----------
    x : float или int
        число, знак которого необходимо определить.

    Returns
    -------
    int
        возвращает 1,0 или -1 в зависимости от знака.

    """
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
    
def month_payment(startBalance):
    """
    Calculates fixed payment in order to
    pay off a credit card balance within 12 months
    """
    epsilon = 0.1
    monthInterestRate = annualInterestRate / 12
    lowerPay = balance / 12
    upperPay = (balance * (1 + monthInterestRate)**12) / 12
    
    """
    Реализация алгоритма Bisection
    """
    NMAX = 1000
    N = 0
    while N <= NMAX:
        midPay = (upperPay + lowerPay) / 2.0
        yearBalance = year_credit_card_balance(startBalance, midPay)
        yearBalanceLow = year_credit_card_balance(startBalance, lowerPay)
        checkTol = (upperPay - lowerPay) / 2.0
        if yearBalance == 0 or checkTol < epsilon:
            return round(midPay, 2)
        else:
            N += 1
            if sign_function(yearBalance) == sign_function(yearBalanceLow):
                lowerPay = midPay
            else:
                upperPay = midPay
    return round(midPay, 2) 

print("Lowest Payment: " + str(month_payment(balance)))