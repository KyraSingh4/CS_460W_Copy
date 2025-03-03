import datetime

class Calender:
    def __init__():
        reservations_sunday = []
        reservations_monday = []
        reservations_tuesday = []
        reservations_wednesday = []
        reservations_thursday = []
        reservations_friday = []
        reservations_saturday = []
        self.reservations = {
            0: reservations_sunday,
            1: reservations_monday,
            2: reservations_tuesday,
            3: reservations_wednesday,
            4: reservations_thursday,
            5: reservations_friday,
            6: reservations_saturday
        }
        self.date = datetime.datetime.now()
        self.weekDay = date.weekday()
    
    def getReservations(self, weekDay, court):
        matching_reservations = []
        for reservation in self.reservations[weekDay]:
            if reservation.getCourt() == court:
                matching_reservations.append(reservation)
        sortByTime(matching_reservations)
        # Sort the reservations by time
        return matching_reservations
    
    def sortByTime(self, reservations):
        return sorted(reservations, key=lambda x: x.getTime())
    
    def addReservation(self, reservation, weekDay):
        self.reservations[weekDay].append(reservation)

    def getDay(self):
        return self.weekDay
    
    def getDate(self):
        return self.date
    
    def updateDate(self, date):
        self.date = datetime.datetime.now()
        self.weekDay = date.weekday()
        self.reservations[weekDay] = []
