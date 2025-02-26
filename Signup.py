import DB_Creadentials as crd
import mysql.connector as conn
import streamlit as st
import re
import bcrypt
from User import User

table_name = "user"

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def email_exists(email, cursor):
    cursor.execute(f"SELECT * FROM {table_name} WHERE email = %s", (email,))
    return cursor.fetchone() is not None

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def is_strong_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in "!@#$%^&*()_+" for c in password)

def run():
    st.title("Signup Page")
    
    with st.form("signup_form"):
        st.subheader("Create an Account")
        
        email = st.text_input("Email", placeholder="Enter your email address")
        password = st.text_input("Password", type="password", placeholder="Enter a strong password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")
        f_name = st.text_input("First Name", placeholder="Enter your first name")
        l_name = st.text_input("Last Name", placeholder="Enter your last name")
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gen = st.selectbox("Gender", ["Male", "Female", "Other"])
        skills = st.text_area("Skills", placeholder="List your skills separated by commas")
        experience = st.selectbox("Years of Experience",["Fresher","1-3","3-5","5+"])
        education = st.text_input("Highest Education", placeholder="Enter your highest degree")
        career_interest_options = ["AI & Machine Learning", "Software Development", "Data Science", "Cybersecurity", "Marketing", "Finance"]
        career_interests = st.multiselect("Career Interests", career_interest_options )
        hobbies = st.text_area("Hobbies", placeholder="Enter your hobbies (comma-separated)")
        interests = st.text_area("Interests", placeholder="Enter your interests (comma-separated)")
        submit_button = st.form_submit_button("Signup")
        
        if submit_button:
            if not all([email, password, confirm_password, f_name, l_name, phone, str(age), gen, skills, experience, education, hobbies, interests]) or not career_interests:

                st.error("All fields are required. Please fill in all details.")
            elif not is_valid_email(email):
                st.error("Invalid email format. Please enter a valid email.")
            elif not is_strong_password(password):
                st.error("Password must be at least 8 characters long, include a number, an uppercase letter, and a special character.")
            elif password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            elif not phone.isdigit() or len(phone) not in [10, 12]:
                st.error("Invalid phone number. Please enter a valid 10 or 12-digit number.")
            else:
                skills_list = [s.strip() for s in skills.split(",") if s.strip()]
                hobbies_list = [h.strip() for h in hobbies.split(",") if h.strip()]
                interests_list = [i.strip() for i in interests.split(",") if i.strip()]
                career_interests_list = ", ".join(career_interests)

                new_user = User(
                    email=email,
                    pwd=password,
                    fname=f_name,
                    lname=l_name,
                    phone=phone,
                    age = age ,
                    gender = gen,
                    skills=skills_list,
                    experience = experience,
                    education= education,
                    career_interests = career_interests_list,
                    hobbies=hobbies_list,
                    interests=interests_list    
                )
                try:
                    insert_data(new_user)
                except Exception as e:
                    st.error(f"Failed to insert user: {e}")


                

def insert_data(user : User):
    try:
        db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd,database = crd.db_name,port=crd.port)


        cursor = db.cursor()
        
        if email_exists(user.email, cursor):
            st.error("Email already exists. Please use a different email.")
        else:
            hashed_password = hash_password(user.pwd)
            cursor.execute(f"INSERT INTO {table_name} (email, password, first_name, last_name, phone, age,gender,skills, experience, education, career_interests, hobbies, interests) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (user.email, hashed_password, user.fname, user.lname, user.phone,user.age,user.gender, ", ".join(user.skills), user.experience, user.education, user.career_interests, ", ".join(user.hobbies), ", ".join(user.interests)))


            db.commit()
            st.success("Account created successfully! You can now login.")
        
        cursor.close()
        db.close()
    except Exception as e:
        st.error(f"Database error: {e}")