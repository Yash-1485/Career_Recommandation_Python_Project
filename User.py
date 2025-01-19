import mysql.connector as conn
import DB_Creadentials as crd
class User:
    def __init__(self,email,pwd,fname, mname, lname, age, gender, branch, education, skills, hobbies, interests):
        self.uid=get_uid()
        self.email=email
        self.pwd=pwd
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.branch = branch
        self.education = education  # list
        self.skills = skills  # list
        self.hobbies = hobbies  # list
        self.interests = interests  # list

    # Getter methods
    def get_fname(self):
        return self.fname

    def get_mname(self):
        return self.mname

    def get_lname(self):
        return self.lname

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_education(self):
        return self.education

    def get_skills(self):
        return self.skills

    def get_hobbies(self):
        return self.hobbies

    def get_interests(self):
        return self.interests

    def get_branch(self):
        return self.branch

    # Setter methods
    def set_fname(self, fname):
        self.fname = fname

    def set_mname(self, mname):
        self.mname = mname

    def set_lname(self, lname):
        self.lname = lname

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_education(self, education):
        self.education = education

    def set_skills(self, skills):
        self.skills = skills

    def set_hobbies(self, hobbies):
        self.hobbies = hobbies

    def set_interests(self, interests):
        self.interests = interests

    def set_branch(self, branch):
        self.branch = branch
        
    def __str__(self):
        return (f"User(fname={self.fname}, mname={self.mname}, lname={self.lname}, age={self.age}, "
            f"gender={self.gender}, address={self.address}, education={self.education}, "
            f"skills={self.skills}, hobbies={self.hobbies}, interests={self.interests}, "
            f"branch={self.branch})")

def get_uid():
    db=conn.connect(host=crd.host,user=crd.user,password=crd.pwd,database=crd.db_name)
    cursor=db.cursor()
    query = "SELECT * FROM USER ORDER BY USER_ID DESC LIMIT 1"
    cursor.execute(query)

    # Fetching the last enered result
    last_entry = cursor.fetchone()
    print(last_entry[0])
    return last_entry[0]+1


if __name__=="__main__":
    # Example:
    user = User(
        fname="John",
        mname="M",
        lname="Doe",
        age=25,
        gender="Male",
        address="123 Main St",
        education=["High School", "Bachelor's in CS"],
        skills=["Python", "Java"],
        hobbies=["Reading", "Cycling"],
        interests=["AI", "Data Science"],
        branch="Computer Science"
    )

    print(user)  # Output: John
