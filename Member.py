from Bill import Bill
import psycopg2
from psycopg2 import sql


class Member:
    def __init__(self, memberid):
        self.memberid = memberid
        self.my_bill = Bill(self.memberid)

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

