import DB_Creadentials as crd
import mysql.connector as conn
import streamlit as st
from User import User

table_name="user"
def run():
    st.title("Signup Page")
    
    # , clear_on_submit=True
    with st.form("signup_form"):
        st.subheader("Create an Account")
        
        em = st.text_input("Email", placeholder="Enter your email address")
        password = st.text_input("Password", type="password", placeholder="Enter a strong password")
        f_name = st.text_input("First Name", placeholder="Enter your first name")
        m_name = st.text_input("Middle Name (Optional)", placeholder="Enter your middle name")
        l_name = st.text_input("Last Name", placeholder="Enter your last name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gen = st.selectbox("Gender", ["Male", "Female", "Other"])
        education = st.text_area("Education", placeholder="Enter your education (comma-separated)")
        skills = st.text_area("Skills", placeholder="Enter your skills (comma-separated)")
        hobbies = st.text_area("Hobbies", placeholder="Enter your hobbies (comma-separated)")
        interests = st.text_area("Interests", placeholder="Enter your interests (comma-separated)")
        brn = st.text_input("Branch", placeholder="Enter your branch or department")
        
        # Submit button
        submitted = st.form_submit_button("Sign Up")        
        
        if submitted:
            if not em or not password or not f_name or not l_name or not age or not brn or not skills or not education or not hobbies or not interests:
                st.error("Please fill in all required fields.")
            else:
                # Convert comma-separated text fields into lists
                education_list = [e.strip() for e in education.split(",") if e.strip()]
                skills_list = [s.strip() for s in skills.split(",") if s.strip()]
                hobbies_list = [h.strip() for h in hobbies.split(",") if h.strip()]
                interests_list = [i.strip() for i in interests.split(",") if i.strip()]
                print(education_list)
                # Create a User instance
                new_user = User(
                    email=em,
                    pwd=password,
                    fname=f_name,
                    mname=m_name,
                    lname=l_name,
                    age=age,
                    gender=gen,
                    branch=brn,
                    education=education_list,
                    skills=skills_list,
                    hobbies=hobbies_list,
                    interests=interests_list
                )
                
                insert_data(new_user)
                                
                # st.success("Account created successfully!")
                st.write("Welcome, ", new_user.fname)
                
                # st.json(new_user.__dict__) # JSON File
    clear=st.button("Clear Form")
    if(clear):
        pass
def insert_data(user:User):
    try:
        db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd,database=crd.db_name)
        cur=db.cursor()
        user.uid=3
        query="INSERT INTO USER VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(user.uid,user.email,user.pwd,user.fname,user.mname,user.lname,user.age,user.gender,user.branch,str(user.education),str(user.skills),str(user.hobbies),str(user.interests)))
        db.commit()        
        if(cur.rowcount>0):
            st.success("New User added & Account created successfully!")
            st.info("Now to use app, you should login through app first")
        db.close()
    except Exception as e:
        st.info("Something went wrong!!!")