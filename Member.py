from Bill import Bill


class Member:
    def __init__(self, memberid):
        self.memberid = memberid
        self.my_bill = Bill(self.memberid)
