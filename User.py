import mysql.connector as conn
import DB_Creadentials as crd
class User:
    def __init__(self, email, pwd, fname, lname, phone, age, gender, skills, experience, education, career_interests, hobbies, interests):
        self.email = email
        self.pwd = pwd
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.age = age
        self.gender = gender
        self.skills = skills  # List of skills
        self.experience = experience
        self.education = education
        self.career_interests = career_interests  # List of interests
        self.hobbies = hobbies  # List of hobbies
        self.interests = interests  # List of general interests
    
    # Getter methods
    def get_email(self):
        return self.email
    
    def get_pwd(self):
        return self.pwd
    
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
    
    def get_phone(self):
        return self.phone
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_skills(self):
        return self.skills
    
    def get_experience(self):
        return self.experience
    
    def get_education(self):
        return self.education
    
    def get_career_interests(self):
        return self.career_interests
    
    def get_hobbies(self):
        return self.hobbies
    
    def get_interests(self):
        return self.interests
    
    # Setter methods
    def set_email(self, email):
        self.email = email
    
    def set_pwd(self, pwd):
        self.pwd = pwd
    
    def set_fname(self, fname):
        self.fname = fname
    
    def set_lname(self, lname):
        self.lname = lname
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_age(self, age):
        self.age = age
    
    def set_gender(self, gender):
        self.gender = gender
    
    def set_skills(self, skills):
        self.skills = skills
    
    def set_experience(self, experience):
        self.experience = experience
    
    def set_education(self, education):
        self.education = education
    
    def set_career_interests(self, career_interests):
        self.career_interests = career_interests
    
    def set_hobbies(self, hobbies):
        self.hobbies = hobbies
    
    def set_interests(self, interests):
        self.interests = interests
    
    def __str__(self):
        return f"User({self.fname} {self.lname}, {self.email}, {self.phone}, {self.age} years old, {self.gender}, \
        Education: {self.education}, Experience: {self.experience}, Skills: {', '.join(self.skills) if self.skills else 'N/A'}, \
        Career Interests: {', '.join(self.career_interests) if self.career_interests else 'N/A'}, \
        Hobbies: {', '.join(self.hobbies) if self.hobbies else 'N/A'}, Interests: {', '.join(self.interests) if self.interests else 'N/A'})"

        

# def get_uid():
#     db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd,database=crd.db_name,port=crd.port)
#     cursor=db.cursor()
#     query = "SELECT * FROM USER ORDER BY USER_ID DESC LIMIT 1"
#     cursor.execute(query)

#     # Fetching the last enered result
#     last_entry = cursor.fetchone()
#     print(last_entry[0])
#     return last_entry[0]+1


if __name__=="__main__":
    # Example:
    user = User(
        email="john@gmail.com",
        pwd="John@1234",
        fname="John",
        lname="Doe",
        age=25,
        gender="Male",
        phone="7201020019",
        skills=["Python", "Java"],
        experience="Fresher",
        education="B.Tech",
        hobbies=["Reading", "Cycling"],
        interests=["AI", "Data Science"],
        career_interests=["WebDeveloper"]
    )

    print(user)  # Output: John
