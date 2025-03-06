import datetime

class Charge:
    def __init__(self, value: float,memo: str,type: str):
        self.value = value
        self.date = datetime.datetime.now()
        self.memo = memo
        self.type = type

    def getCharge(self):
        return self.value, self.date, self.memo, self.type

    def getValue(self):
        return self.value
