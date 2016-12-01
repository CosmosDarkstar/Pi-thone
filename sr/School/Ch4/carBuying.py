'''
Created on Oct 4, 2016

@author: Gab
'''
'''Write a program that helps a person decide
whether to buy a hybrid car. Your program’s
inputs should be:
• The cost of a new car
• The estimated miles driven per year
• The estimated gas price
• The efficiency in miles per gallon
• The estimated resale value after 5 years
Compute the total cost of owning the car for
five years. (For simplicity, we will not take the cost of financing into account.)

Obtain realistic prices for a new and used hybrid and a comparable car from the
Web. Run your program twice, using today’s gas price and 15,000 miles per year.
'''

cost = input("Cost of car")
miles = input("Miles driven per year")
gasPrice = input("Price of gas")
efficiency = input("WHats the MPG")
resale = input("Resale value after 5 years")

yearfFin = (cost + ((miles / efficiency) * gasPrice)) - resale
print(resale)
