import pymysql
import time

user = None
password = None
db = None
c =None
conn = None

def link_to ():
    global c,conn
    conn = pymysql.connect(host='localhost', user=user, password=password, database=db, charset='utf8')
    c = conn.cursor()

def write_json( name, description, salary, location, job_type, education_required, tags, company_name,
               company_size, url):
    global c
    try:
        c.execute(
            "INSERT INTO job (name,description,salary,location,job_type,education_required,tags,company_name,company_size,is_active,url,expiration_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (name, description, salary, location, job_type, education_required, tags, company_name, company_size, 1,
             url, time.strftime("2099-%m-%d %H:%M:%S", time.gmtime(time.time()))))
    except pymysql.err.OperationalError as e:
        print(e)
        print(name, description, salary, location, job_type, education_required, tags, company_name, company_size, 1,
             url, time.strftime("2099-%m-%d %H:%M:%S", time.gmtime(time.time())),sep="\n")

def close_conn():
    global conn
    conn.commit()
    conn.close()