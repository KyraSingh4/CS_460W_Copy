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

    def getInformation(self):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT firstname, lastname, email, phonenum, OptIn, guestpass FROM member WHERE member_ID = (%s) ", (self.memberid,))
                information = cur.fetchall()
        return information

    def getReservations(self):
        return self.reservations

    def getBill(self):
        return self.my_bill.getBill()

    def payBill(self):
        return self.my_bill.resetBill()

    def updateInformation(self, attribute: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                 cur.execute(
                    sql.SQL("UPDATE member SET {} = %s WHERE member_id = %s",).format(sql.Identifier(attribute)),
                (value, self.memberid))

    def createReservation(self, restype: str, day: int, start: time, end: time, court: int, members: list[int], guests: list[str]):
        check = self.checkReservationRules(restype, day, start, end, court, members, guests)
        print(check)
        if check != 0:
            return check
        else:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:

                with conn.cursor() as cur:
                    cur.execute("INSERT INTO reservation (court_num, res_day, start_time, end_time, member_id, type) VALUES "
                        "((%s), (%s), (%s), (%s), (%s), (%s))", (court, day, start, end, self.memberid, restype))


                with conn.cursor() as cur:
                    cur.execute("SELECT reservation_id FROM reservation WHERE member_ID = (%s) AND start_time = (%s) AND court_num = (%s)",
                        (self.memberid, start, court))
                    res_id = cur.fetchone()

                for i in range(len(members)):
                    with conn.cursor() as cur:
                        cur.execute("SELECT firstname, lastname FROM member WHERE member_ID = (%s)", (members[i],))
                        memname = cur.fetchall()
                        cur.execute("INSERT INTO attendees VALUES ((%s), (%s), (%s), (%s))",
                            (res_id[0], memname[0][0], memname[0][1],members[i]))

                for i in range(len(guests)):
                    guest = guests[i].split()
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO attendees (reservation_id, firstname, lastname) VALUES ((%s), (%s), (%s))",
                            (res_id[0], guest[0], guest[1]))
                        cur.execute("SELECT guestpass FROM member WHERE member_id = (%s)", (self.memberid,))
                        rem_passes = cur.fetchall()
                        cur.execute("UPDATE member SET guestpass = (%s) WHERE member_id = (%s)",
                            (rem_passes[0][0]-1, self.memberid))
                    self.my_bill.createCharge(5, "Guest Fee", "Other")
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
                return 1
            if check[i][0] <= end <= check[i][1]:
                conn.close()
                return 1

            #Rule 2: Overlapping reservation from same member.
        with conn.cursor() as cur:
            cur.execute("SELECT start_time, end_time FROM reservation WHERE member_ID = (%s) AND res_day = (%s)",
                        (self.memberid,day))
            check = cur.fetchall()
            for i in range(len(check)):
                if check[i][0] <= start <= check[i][1]:
                    conn.close()
                    return 2
                if check[i][0] <= end <= check[i][1]:
                    conn.close()
                    return 2

            #Rule 3: Reservation proximity before.
            for i in range(len(check)):
                if check[i][0] > end and datetime.combine(datetime.now(), check[i][0]) < (datetime.combine(datetime.now(), end) + timedelta(minutes=60)):
                    conn.close()
                    return 3

            #Rule 4: Reservation proximity after.
            for i in range(len(check)):
                if check[i][1] < start and datetime.combine(datetime.now(), check[i][1]) > (datetime.combine(datetime.now(), start) - timedelta(minutes=60)):
                    conn.close()
                    return 4

            #Rule 5: Checked on front-end.
            #Rule 6: Member has enough guest passes.
        with conn.cursor() as cur:
            cur.execute("SELECT guestpass FROM member WHERE member_id = (%s)", (self.memberid,))
            check = cur.fetchall()
        if len(guests) > check[0][0]:
            conn.close()
            return 6

            #Rule 7: Member has no more than 2 other reservations.
        with conn.cursor() as cur:
            cur.execute("SELECT reservation_id FROM reservation WHERE member_ID = (%s)", (self.memberid,))
            check = cur.fetchall()
        if len(check) > 3:
            conn.close()
            return 7

            #Rule 8: Check count of accompanying members.
        if restype == "doubles":
            if len(guests) + len(members) != 3:
                conn.close()
                return 8
        elif restype == "singles":
            if len(guests) + len(members) != 1:
                conn.close()
                return 8
        else:
            conn.close()
            return 8

        conn.close()
        return 0


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

    def updateInformation(self, member_id: int, attribute: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                if attribute == 'password':
                    cur.execute("UPDATE member SET password = crypt(%s, gen_salt('md5')) WHERE member_id = (%s)", (value,))
                else:
                    cur.execute(sql.SQL("UPDATE member SET {attr} = %s WHERE member_id = %s").format(attr = sql.Identifier(attribute)),(value,member_id))

    def deactivateMember(self, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE member SET active = FALSE WHERE member_id = %s", (value,))

    def getBill(self,memberid: int):
        bill = Bill(memberid)
        return bill.getBill()

class BillingStaff(Member):
    def __init__(self):
        super().__init__(2)

    def addEventFee(self, fee: float, memo: str, memberid: int):
        bill = Bill(memberid)
        bill.createCharge(fee, memo, "Other")

    def checkBillStatus(self, memberid: int):
        bill = Bill(memberid)
        return bill.isPaid()

    def modifyBill(self, charge_id: int, attribute: str, value: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute(sql.SQL("UPDATE charges SET {attr} = %s WHERE charge_id = (%s)").format(attr = sql.Identifier(attribute)),
                            (value, charge_id))

    def deleteCharge(self, charge_id:int):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM charges WHERE charge_id = %s", (charge_id,))

    def getBill(self,memberid: int):
        bill = Bill(memberid)
        return bill.getBill()