#Aman Bilkhoo k21013503
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from mimetypes import init

#Class to represent an Employee for the purposes of calculating pay and providing a string description.
class Employee:

    #Create an employee with a name, contract (can be None), and commision (can be None).
    def __init__(self, name, contract, commission):
        self.name = name
        self.payMethods = []
        if (contract != None): 
            self.payMethods.append(contract);
        if (commission != None):
            self.payMethods.append(commission);

    #Calculate the total pay based on the pay methods provided
    def get_pay(self):
        pay = 0;
        for payMethod in self.payMethods:
            pay += payMethod.getPay();

        return pay

    #Provide a string description of this Employee, including its name, followed by a description of the contract/commision, and the total pay.
    def __str__(self):
        str = f"{self.name} "

        if len(self.payMethods) == 0:
            str += " does not have any associated pay method"
        else:
            str += self.payMethods[0].generateString();

            for i in range(1, len(self.payMethods)):
                str += " and " + self.payMethods[i].generateString();

        return str + f". Their total pay is {self.get_pay()}."

#Abstract class to represent a pay method with only a means to get pay, and to generate a string description.
class PayMethod:
    #Override to calculate pay
    def getPay(self):
        return 0;

    #Override to generate a description.
    def generateString(self):
        return "-";

#Pay method to represent a monthly salary
class SalaryContract(PayMethod):
    def __init__(self, monthlySalary):
        self.monthlySalary = monthlySalary

    def getPay(self):
        return self.monthlySalary 

    def generateString(self):
        return f'works on a monthly salary of {self.monthlySalary}'

#Pay method to represent an hourly contract with the number of hours and the hourly rate
class HourlyContract(PayMethod):
    def __init__(self, numberOfHours, hourlyRate):
        self.numberOfHours = numberOfHours
        self.hourlyRate = hourlyRate

    def getPay(self):
        return self.numberOfHours * self.hourlyRate

    def generateString(self):
        return f'works on a contract of {self.numberOfHours} hours at {self.hourlyRate}/hour'

#Pay method to represent a bonus commision
class BonusCommission(PayMethod):
    def __init__(self, bonusCommissionAmount):
        self.bonusCommissionAmount = bonusCommissionAmount

    def getPay(self):
        return self.bonusCommissionAmount 

    def generateString(self):
        return f'receives a bonus commission of {self.bonusCommissionAmount}'

#Pay method to represent a contract commision with the number of contracts landed and a fixed commision per contract value.
class ContractCommission(PayMethod):
    def __init__(self, numberOfContractsLanded, commissionPerContract):
        self.numberOfContractsLanded = numberOfContractsLanded
        self.commissionPerContract =  commissionPerContract

    def getPay(self):
        return self.numberOfContractsLanded * self.commissionPerContract

    def generateString(self):
        return f'receives a commission for {self.numberOfContractsLanded} contract(s) at {self.commissionPerContract}/contract'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000), None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(100, 25), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120, 30), BonusCommission(600))

