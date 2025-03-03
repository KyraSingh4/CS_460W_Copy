import datetime

class Reservation:
    def __init__(members,guests,court,date,time,weekDay):
        #initialize the members and guests lists
        members = []
        guests = []
        self.members = members
        self.guests = guests
        self.court = court
        self.date = date #datetime date object
        self.time = time #datetime time object
        self.weekDay = weekDay #monday to sunday (0-6)

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
