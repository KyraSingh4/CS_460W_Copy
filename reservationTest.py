import psycopg2
import datetime
from datetime import datetime, time, timedelta

with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
    with conn.cursor() as cur:
        cur.execute("select * from reservation")
        check = cur.fetchall()

print(check[0][4])

end = time(12,50)

print(datetime.combine(datetime.now(), check[0][4]) > (datetime.combine(datetime.now(), end) - timedelta(minutes=60)))
print(check[0][4] < end)

