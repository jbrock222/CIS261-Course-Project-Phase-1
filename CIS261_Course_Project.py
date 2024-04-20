'''
Joshua Brock
CIS261
Course Project Phase 1
'''

index = 0
employeeName = " "
totalHours = 0
hourlyRate = 0
taxRate = 0

def enterName():
    global employeeName
    print("enter employee name")

def enterHours():
    global totalHours
    print("enter total hours")

def enterHourlyRate():
    global hourlyRate
    print("enter hourly rate")
    
def enterTaxRate():
    global taxRate
    print("enter tax rate")
    
def calculate():
    print("calculate")
    
functions = [enterName, enterHours, enterHourlyRate, enterTaxRate, calculate]

for f in functions:
    result = f()

