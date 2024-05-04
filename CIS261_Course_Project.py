'''
Joshua Brock
CIS261
Course Project Phase 2
'''

def getDatesWorked():
        fromDate = input("Please enter start date in the following format MM/DD/YY: ")
        endDate = input("Please enter the end date in the following format MM/DD/YY: ")
        return fromDate, endDate
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

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
        gpay = hours * hourlyRate
        incomeTax = gpay * taxRate
        netPay = gpay - incomeTax
        return gpay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay
        
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totNet"] = totalNetPay
        empTotals["totTax"] = totalTax

def PrintTotals(empTotals):
       print(f"Total number of Employees:   {empTotals['totEmp']}")
       print(f"Total hours of the Employees: {empTotals['totHours']}")
       print(f"Total Gross Pay of the Employees: {empTotals['totGross']}")
       print(f"Total tax of Employees:  {empTotals['totTax']}")
       print(f"Total net pay of employees:  {empTotals['totNet']}")
       
if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
    printInfo(empDetailList)
    PrintTotals(empTotals)        