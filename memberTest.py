from Member import Member
import psycopg2
from psycopg2 import sql


search = "email"
value = "test@test.com"

with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
    with conn.cursor() as cur:
        cur.execute(sql.SQL("UPDATE member SET active = FALSE WHERE {sear} = %s").format(sear=sql.Identifier(search)),
                    (value,))