import Charge
import datetime

class Bill:
    def __init__(self):
        self.charges = []
        self.isPaid = False

    def isPaid(self):
        return self.isPaid

    def getTotal(self):
        total = 0
        for i in range(len(self.charges)):
            total += self.charges[i].getValue()
        return total

    def createCharge(self, value: float, memo: str, type: str):
        charge = Charge.Charge(value, memo, type)
        self.charges.append(charge)

    def getBill(self):
        