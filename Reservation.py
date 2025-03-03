import datetime

class Reservation:
    def __init__(members,guests,court):
        members = []
        guests = []
        self.members = members
        self.guests = guests
        self.court = court
        self.date = datetime.datetime.now()
        self.time = datetime.datetime.now()
        self.weekDay = date.weekday()

    def getDay(self):
        return self.weekDay

    def getTime(self):
        return self.time

    def getDate(self):
        return self.date
    
    def getCourt(self):
        return self.court
    
    def getPrimaryMember(self):
        return self.members[0]

    def getMembers(self):
        return self.members

    def getGuests(self):
        return self.guests

    def updateMembers(self, members):
        self.members = members

    def updateGuests(self, guests):
        self.guests = guests

    def numGuests(self):
        return len(self.guests)
