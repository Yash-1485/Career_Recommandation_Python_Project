from User import User
import DB_Creadentials as crd
import mysql.connector as conn
import streamlit as st
def run():
    user:User=st.session_state["User"]
    st.markdown(
        """
        <style>
            
            .profile-header {
                color: #00879E;
                text-align: center;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .profile-section {
                font-size: 18px;
                margin-bottom: 10px;
            }
            .highlight {
                font-weight: bold;
                color: #457b9d;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # User Profile Section
    st.markdown('<div class="profile-header">User Profile</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="profile-section"><span class="highlight">Name:</span> {user.fname} {user.lname}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Email:</span> {user.email}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Age:</span> {user.age}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Education:</span> {user.education}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Skills:</span> {", ".join(user.skills)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Hobbies:</span> {", ".join(user.hobbies)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Career Interests:</span> {", ".join(user.career_interests)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Experience:</span> {user.experience}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="profile-section"><span class="highlight">Other Interests:</span> {", ".join(user.interests)}</div>', unsafe_allow_html=True)
