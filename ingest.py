import requests
import psycopg2
import hidden

with requests.get("http://127.0.0.1:5000/fetch_employee_data/10000", stream=True) as r:

    # Load the secrets
    secrets = hidden.secrets()

    conn = psycopg2.connect(host=secrets['host'],
            port=secrets['port'],
            database=secrets['database'],
            user=secrets['user'],
            password=secrets['pass'],
            connect_timeout=3)

    cur = conn.cursor()
    sql = "INSERT INTO emp_happiness (id, occupation, salary, level, vacation, happiness) VALUES (%s, %s, %s, %s, %s, %s)"

    buffer = ""
    for chunk in r.iter_content(chunk_size=1):
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            print(t)
            cur.execute(sql, (t[0], t[1], t[2], t[3], t[4], t[5]))
            conn.commit()
            buffer = ""
        else:
            buffer += chunk.decode()
