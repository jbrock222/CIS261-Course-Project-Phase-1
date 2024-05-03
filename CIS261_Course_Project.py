'''
Joshua Brock
CIS261
Course Project Phase 1
'''
def getEmpName():
        empName = input("Enter Employee Name: ")
        return empName

def getHoursWorked():
        hours = float(input("Enter Hours Worked: "))
        return hours

def getHourlyRate():
        hourlyRate = float(input("Enter Hourly Rate: "))
        return hourlyRate
def getTaxRate():
        taxRate = float(input("Enter Tax rate: "))
        taxRate = taxRate / 100
        return taxRate

def calcTaxAndNetPay(hours, hourlyRate, taxRate):
        gpay = hours * hourlyRate
        incomeTax = gpay * taxRate
        netPay = gpay - incomeTax
        return gpay, incomeTax, netPay

def printinfo(empName, hours, hourlyRate, gpay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gpay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
    

