import psycopg2

def main():
    username = 'test'
    password = 'pass'
    with psycopg2.connect(dbname="postgres", user="postgres", password="Cookepolitikos1", port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO authenticate VALUES (%s,crypt(%s, gen_salt('md5')))", (username, password))


    print("done")

main()