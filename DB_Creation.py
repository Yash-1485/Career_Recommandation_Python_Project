import DB_Creadentials as crd
import mysql.connector as conn
def db_creation():
    try:
        db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd)
        cur=db.cursor()
        create_db=f"CREATE DATABASE IF NOT EXISTS {crd.db_name}"
        cur.execute(create_db)
        table_name="user"
        create_table=f"CREATE TABLE IF NOT EXISTS USER(USER_ID INT PRIMARY KEY,EMAIL VARCHAR(100),PWD VARCHAR(20),FNAME VARCHAR(50),MNAME VARCHAR(50),LNAME VARCHAR(50),AGE INT,GENDER VARCHAR(20),BRANCH VARCHAR(1000),EDUCATION VARCHAR(1000),SKILLS VARCHAR(1000),HOBBIES VARCHAR(1000),INTERESTS VARCHAR(1000))"
        db.database=crd.db_name
        cur.execute(create_table)
        db.commit()
        db.close()
    except Exception as e:
        print(e)