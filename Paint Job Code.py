# Need to get input for the following float variables:
#square feet of the wall = area
#paint price = fPaintPrice
#ft per gallon of paint = ftPerGallon
#labor hours per gallon = hrsPerGallon
#painting labor charge per hour = hourlyRate

##inputs:##
# Enter wall space in square feet:
#Enter paint price per gallon:
#Enter feet per gallon:
#How many labor hours per gallon:
#Labor charge per hour:
#what state will the job take place in: taxRate
#what is the customers last name: lastName

#program order:
# receive input for wall area, paint price, ft per gallon, labor hours, and hourly labor charge
# receive input for state the job is being completed in, and the customer's last name
# determine how many gallons of paint needed- getGallonsOfPaint = fArea / fFeetPerGal **INT, ROUNDED UP**
# determine how many hours of labor needed to complete the job- getLaborHours = fLaborHours * getGallonsofPaint
# determine the labor cost- getLaborCost = getLaborHours * fHourlyRate
# determine the paint cost- getPaintCost = getGallonsOfPaint * fPaintPrice
# determine the sales tax, if any- getSalesTax = (getLaborCost + getPaintCost) * taxRate
# determine the total cost- showCostEstimate = getLaborCost + getPaintCost + getSalesTax
#output, and code output to a file with lastName input

import math

def getFloatInput(prompt):
    fNum = 0
    while fNum <= 0:
        try:
            fNum = float(input(prompt))
            if fNum <= 0:
                print("Must be a numeric value greater than zero.")
        except ValueError:
            print("Must be a numeric value greater than zero.")
    return fNum


def getGallonsOfPaint(fSquareFootage, fFeetGallons):
    iGallons = math.ceil(fSquareFootage / fFeetGallons)
    return iGallons

def getLaborHours(fHours, fPaintGals):
    fLabor = float(fHours * fPaintGals)
    return fLabor

def getLaborCost(fLaborHours, fHourly):
    fLaborCost = float(fLaborHours * fHourly)
    return fLaborCost

def getPaintCost(fPaintGals, fPrice):
    fPaintCost = float(fPaintGals * fPrice)
    return fPaintCost

def getSalesTax(sState):
    if sState == 'CT' or sState == 'VT':
        fRate = .06
    elif sState == 'MA':
        fRate = .0625
    elif sState == 'ME':
        fRate = .085
    elif sState == 'RI':
        fRate = .07
    else:
        fRate = 0

    return fRate

def showCostEstimate(fLaborCost, fPaintCost, fTaxTotal):
    fCostTotal = float(fLaborCost + fPaintCost + fTaxTotal)
    return fCostTotal

def main():
    #get inputs#
    fArea = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGal = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGal = getFloatInput("How many labor hours per gallon?: ")
    fHourlyRate = getFloatInput("Enter labor charge per hour: ")
    sState = input("What state will the job take place in? ")
    sName = input("What is your last name? ")


    iTotalGallons = getGallonsOfPaint(fArea, fFeetPerGal)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGal, iTotalGallons)
    fLaborCost = getLaborCost(fTotalLaborHours, fHourlyRate)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fTaxRate = getSalesTax(sState)
    fTaxTotal = float((fLaborCost + fPaintCost) * fTaxRate)
    fCostTotal = showCostEstimate(fLaborCost, fPaintCost, fTaxTotal)

#output time and open text file yippee
    outputfile = open(f'{sName}_PaintJobOutput.txt', 'w')
    outputfile.write('')
    print("Gallons of paint: ", iTotalGallons)
    print("Hours of labor: ", fTotalLaborHours)
    print("Paint Charges: ", f"${fPaintCost:,.2f}")
    print("Labor Charges: ", f"${fLaborCost:,.2f}")
    print("Tax: ", f"${fTaxTotal:,.2f}")
    print("Total Cost: ", f"${fCostTotal:,.2f}")
    print((f"File: {outputfile} was created."))
    outputfile.close()


main()

















