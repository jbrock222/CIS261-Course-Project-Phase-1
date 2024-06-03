'''
Joshua Brock
CIS261
Course Project Phase 3
'''

from os import write
from datetime import datetime

def CreateUsers():
    print("Create users, passwords, and roles")
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter a username or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter a password: ")
    return pwd

def GetUserRole():
     userrole = input("Enter a role (Admin or User): ")
     while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER")
            return userrole
        else: userrole = input("Enter a role(Admin or User): ")
        
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break 
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)
        
def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter username: ")
    UserPwd = input("Enter password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
            UserRole = UserList[2]
            return UserRole, UserName
        
    return UserRole, UserName
        

          

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
    EmpFile = open("Employees.txt:, "r")
    while True:
        rundate = input("Enter start date for report (mm/dd/yyy): ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.striptime(rundate, %m/%d/$Y)
            break
        except ValueError:
            print("Invalid date format. Try again. ")
            print()
            continue
    while True:
    EmpDetail = EmpFile.readline()
    if not EmpDetail:
        break
    
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
       
def WriteEmployeeInformation(employee):
        file = open("employeeinfo.txt", "a")  
        file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def GetFromDate():
    valid = False
    fromdate = ""
    
    while not valid:
        fromdate = input("Enter from date (mm/dd/yyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid date format")
        else:
            valid = True
            
    return fromdate

def ReadEmployeeInformation(fromdate):
    empDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    
    if fromdate.upper() == 'ALL':
        condition = False
        
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        
        if not condition:
            empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
            
        else:
            if fromdate == employee[0]:
                empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
              
    return empDetailList
            
if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        fromdate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        
        print()
        
        empDetail = [fromdate, endDate, empName, hours, hourlyRate, taxRate]
        WriteEmployeeInformation(empDetail)
        
    print()
    print()
    fromdate = GetFromDate()
    
    empDetailList = ReadEmployeeInformation(fromdate)
    
    print()
    printInfo(empDetailList)
    print()
    PrintTotals(empTotals)
               