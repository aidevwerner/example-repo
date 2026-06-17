import math

#the user first needs to choose between a investment or bond 

print ("Investment - to calculate the amount of interest you'll earn on your investment.")
print (" Bond - to calculate the amount you'll have to pay on a home loan.")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()

# below is if-elif-else statements that directs the user based on his input. first it is the selection of investment and then the investment options or bond as options.

if choice == "investment":
    deposit = float(input("How much money do you want to deposit?"))
    interest_rate = float(input("Enter your interest rate as number? (e.g. 8 for 8%)")) / 100
    years = int(input("Number of years you want to invest?"))
    interest = input("Do you want 'simple' or 'compound' interest?").lower().strip()

    if interest == "simple":
        total_simple = deposit * (1 + interest_rate * years)
        print("The total simple interest earned is {}.".format(total_simple))
    
    elif interest == "compound":
        total_compound = deposit * math.pow((1 + interest_rate),years)
        print("The total compound interest earned is {}.".format(total_compound))
    
    else:
        print ("Invalid input. Input either 'simple' or 'compound'.")

#below bond input is asked and bond caculation executed. 

elif choice == "bond":
    house_value = int(input("What is the present value of your house?"))
    interest_rate2 = float(input("What is the interest rate of the bond? (e.g. 8 for 8%)")) / 100
    repayment_months = int(input("In how many months are you planning to repay?"))
    
    monthly_interest = interest_rate2 / 12
    repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest)**(-repayment_months))
    print("The monthly repayment amount is {}".format(repayment))
    
#if wrong initial input then the following statement is printed/displayed. 
    
else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")
    
