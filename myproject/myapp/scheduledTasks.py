import schedule
import threading
import psycopg2
import datetime
from Bill import Bill


def addYearlyFee():
    year = datetime.datetime.now().year - 1

    with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT member_id FROM member")
            members = cur.fetchall()
        for member in members:
            if member[0] != 1 and member[0] != 2:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO charges (member_id, amount, date, description, type) VALUES (%s, %s, %s, %s, %s)",
                                (member[0], 400, datetime.date(year, 1, 1),'Annual Dues', 'Annual'))

def getUnpaid():
    year = str(datetime.datetime.now().year - 1)
    date = ''+year+'-01-01'
    with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT charge_id FROM charges WHERE isPaid = False AND date = %s AND type = 'Annual'",(date,))
            result = cur.fetchall()
    return result


def addLateFee():
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year - 1
    unpaid = getUnpaid()
    with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
        if month == 2:
            for i in range(len(unpaid)):
                with conn.cursor() as cur:
                    cur.execute("UPDATE charges SET amount = %s WHERE charge_id = %s", (440, unpaid[i][0]))
        if month == 3:
            for i in range(len(unpaid)):
                with conn.cursor() as cur:
                    cur.execute("UPDATE charges SET amount = %s WHERE charge_id = %s", (480, unpaid[i][0]))



def refreshReservation():
    day = datetime.datetime.today().weekday()
    with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM reservation WHERE res_day = %s", (day,))
