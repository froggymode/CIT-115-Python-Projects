#code purpose: calculate the interest for each month that a deposit exists in a savings account
#user needs to enter deposit, interest rate %, number of months, and savings goal
#program needs to determine how many months it will take for the original investment to reach the savings goal.
# A = P(1+r/n)**nt
# "A" = final value
# "P" = initial principal value
# "r" = interest rate
# "n" = compound or frequency the interest is applied (monthly, weekly, yearly, etc.)
# "t" = number of time periods elapsed, aka how many months or weeks as referenced above

# 1. get the initial deposit number, make sure it is positive, then continue processing
fDeposit = 0
while fDeposit <= 0:
#make sure the deposit is a number greater than 0!
    try:
        fDeposit = float(input("Enter your original deposit amount (positive value): "))
        if fDeposit <= 0:
            print("You must input a numeric value greater than zero.")
    except ValueError:
        print ("You must input a numeric value greater than zero.")

#find interest rate, ensure it is positive
fRate = 0
while fRate <= 0:
    try:
        fRate = float(input("Enter your interest rate percentage (positive value): "))
        if fRate <= 0:
            print("You must input a numeric value greater than zero.")
    except ValueError:
        print("You must input a numeric value greater than zero.")

#how many months? greater than 0.
iMonths = 0
while iMonths <= 0:
    try:
        iMonths = int(input("Enter the number of months (positive value): "))
        if iMonths <= 0:
            print("You must input a numeric value greater than zero.")
    except ValueError:
        print("You must input a numeric value greater than zero.")

#what is their savings goal? can be greater or equal to 0
fGoal = -1
while fGoal < 0:
    try:
        fGoal = float(input("Enter your goal savings amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print("You must input a numeric value greater than zero.")
    except ValueError:
        print("You must input a numeric value greater than zero.")

#obtain the monthly interest rate. convert the input for fRate to a decimal variable and divide by 12.
#This value is the monthly interest rate.
fMonthlyIntRate = float((fRate/100) / 12)
print(float(fMonthlyIntRate))

#get the interest for the month
#get new account balance, and create variable to do the addition for the months listed
#output the month number and new account balance, formatted as currency!
#"Month:" <month number> "Account Balance is: " <fAcctBalance>

fBalance = fDeposit
for iMonth in range(0, iMonths):
    fMonthlyInt = float(fDeposit * fMonthlyIntRate)
    fDeposit += fMonthlyInt
    print(f"Month: {iMonth + 1} Account Balance is: ${fDeposit:,.2f}")

#find how many months it will take to reach the goal amount. while the balance is less than the goal, keep calculating
#the balance for each month until the balance is >= the goal.
fBalance >= fGoal
iMonthNum = 0
while fBalance < fGoal:
    fMonthlyInt = float(fBalance * fMonthlyIntRate)
    fBalance += fMonthlyInt
    iMonthNum += 1
print(f"It will take: {iMonthNum} months to reach the goal of ${fGoal:,.2f}")







