import psycopg2

class Bill:
    def __init__(self, memberID):
        self.memberID = memberID

    def getTotal(self):
        total = 0
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT amount FROM charges WHERE member_id = (%s) AND isPaid = False",(self.memberID,))
                bill = cur.fetchall()

        for i in range(len(bill)):
            total += bill[i][0]

        return total

    def createCharge(self, value: float, memo: str, type: str):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO charges (member_id, amount, description, type) "
                    "VALUES (%s, %s, %s, %s)", (self.memberID, value, memo, type))

    def payBill(self, year: int):
        ystring = str(year)+'%'
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE charges SET isPaid = True WHERE date::varchar(10) LIKE %s AND member_id = %s", (ystring,self.memberID))

    def getBill(self):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT charge_id, amount, date, description, type  FROM charges where member_id = (%s) AND isPaid = FALSE",
                            (self.memberID,))
                bill = cur.fetchall()

        bill.append(("",self.getTotal(),"","Total Bill",""))

        return bill

    def getFullBill(self):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute(
                "SELECT charge_id, amount, date, description, type  FROM charges where member_id = (%s)",
                (self.memberID,))
                bill = cur.fetchall()

        bill.append(("", self.getTotal(), "", "Total Bill", ""))

        return bill