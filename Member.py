from Bill import Bill
import psycopg2
from psycopg2 import sql
import time


class Member:
    def __init__(self, memberid):
        self.memberid = memberid
        self.my_bill = Bill(self.memberid)
        conn = psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT reservation_id FROM reservation WHERE member_ID = (%s)", (self.memberid,))
        self.reservations = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

    def getReservations(self):
        return self.reservations

    def getBill(self):
        return self.my_bill.getBill()

    def updateInformation(self, attribute: str, value: str):
        conn = psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432")
        cur = conn.cursor()

        cur.execute(
            sql.SQL("UPDATE member SET {} = %s WHERE member_id = %s",).format(sql.Identifier(attribute)),
            (value, self.memberid))

        conn.commit()
        cur.close()
        conn.close()

    def createReservation(self, restype: str, day: int, restime: str, court: int, members: list[int], guests: list[str]):
        

