#Capstone project 1
import math

#Ask user which calculation they want to do
choice = input("Choose either 'investment' or 'bond' from the menu below to poceed:\n\ninvestment\t- to calculate the amount of interest you'll earn on interest\nbond\t\t- to calculate the amount you'll have to pay on a home loan\n")

#Check if input is valid
if (choice.lower() != 'bond' and choice.lower() != 'investment'):
    print("Invalid choice")

if choice.lower() == 'investment':
    #Calculate interest on investment using parameters from user
    p = float(input("Please enter the amount of money you are depositing: "))
    r = float(input("Please enter the interest rate, only the number, as a percentage: "))
    t = float(input("How many years do you plan on investing for: "))
    interest = input("Please make a choice between simple or compound interest - enter 'simple' or 'compund': ")
    if interest.lower() == 'simple':
        a = p*(1 + float(r)/100*t)
        print("After " + str(t) + " years the investment will be worth R" + str(round(a, 2)))
    elif interest.lower() == 'compound':
        a = p*math.pow((1 + float(r)/100), t)
        print("After " + str(t) + " years the investment will be worth R" + str(round(a, 2)))
    else:
        print("Invalid input")
elif choice.lower() == 'bond':
    #Calculate monthly payment on home loan using parameters from user
    p = float(input("Please enter the present value of the house: "))
    i = float(input("Please enter the interest rate, only the number, as a percentage: "))
    n = float(input("Please enter the number of months over which you plan to pay the loan: "))
    x = (p*((float(i))/100)/12)/(1 - (1 + ((float(i))/100)/12)**(-float(n)))
    print("Your monthly payment will be R" + str(round(x, 2)))
