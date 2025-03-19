from Bill import Bill
import psycopg2
from psycopg2 import sql
from datetime import time, datetime, timedelta


class Member:
    def __init__(self, memberid):
        self.memberid = memberid
        self.my_bill = Bill(self.memberid)
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT reservation_id FROM reservation WHERE member_ID = (%s)", (self.memberid,))
                self.reservations = cur.fetchall()

    def getReservations(self):
        return self.reservations

    def getBill(self):
        return self.my_bill.getBill()

    def updateInformation(self, attribute: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                 cur.execute(
                    sql.SQL("UPDATE member SET {} = %s WHERE member_id = %s",).format(sql.Identifier(attribute)),
                (value, self.memberid))

    def createReservation(self, restype: str, day: int, start: time, end: time, court: int, members: list[int], guests: list[str]):
        if not self.checkReservationRules(restype, day, start, end, court, members, guests):
            return False

        conn = psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432")

        with conn.cursor() as cur:
            cur.execute("INSERT INTO reservation (courtnum, res_day, start_time, end_time, member_id, type) VALUES "
                        "((%s), (%s), (%s), (%s), (%s), (%s))", (court, day, start, end, self.memberid, restype))
        with conn.cursor() as cur:
            cur.execute("SELECT reservation_id FROM reservation WHERE member_ID = (%s) AND start_time = (%s) AND courtnum = (%s)",
                        (self.memberid, start, court))
            res_id = cur.fetch()

        for i in range(len(members)):
            with conn.cursor() as cur:
                cur.execute("SELECT firstname, lastname FROM member WHERE member_ID = (%s)", (members[i],))
                memname = cur.fetchall()
                cur.execute("INSERT INTO attendees VALUES ((%s), (%s), (%s), (%s))",
                            (res_id, memname[0][0], memname[0][1],members[i]))

        for i in range(len(guests)):
            guest = guests[i].split()
            with conn.cursor() as cur:
                cur.execute("INSERT INTO attendees (reservation_id, firstname, lastname) VALUES ((%s), (%s), (%s))",
                            (res_id, guest[0], guest[1]))
                cur.execute("SELECT guestpass FROM member WHERE member_id = (%s)", (self.memberid,))
                rem_passes = cur.fetchall()
                cur.execute("UPDATE member SET guestpass = (%s) WHERE member_id = (%s)",
                            (rem_passes[0][0]-1, self.memberid))
            self.my_bill.createCharge(5, "Guest Fee", "Other")

        conn.close()
        return True


    def checkReservationRules(self, restype: str, day:int, start: time, end: time, court: int, members: list[int], guests: list[str]):
        conn = psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432")
            #Rule 1: Overlapping reservation
        with conn.cursor() as cur:
            cur.execute("SELECT start_time, end_time FROM reservation WHERE res_day = (%s) AND court_num = (%s)",
                        (day, court))
            check = cur.fetchall()
        for i in range(len(check)):
            if check[i][0] <= start <= check[i][1]:
                conn.close()
                return False
            if check[i][0] <= end <= check[i][1]:
                conn.close()
                return False

            #Rule 2: Overlapping reservation from same member.
        with conn.cursor() as cur:
            cur.execute("SELECT (start_time, end_time) FROM reservation WHERE member_ID = (%s) AND day = (%s)",
                        (self.memberid,day))
            check = cur.fetchall()
        for i in range(len(check)):
            if check[i][0] <= start <= check[i][1]:
                conn.close()
                return False
            if check[i][0] <= end <= check[i][1]:
                conn.close()
                return False

            #Rule 3: Reservation proximity before.
        for i in range(len(check)):
            if check[i][0] > end and datetime.combine(datetime.now(), check[i][0]) < (datetime.combine(datetime.now(), end) + timedelta(minutes=60)):
                conn.close()
                return False

            #Rule 4: Reservation proximity after.
        for i in range(len(check)):
            if check[i][1] < start and datetime.combine(datetime.now(), check[i][1]) > (datetime.combine(datetime.now(), start) - timedelta(minutes=60)):
                conn.close()
                return False

            #Rule 5: Checked on front-end.
            #Rule 6: Member has enough guest passes.
        with conn.cursor() as cur:
            cur.execute("SELECT guestpass FROM member WHERE member_id = (%s)", (self.memberid,))
            check = cur.fetchall()
        if len(guests) > len(check[0][0]):
            conn.close()
            return False

            #Rule 7: Member has no more than 2 other reservations.
        with conn.cursor() as cur:
            cur.execute("SELECT reservation_id FROM reservation WHERE member_ID = (%s)", (self.memberid,))
            check = cur.fetchall()
        if len(check) > 2:
            conn.close()
            return False

            #Rule 8: Check count of accompanying members.
        if restype == "doubles":
            if len(guests) + len(members) != 3:
                conn.close()
                return False
        elif restype == "singles":
            if len(guests) + len(members) != 1:
                conn.close()
                return False
        else:
            conn.close()
            return False

        conn.close()


class President(Member):
    def __init__(self):
        super().__init__(1)

    def addEventFee(self, fee: float, memo: str, memberid: int):
        bill = Bill(memberid)
        bill.createCharge(fee, memo, "Other")

    def checkBillStatus(self, memberid: int):
        bill = Bill(memberid)
        return bill.isPaid()

    def createMember(self, firstname: str, lastname: str, email: str, phonenum: str, optin: bool, pw: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO member (firstname, lastname, email, phonenum, optin, password) "
                            "VALUES (%s, %s, %s, %s, %s, crypt(%s, gen_salt('md5')))",
                            (firstname, lastname, email, phonenum, optin, pw))

    def updateInformation(self, search: str, svalue: str, attribute: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                if attribute == 'password':
                    cur.execute(sql.SQL("UPDATE member SET {attr} = crypt(%s, gen_salt('md5')) WHERE {sear} = %s", ).format(attr = sql.Identifier(attribute), sear = sql.Identifier(search)),
                    (value, svalue))
                else:
                    cur.execute(sql.SQL("UPDATE member SET {attr} = %s WHERE {sear} = %s", ).format(attr = sql.Identifier(attribute), sear = sql.Identifier(search)),
                    (value, svalue))

    def deactivateMember(self, search: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute(sql.SQL("UPDATE member SET active = FALSE WHERE {sear} = %s").format(sear = sql.Identifier(search)),
                            (value,))

class BillingStaff(Member):
    def __init__(self):
        super().__init__(2)

    def addEventFee(self, fee: float, memo: str, memberid: int):
        bill = Bill(memberid)
        bill.createCharge(fee, memo, "Other")

    def checkBillStatus(self, memberid: int):
        bill = Bill(memberid)
        return bill.isPaid()

    def modifyBill(self, memberid: int, search: str, svalue: str, attribute: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute(sql.SQL("UPDATE charges SET {attr} = %s WHERE {sear} = %s AND member_id = (%s)").format(attr = sql.Identifier(attribute), sear = sql.Identifier(search)),
                            (value, svalue, memberid))

    def getBill(self,memberid: int):
        bill = Bill(memberid)
        return bill.getBill()