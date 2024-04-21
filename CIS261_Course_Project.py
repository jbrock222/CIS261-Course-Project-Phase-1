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
totalEmployees = 0
totalGrossPay = 0
totalHoursWorked = 0
totalIncomeTaxes = 0
totalNetPay = 0

def enterName():
    global employeeName
    global totalEmployees
    employeeName = input("Enter the Employee's Name: ")
    if employeeName.lower() == "end":
        print("Number of Employees: " + str(totalEmployees))
        print("Total Hours Worked: " + str(totalHoursWorked) + " hours")
        print("Total Gross Pay: $" + str(totalGrossPay))
        print("Total Income Taxes: $" + str(totalIncomeTaxes))
        print("Total Net Pay: $" + str(totalNetPay))
        exit()
        
    else:
        totalEmployees = totalEmployees + 1

def enterHours():
    global totalHours
    global totalHoursWorked
    totalHours = float(input("Enter total hours worked: "))
    totalHoursWorked = totalHoursWorked + totalHours

def enterHourlyRate():
    global hourlyRate
    hourlyRate = float(input("Enter " + employeeName + "'s hourly rate: "))
    
def enterTaxRate():
    global taxRate
    taxRate = float(input("Enter the tax rate: "))
    
def calculate():
    global employeeName
    global totalHours
    global hourlyRate 
    global taxRate
    global totalGrossPay
    global totalIncomeTaxes
    global totalNetPay
    grossPay = totalHours * hourlyRate
    totalGrossPay = totalGrossPay + grossPay
    totalIncomeTaxes = totalIncomeTaxes + (totalHours * hourlyRate) * taxRate
    totalNetPay = totalNetPay + (grossPay - grossPay * taxRate)
    print(employeeName)
    print("Hours Worked: " + str(totalHours))
    print("Hourly Rate: " + str(hourlyRate))
    print("Gross Pay: $" + str(totalHours * hourlyRate)) 
    print("Income Tax Rate: " + str(taxRate))
    print("Income Taxes: " + str((totalHours * hourlyRate) * taxRate))
    print("Net Pay: $" + str(grossPay - grossPay * taxRate))
    
    
functions = [enterName, enterHours, enterHourlyRate, enterTaxRate, calculate]

while 1 == 1:
    for f in functions:
        result = f()

