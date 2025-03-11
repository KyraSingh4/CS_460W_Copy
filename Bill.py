import psycopg2

class Bill:
    def __init__(self, memberID):
        self.isPaid = False
        self.memberID = memberID

    def isPaid(self):
        return self.isPaid

    def getTotal(self):
        total = 0

        conn = psycopg2.connect(dbname = "aced", user="postgres", password="", port="5423")
        cur = conn.cursor()
        cur.execute("SELECT amount FROM charges WHERE member_id = (%s)",*(self.memberID))
        
        bill = cur.fetchall()

        for i in bill:
            total += bill[i][0]

        return total

    def createCharge(self, value: float, memo: str, type: str):

        conn = psycopg2.connect(dbname="aced", user="postgres", password="", port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO charges (member_id, amount, description, type) "
                    "VALUES (%s, %s, %s, %s)", (self.memberID, value, memo, type))
        conn.commit()
        cur.close()
        conn.close()

    def resetBill(self):

        conn = psycopg2.connect(dbname="aced", user="postgres", password="", port="5432")
        cur = conn.cursor()
        cur.execute("DELETE FROM charges where member_id = (%s)", (self.memberID))
        conn.commit()
        cur.close()
        conn.close()

    def getBill(self):

        conn = psycopg2.connect(dbname="aced", user="postgres", password="", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT amount, date, description, type  FROM charges where member_id = (%s)", (self.memberID))
        bill = cur.fetchall()
        bill.append((self.getTotal(),"","Total Bill",""))


        