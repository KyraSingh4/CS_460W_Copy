import datetime
from Calendar import Calender
from Reservation import Reservation

# Create a Calender object
calender = Calender()

# Create some Reservation objects
reservation1 = Reservation(
    members=["John Doe", "Jane Doe"],
    guests=["Guest1"],
    court="1",
    date=datetime.datetime(2025, 3, 6),
    time=datetime.time(10, 0),
    weekDay=3
)

reservation2 = Reservation(
    members=["Alice", "Bob", "Charlie","David"],
    guests=["Guest2", "Guest3"],
    court="2",
    date=datetime.datetime(2025, 3, 7),
    time=datetime.time(11, 0),
    weekDay=4
)

# Add reservations to the calender
calender.addReservation(reservation1, reservation1.getDay())
calender.addReservation(reservation2, reservation2.getDay())

# Save the calender to a CSV file
calender.saveToCSV('calender.csv')

# Create a new Calender object and load the data from the CSV file
new_calender = Calender()
new_calender.loadFromCSV('calender.csv')

# Print the loaded reservations to verify
for weekDay, reservations in new_calender.reservations.items():
    for reservation in reservations:
        print(f"WeekDay: {weekDay}, Court: {reservation.getCourt()}, Date: {reservation.getDate()}, Time: {reservation.getTime()}, Members: {reservation.getMembers()}, Guests: {reservation.getGuests()}")