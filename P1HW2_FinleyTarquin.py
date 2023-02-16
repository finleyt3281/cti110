# This program calculates and displays travel expenses
# 02/16/2023
# CTI-110 P1HW2 - Travel Expense
# Tarquin Finley
#


print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
name = input("Enter your travel destination: ")
print()
gas = float(input("Amount they will spend on gas: "))
print()
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = float(input("Amount they will spend on food: "))
print()
print("------------Travel Expenses------------")
print("Location: ", name)
print("initial budget: ", budget)
print()
print("Fuel: ", gas)
print("Accommodation: ",hotel)
print("Food: ", food)      
print()
balance = budget - gas - food - hotel
#print("Remaining Balance: ", balance)
print("Remaining Balance: ", format(balance,',.0f'))


