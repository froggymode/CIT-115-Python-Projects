# Create a program that allows for numeric entry of a temperature that can be converted to Celsius or Fahrenheit.
# 1. Write a welcome message with my name
print ("Hi there! My name is Cassidy, and this is my temperature converter code. Enjoy!")
# 2. Prompt the user for a temperature
fTemp = float(input("Please enter a temperature: "))
# 3. Ask the user if the temp that was entered is F/f for Fahrenheit or C/c for Celsius
sInput = input ("Great! Is the temperature F for Fahrenheit, or C for Celsius? ")
# 4. If the user entered F, we need to convert it to C. If the user entered C, we need to convert it to F. If the user
# entered something other than C or F, we need to display "Enter an F or a C".
if sInput == 'F' or sInput == 'f':
    if fTemp > 212:
        print ("Temp cannot be > 212")
    else:
        fConversion = ((5.0 / 9.0) * (fTemp - 32))
        print ("The Celsius equivalent is " +format(fConversion,'.1f'))

elif sInput == 'C' or sInput == 'c':
    if fTemp > 100:
        print ("Temp cannot be > 100")
    else:
        fConversion = ((9.0 / 5.0) * fTemp) + 32
        print ("The Fahrenheit equivalent is " +format(fConversion,'.1f'))
else:
    print ("Enter an F or a C.")








