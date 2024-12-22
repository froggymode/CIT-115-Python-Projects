#code objective: a real estate company has asked us to design a sales analyzer program for real estate sales.
#Use a list- enter the property sales by entering a valid sales dollar amount repeatedly, until the user says
#no to more input.

#receive a string as a parameter to be used as the prompt input text and it returns a float
#MAKE SURE inputs are non-zero, positive, numeric values- create an error message and ask for input again if not.
def getFloatInput(prompt):
    fNum = 0
    while fNum <= 0:
        try:
            fNum = float(input(prompt))
            if fNum <= 0:
                print("Please input a number greater than zero.")
        except ValueError:
            print("Please input a number greater than zero.")
    return fNum

#create a function called getMedian that receives a LIST and returns a FLOAT.
#if number of list entries is odd= divide the count by 2 and use that entry as the median
#if the number of entries in the list is even, divide the count by 2. use the avg of that entry and the one
#before it to use as the median. use modulus operation to determine odd or even.
#determine the length (len) of the list- is there an odd or even number of elements? REMEMBER the first index
#is 0, not 1.
#need to sort the list from lowest to highest first!
def getMedian(sales_list):
    sales_list.sort()
    iEntries = len(sales_list)
    if iEntries % 2 !=0:
        return float(sales_list[iEntries // 2])
    else:
        iMiddle1 = iEntries // 2
        iMiddle2 = iMiddle1 - 1
        return float((sales_list[iMiddle1] + sales_list[iMiddle2]) / 2)

#code a main function! use a list to store the inputted sales values, call getFloatInput and add to the list
#using the append method. create a loop because we don't know how many values will be entered. make sure they enter a
#Y on an N and gives an error if they enter something else.
def main():
    sales_list = []
    keep_going = 'Y'
    while True:
        try:
            sales_price = getFloatInput("Enter property sales value: ")
            sales_list.append(sales_price)
            keep_going = input("Would you like to enter another value? Please type Y for yes, or N for no: ").lower()
            if keep_going == 'n':
                break
            elif keep_going != 'y':
                print("Error. Please enter a Y or an N.")
                keep_going = input("Would you like to enter another value? Please type Y for yes, or N for no: ").lower()
                if keep_going == 'n':
                    break
        except ValueError:
            print("error")


#sort the list from smallest to largest with the .sort() method
    sales_list.sort()
#now for output. first, output the sorted list formatted as $ with 2 dec points, labeled as property number
    print("Here are your property sales in order of lowest to highest:")
    iProperty = 1
    for saleAmount in sales_list:
        print(f"Property #{iProperty}: ${saleAmount:,.2f}")
        iProperty += 1
#output the minimum, maximum, total, average, median, and commission.
#for commission- multiply the TOTAL by .03, output as currency w/ 2 dec points
    fMinimum = sales_list[0]
    fMaximum = sales_list[-1]
    fTotal = sum(sales_list)
    fAverage = fTotal / len(sales_list)
    fMedian = getMedian(sales_list)
    fCommission = fTotal * .03

    print(f"Minimum: ${fMinimum:,.2f}")
    print(f"Maximum: ${fMaximum:,.2f}")
    print(f"Total: ${fTotal:,.2f}")
    print(f"Average: ${fAverage:,.2f}")
    print(f"Median: ${fMedian:,.2f}")
    print(f"Commission: ${fCommission:,.2f}")

main()










