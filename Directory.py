import psycopg2
from psycopg2 import sql

class Directory():
    def __init__(self):
        pass

    def getAll(self, memberid: int):
            #Member View
        if memberid != 1 and memberid !=2:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT firstname, lastname, email, phonenum FROM member"
                                "WHERE optin = TRUE AND active = true")
                    return cur.fetchall()
            #Admin View
        else:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM member")
                    return cur.fetchall()

    def searchAttr(self, memberid: str, attribute: str, value: str):
            #member View
        if memberid != 1 and memberid !=2:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
                with conn.cursor() as cur:
                    cur.execute(sql.SQL("SELECT firstname, lastname, email, phonenum FROM member"
                                "WHERE optin = TRUE AND active = true AND {attr} = %s").format(attr=sql.Identifier(attribute)),
                                (value,))
                    return cur.fetchall()
            #Admin View
        else:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
                with conn.cursor() as cur:
                    cur.execute(sql.SQL("SELECT * FROM member WHERE {attr} = %s").format(attr=sql.Identifier(attribute)),
                                (value,))
                    return cur.fetchall()

    def searchAll(self, memberid: str, value: str):
        if memberid != 1 and memberid !=2:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT firstname, lastname, email, phonenum FROM member"
                                "WHERE firstname = (%s) OR lastname = (%s) OR email = (%s) OR phonenum = (%s)",
                                (value, value, value, value))
                    return cur.fetchall()
        else:
            with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM member WHERE"
                                "member_id = %s OR firstname = %s OR lastname = %s OR email = %s OR phonenum = %s"
                                "OR guestpasses = %s OR optin = %s OR active = %s",
                                (value, value, value, value, value, value, value, value))