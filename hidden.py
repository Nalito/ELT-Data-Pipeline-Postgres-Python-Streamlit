# Keep this file separate

# Replace your credentials in secrets and save your changes

def secrets():
    return {"host": "your_host",
            "port": 5432,
            "database": "your_database",
            "user": "user",
            "pass": "password"}

def psycopg2(secrets) :
     return ('dbname='+secrets['database']+' user='+secrets['user']+
        ' password='+secrets['pass']+' host='+secrets['host']+
        ' port='+str(secrets['port']))

# Return an SQLAlchemy string

def alchemy(secrets) :
    return ('postgresql://'+secrets['user']+':'+secrets['pass']+'@'+secrets['host']+
        ':'+str(secrets['port'])+'/'+secrets['database'])

