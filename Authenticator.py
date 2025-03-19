import psycopg2

class Authenticator:
    def __init__(self):
        pass

    def login(self, username, password):
        with psycopg2.connect(dbname="aced", user="aceduser", password="acedpassword", port="5432") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT member_id, firstname, lastname, (password = crypt(%s, password)) FROM member", (password,))
                members = cur.fetchall()


        for i in range(len(members)):
            name = members[i][1][0] + members[i][2][0:4]
            if self.checkUsername(username, name) and members[i][3] == True:
                return members[i][0]

        return False


    def checkUsername(self, username, name):
        if name  == username:
            return True
        else:
            return False