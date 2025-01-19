import DB_Creation as crt_db
import mysql.connector as conn
from User import User
import streamlit as st
from streamlit_tags import st_tags
from Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos
import io, random
import base64
from fpdf import FPDF

def course_recommender(course_list):
    st.subheader("**Courses & Certificates🎓 Recommendations**")
    c = 0
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 4)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course

# def show_pdf(file_path):
#     with open(file_path, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

def show_pdf(file_path):
    """Embed a PDF file in Streamlit."""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

# Function to create the resume PDF
def create_resume(user:User):
    pdf = FPDF()
    pdf.add_page()
    
    # Set title
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(0, 51, 102)  # Dark blue
    pdf.cell(0, 10, "Resume", ln=True, align='C')
    pdf.ln(10)

    # Basic Details
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Basic Details:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"First Name: {user.fname}", ln=True)
    pdf.cell(0, 10, f"Middle Name: {user.mname}", ln=True)
    pdf.cell(0, 10, f"Last Name: {user.lname}", ln=True)
    pdf.cell(0, 10, f"Age: {user.age}", ln=True)
    pdf.cell(0, 10, f"Gender: {user.gender}", ln=True)
    pdf.ln(10)

    # Education
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, "Education:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Branch: {user.branch}", ln=True)
    pdf.cell(0, 10, f"Highest Education: {user.education}", ln=True)
    pdf.ln(10)

    # Career
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, "Career:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Skills: {user.skills}")
    pdf.multi_cell(0, 10, f"Hobbies: {user.hobbies}")
    pdf.multi_cell(0, 10, f"Interest: {user.interests}")
    pdf.ln(10)

    # Save PDF
    # save_path = user.fname+".pdf"
    save_path = user.fname
    pdf.output(save_path)
    return pdf,save_path

def run():
    try:
        st.title("Welcome to the Career Recommendation System")
        st.write("Explore career opportunities tailored to your skills and interests.")
        
        flag=False
        user=None
        if("User" in st.session_state):
            user:User=st.session_state["User"]
            flag=True
        
        if(flag):
            skills=eval(user.skills)
            # print(skills)
            name=user.fname+" "+user.mname+" "+user.lname
            st.header("**Resume Analysis**")
            st.success("Hello " + name)
            st.subheader("**Your Basic info**")
            st.write('User Id: ' + str(user.uid))
            st.write('Name: ' + name)
            st.write('Email: ' + user.email)
            st.write('Age: ' + str(user.age))
            st.write('Gender: ' + user.gender)
            st.write('Branch: ' + user.branch)

            st.subheader("**Skills Recommendation💡**")
                ## Skill shows
            keywords = st_tags(
                label='### Skills that you have',
                text='See our skills recommendation',
                value=skills,  # Initial tags
                # suggestions=["Data Science", "AI", "Deep Learning"],  # Suggestions
                maxtags=10,  # Max number of tags
            )
            # st.write(keywords)

            ##  recommendation
            ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep Learning', 'flask',
                            'streamlit']
            web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                            'javascript', 'angular js', 'c#', 'flask','html','css']
            android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
            ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
            uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes',
                            'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator',
                            'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro',
                            'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp',
                            'user research', 'user experience']

            recommended_skills = []
            reco_field = ''
            rec_course = ''

            ## Courses recommendation
            for i in skills:
                ## Data science recommendation
                if i.lower() in ds_keyword:
                    print(i.lower())
                    reco_field = 'Data Science'
                    st.success("** Our analysis says you are looking for Data Science Jobs.**")
                    recommended_skills = ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling',
                                            'Data Mining', 'Clustering & Classification', 'Data Analytics',
                                            'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras',
                                            'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', "Flask",
                                            'Streamlit']
                    recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                    text='Recommended skills generated from System',
                                                    value=recommended_skills, key='2')
                    st.markdown(
                        '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                        unsafe_allow_html=True)
                    rec_course = course_recommender(ds_course)
                    break

                ## Web development recommendation
                elif i.lower() in web_keyword:
                    print(i.lower())
                    reco_field = 'Web Development'
                    st.success("** Our analysis says you are looking for Web Development Jobs **")
                    recommended_skills = ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel', 'Magento',
                                            'wordpress', 'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']
                    recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                    text='Recommended skills generated from System',
                                                    value=recommended_skills, key='3')
                    st.markdown(
                        '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                        unsafe_allow_html=True)
                    rec_course = course_recommender(web_course)
                    break

                ## Android App Development
                elif i.lower() in android_keyword:
                    print(i.lower())
                    reco_field = 'Android Development'
                    st.success("** Our analysis says you are looking for Android App Development Jobs **")
                    recommended_skills = ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java',
                                            'Kivy', 'GIT', 'SDK', 'SQLite']
                    recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                    text='Recommended skills generated from System',
                                                    value=recommended_skills, key='4')
                    st.markdown(
                        '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                        unsafe_allow_html=True)
                    rec_course = course_recommender(android_course)
                    break

                ## IOS App Development
                elif i.lower() in ios_keyword:
                    print(i.lower())
                    reco_field = 'IOS Development'
                    st.success("** Our analysis says you are looking for IOS App Development Jobs **")
                    recommended_skills = ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode',
                                            'Objective-C', 'SQLite', 'Plist', 'StoreKit', "UI-Kit", 'AV Foundation',
                                            'Auto-Layout']
                    recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                    text='Recommended skills generated from System',
                                                    value=recommended_skills, key='5')
                    st.markdown(
                        '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                        unsafe_allow_html=True)
                    rec_course = course_recommender(ios_course)
                    break

                ## Ui-UX Recommendation
                elif i.lower() in uiux_keyword:
                    print(i.lower())
                    reco_field = 'UI-UX Development'
                    st.success("** Our analysis says you are looking for UI-UX Development Jobs **")
                    recommended_skills = ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq',
                                            'Prototyping', 'Wireframes', 'Storyframes', 'Adobe Photoshop', 'Editing',
                                            'Illustrator', 'After Effects', 'Premier Pro', 'Indesign', 'Wireframe',
                                            'Solid', 'Grasp', 'User Research']
                    recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                    text='Recommended skills generated from System',
                                                    value=recommended_skills, key='6')
                    st.markdown(
                        '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                        unsafe_allow_html=True)
                    rec_course = course_recommender(uiux_course)
                    break
            # print(rec_course)
            # st.write(rec_course)

            try:                
                export_as_pdf = st.button("Export Report")                

                if export_as_pdf:
                    pdf,path=create_resume(user)
                    # Creating download link
                    pdf_data = pdf.output(dest="S").encode("latin-1")
                    html = create_download_link(pdf_data,path)
                    st.markdown(html, unsafe_allow_html=True)
                
                # pdf_file=f"{user.fname}.pdf"
                # see_file=st.button("Preview of Resume")
                # Predefined path to the PDF file
                pdf_path = f"D:/Career_Recommandation_Python_Project/Career_Recommandation_Python_Project/Resume/{user.fname}.pdf"  # Replace with your actual PDF path
                # Initialize the session state for toggling
                if "show_pdf" not in st.session_state:
                    st.session_state.show_pdf = False

                # Button to toggle PDF visibility
                if st.button("Preview/Hide Resume"):
                    st.session_state.show_pdf = not st.session_state.show_pdf

                # Display or hide the PDF based on the session state
                if st.session_state.show_pdf:
                    show_pdf(pdf_path)                    
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
