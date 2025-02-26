import DB_Creadentials as crd
import mysql.connector as conn
def db_creation():
    try:
        db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd)
        cur=db.cursor()
        create_db=f"CREATE DATABASE IF NOT EXISTS {crd.db_name}"
        cur.execute(create_db)
        db.database=crd.db_name
        table_name="user"
        create_table=f"CREATE TABLE If not Exists user (id INT AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255) UNIQUE NOT NULL,password VARCHAR(255) NOT NULL,first_name VARCHAR(100) NOT NULL,last_name VARCHAR(100) NOT NULL,phone VARCHAR(15) NOT NULL,age INT NOT NULL,gender ENUM('Male', 'Female', 'Other') NOT NULL,skills TEXT NOT NULL,experience VARCHAR(10) NOT NULL,education VARCHAR(255) NOT NULL,career_interests TEXT NOT NULL,hobbies TEXT NOT NULL,interests TEXT NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
        db.database=crd.db_name
        cur.execute(create_table)
        db.commit()
        db.close()
    except Exception as e:
        print(e)