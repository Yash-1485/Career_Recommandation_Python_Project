import streamlit as st
import mysql.connector as conn
import DB_Creadentials as crd
import User as user

count=0
def run():
    st.title("Login Page")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.button("Login"):
        # Replace this condition with actual database validation
        # if email == "test@example.com" and password == "password123":
        #     st.success("Logged in successfully!")
        # else:
        #     st.error("Invalid email or password. Please try again.")
        db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd,database=crd.db_name)
        cur=db.cursor()
        query="Select email,pwd from user"
        cur.execute(query)
        data=cur.fetchall()
        
        flag=False
        for em,pwd in data:
            if((em == email) and (pwd == password)):
                flag=True
                break
        
        if(flag):
            st.session_state["logged_in"] = True
            st.success("LoggedIn Successfully")
        else:
            global count
            count+=1
            print(count)
            st.error("Invalid email or password. Please try again.")
            
            if(count>2):
                st.info("If you haven't signed up, Sign Up First")
            
            # st.warning("Invalid email or password! Please Enter correct email or password")
        # print(data)