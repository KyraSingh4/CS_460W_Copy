import schedule
import threading
import psycopg2
import datetime
import time
from Bill import Bill
from emailer import Emailer


def run_continouously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()

    return cease_continuous_run



def addYearlyFee():
    if datetime.datetime.now().day == 1 and datetime.datetime.now().month == 1:
        year = datetime.datetime.now().year - 1

        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT member_id FROM member")
                members = cur.fetchall()
            with conn.cursor() as cur:
                cur.execute("SELECT annualfee FROM billing_constants")
                annualfee = cur.fetchall()[0][0]

            em = Emailer()

            for member in members:
                if member[0] != 1 and member[0] != 2:
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO charges (member_id, amount, date, description, type) VALUES (%s, %s, %s, %s, %s)",
                                (member[0], annualfee, datetime.date(year, 1, 1),'Annual Dues', 'Annual'))
                    with conn.cursor() as cur:
                        cur.execute("SELECT email FROM member WHERE member_id = %s", (member[0],))
                        email = cur.fetchall()[0][0]
                        bill = Bill(member[0])
                        try:
                            em.sendBillEmail(bill.getBill(),email)
                        except:
                            pass
        return 0


def getUnpaid():
    year = str(datetime.datetime.now().year - 1)
    date = ''+year+'-01-01'
    with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT charge_id, member_id FROM charges WHERE isPaid = False AND date = %s AND type = 'Annual'",(date,))
            result = cur.fetchall()
    return result


def addLateFee():
    if datetime.datetime.now().day == 1:
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year - 1
        unpaid = getUnpaid()
        em = Emailer()
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            if month == 2:
                for i in range(len(unpaid)):
                    with conn.cursor() as cur:
                        cur.execute("SELECT amount FROM charges WHERE charge_id = %s", (unpaid[i][0],))
                        annualfee = cur.fetchall()[0]
                        annualfee = annualfee[0]
                    with conn.cursor() as cur:
                        cur.execute("UPDATE charges SET amount = %s WHERE charge_id = %s", (annualfee+annualfee*0.1, unpaid[i][0]))
                        cur.execute("SELECT email FROM member WHERE member_id = %s", (unpaid[i][1],))
                        email = cur.fetchone()[0]

                        try:
                            em.lateBillEmail(email)
                        except:
                            pass

            if month == 4:
                for i in range(len(unpaid)):
                    with conn.cursor() as cur:
                        cur.execute("SELECT amount FROM charges WHERE charge_id = %s", (unpaid[i][0],))
                        annualfee = cur.fetchall()[0]
                        annualfee = annualfee[0]/1.1
                    with conn.cursor() as cur:
                        cur.execute("UPDATE charges SET amount = %s WHERE charge_id = %s", (annualfee+annualfee*0.2, unpaid[i][0]))
                        cur.execute("SELECT email FROM member WHERE member_id = %s", (unpaid[i][1],))
                        email = cur.fetchone()[0]
                        try:
                            em.lateBillEmail(email)
                        except:
                            pass



def refreshReservation():
    day = datetime.datetime.today().weekday()
    with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM reservation WHERE res_day = %s", (day,))




schedule.every().day.at("05:30").do(lambda: addYearlyFee())
schedule.every().day.at("05:30").do(lambda: addLateFee())
schedule.every().day.at("05:30").do(lambda: refreshReservation())

stop_run_continuously = run_continouously(43200)


