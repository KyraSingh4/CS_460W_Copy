import unittest
import psycopg2
from ..Calendar import Calendar

class TestCalendar(unittest.TestCase):

    def setUp(self):
        self.calendar = Calendar()

        # Connect to the database and insert test data
        self.conn = psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432")
        with self.conn.cursor() as cur:

            # Insert a test member for member_id = 10
            cur.execute("""
                INSERT INTO member (member_id, firstname, lastname, email, phonenum, guestpass, optIN, active, password)
                VALUES (10, 'John', 'Doe', 'johndoe@example.com', '1234567890', 4, TRUE, TRUE, 'hashedpassword')
                ON CONFLICT (member_id) DO NOTHING
            """)

            # Insert a test reservation for res_id = 1
            cur.execute("""
                INSERT INTO reservation (reservation_id, court_num, res_day, start_time, end_time, member_id, type)
                VALUES (1, 1, 0, '10:00:00', '11:00:00', 10, 'singles')
                ON CONFLICT (reservation_id) DO NOTHING
            """)

            # Commit the changes
            self.conn.commit()

    def tearDown(self):
        # Clean up the test data after each test
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM reservation WHERE reservation_id = 10")
            cur.execute("DELETE FROM member WHERE member_id = 10")
            self.conn.commit()
        self.conn.close()

    def test_retrieve_day(self):
        # Test with a valid day
        day = 0
        result = self.calendar.RetrieveDay(day)
        self.assertIsInstance(result, list)  # Check if the result is a list

    def test_lookup_reservation(self):
        # Test with a valid reservation ID
        res_id = 1
        result = self.calendar.lookupReservation(res_id)
        self.assertIsInstance(result, list)  # Check if the result is a list

    def test_get_attendees(self):
        # Test with a valid reservation ID
        res_id = 1
        result = self.calendar.getAttendees(res_id)
        self.assertIsInstance(result, list)  # Check if the result is a list

    def test_get_attendees_invalid_reservation(self):
        # Test with an invalid reservation ID
        res_id = -1
        result = self.calendar.getAttendees(res_id)
        self.assertIsNone(result)  # Check if the result is None

if __name__ == '__main__':
    unittest.main()  # Run the tests