import streamlit as st
import mysql.connector as conn
import DB_Creadentials as crd
import bcrypt
from User import User

count = 0  # Incorrect login attempt counter

def run():
    st.title("Login Page")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.button("Login"):
        db = conn.connect(host=crd.host, user=crd.user, password=crd.pwd, database=crd.db_name, port=crd.port)
        cur = db.cursor()
        query = "SELECT * FROM user WHERE email = %s"
        cur.execute(query, (email,))
        user_data = cur.fetchone()

        global count
        
        if user_data:
            stored_hashed_password = user_data[2]  # Assuming password is in the 3rd column (index 2)
            
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                st.session_state["logged_in"] = True
                st.success("Logged in Successfully!")
                st.session_state["User"] = create_user_instance(user_data)
            else:
                count += 1
                st.error("Invalid email or password. Please try again.")
        else:
            count += 1
            st.error("Invalid email or password. Please try again.")

        if count > 2:
            st.info("If you haven't signed up, Sign Up First")

        db.close()

def create_user_instance(data):
    """ Create a User object from fetched data """
    return User(
        email=data[1],
        pwd=data[2],
        fname=data[3],
        lname=data[4],
        phone=data[5],
        age=data[6],
        gender=data[7],
        skills=data[8].split(", "),
        experience=data[9],
        education=data[10],
        career_interests=data[11].split(", "),
        hobbies=data[12].split(", "),
        interests=data[13].split(", ")
    )

