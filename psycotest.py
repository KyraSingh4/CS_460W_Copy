import psycopg2

def main():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Cookepolitikos1", port="5432")
    cur = conn.cursor()

    #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
    #            (100, "abc'def"))

    cur.execute("SELECT num FROM test;")

    data = cur.fetchall()

    print(data)

    #print(data[1][1])
    #test = data[1]

    #print(test[1])

    conn.commit()

    cur.close()
    conn.close()

    print("done")

main()