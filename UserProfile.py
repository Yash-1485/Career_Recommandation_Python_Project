from User import User
import DB_Creadentials as crd
import mysql.connector as conn
import streamlit as st
import time

def update_user_data(field, new_value, user):
    """ Update the selected field in the database and user session. """
    try:
        db = conn.connect(host=crd.host, user=crd.user, password=crd.pwd, database=crd.db_name)
        cursor = db.cursor()

        # Convert list-based fields to properly formatted strings
        if field in ["skills", "hobbies", "career_interests", "interests"]:
            new_value = ", ".join([item.strip() for item in new_value.split(",")])  # Clean whitespace

        query = f"UPDATE user SET {field} = %s WHERE id = %s"
        cursor.execute(query, (new_value, 1))
        db.commit()

        # Ensure lists are stored properly in session
        setattr(user, field, new_value.split(", ") if field in ["skills", "hobbies", "career_interests", "interests"] else new_value)
        st.session_state["User"] = user

        st.success(f"✅ {field.replace('_', ' ').capitalize()} updated successfully!")

    except Exception as e:
        st.error(f"❌ Error updating {field}: {e}")

    finally:
        cursor.close()
        db.close()
        time.sleep(3)
        st.rerun()

def run():
    st.title("CareerMap")
    user: User = st.session_state["User"]
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

    # User Profile Display
    st.markdown('<div class="profile-header">User Profile</div>', unsafe_allow_html=True)
    profile_fields = {
        "First Name": f"{user.fname}",
        "Last Name": f"{user.lname}",
        "Email": user.email,
        "Age": user.age,
        "Education": user.education,
        "Skills": ", ".join(user.skills),
        "Hobbies": ", ".join(user.hobbies),
        "Career Interests": ", ".join(user.career_interests),
        "Experience": user.experience,
        "Other Interests": ", ".join(user.interests)
    }

    for key, value in profile_fields.items():
        st.markdown(f'<div class="profile-section"><span class="highlight">{key}:</span> {value}</div>', unsafe_allow_html=True)

    # Edit Profile Section
    st.subheader("📝 Edit Your Profile")
    
    field_options = {
        "First Name": "fname",
        "Last Name": "lname",
        "Email": "email",
        "Age": "age",
        "Education": "education",
        "Skills": "skills",
        "Hobbies": "hobbies",
        "Career Interests": "career_interests",
        "Experience": "experience",
        "Other Interests": "interests"
    }
    
    selected_field = st.selectbox("Select the field to update:", list(field_options.keys()))
    db_field = field_options[selected_field]
    
    # Get current value
    current_value = getattr(user, db_field)
    if isinstance(current_value, list):
        current_value = ", ".join(current_value)
    
    new_value = st.text_input(f"Enter new value for {selected_field}:", value=current_value)
    
    if st.button("Update"):
        if new_value.strip():
            # Convert lists to comma-separated values if necessary
            if db_field in ["skills", "hobbies", "career_interests", "interests"]:
                new_value = ", ".join(new_value.split(","))

            update_user_data(db_field, new_value, user)
        else:
            st.warning("⚠️ Please enter a valid value.")

if __name__ == "__main__":
    run()