import datetime
import csv

import psycopg2


class Calendar:
    def __init__(self):
        pass

    def RetrieveDay(self,day):
        if day < 0 or day > 6:
            return None
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT reservation_id, court_num, start_time, end_time, member_id, type FROM reservation WHERE res_day = %s", (day,))
                return cur.fetchall()

    def lookupReservation(self, res_id: int):
        result = None
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT res_day, court_num, start_time, end_time, type, member_id FROM reservation WHERE reservation_id = %s", (res_id,))
                result = cur.fetchall()
                if not result:  # If no rows are returned
                    return None
        return result

    def getAttendees(self, res_id: int):
        result = []
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT member_id FROM reservation WHERE reservation_id = %s", (res_id,))
                mem_id_result = cur.fetchall()
                if not mem_id_result:
                    return None  # Return None if the reservation does not exist
                mem_id = mem_id_result[0][0]

            with conn.cursor() as cur:
                cur.execute("SELECT firstname, lastname FROM member WHERE member_id = %s", (mem_id,))
                result = cur.fetchall()

            with conn.cursor() as cur:
                cur.execute("SELECT firstname, lastname FROM attendees WHERE reservation_id = %s", (res_id,))
                others = cur.fetchall()
                result.extend(others)

        return result

class Calender2: #unused
    def __init__(self):
        reservations_sunday = []
        reservations_monday = []
        reservations_tuesday = []
        reservations_wednesday = []
        reservations_thursday = []
        reservations_friday = []
        reservations_saturday = []
        self.reservations = {
            0: reservations_monday,
            1: reservations_tuesday,
            2: reservations_wednesday,
            3: reservations_thursday,
            4: reservations_friday,
            5: reservations_saturday,
            6: reservations_sunday
        }
        self.date = datetime.datetime.now()
        self.weekDay = self.date.weekday()
    
    def getReservations(self, weekDay, court): #gets reservation for a specific court on a specific day
        matching_reservations = []
        for reservation in self.reservations[weekDay]:
            if reservation.getCourt() == court:
                matching_reservations.append(reservation)
        self.sortByTime(matching_reservations)
        # Sort the reservations by time
        return matching_reservations
    
    def sortByTime(self, reservations): #sorts a list of reservations by time
        return sorted(reservations, key=lambda x: x.getTime())
    
    def addReservation(self, reservation, weekDay): #adds a reservation to the list of reservations for a specific day
        self.reservations[weekDay].append(reservation)

    def getDay(self):
        return self.weekDay
    
    def getDate(self):
        return self.date
    
    def updateDate(self, date):
        self.date = datetime.datetime.now()
        self.reservations[self.weekDay] = []
        self.weekDay = date.weekday()

    def saveToCSV(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['WeekDay', 'Court', 'Date', 'Time', 'Members', 'Guests'])
            for weekDay, reservations in self.reservations.items():
                for reservation in reservations:
                    writer.writerow([
                        weekDay,
                        reservation.getCourt(),
                        reservation.getDate().isoformat(),
                        reservation.getTime().isoformat(),
                        ','.join(reservation.getMembers()),
                        ','.join(reservation.getGuests())
                    ])

    def loadFromCSV(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                weekDay = int(row[0])
                court = row[1]
                date = datetime.datetime.fromisoformat(row[2])
                time = datetime.time.fromisoformat(row[3])
                members = row[4].split(',')
                guests = row[5].split(',')
                reservation = Reservation(members, guests, court, date, time, weekDay)
                self.addReservation(reservation, weekDay)
