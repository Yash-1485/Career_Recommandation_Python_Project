import DB_Creation as crt_db
import mysql.connector as conn
from User import User
import streamlit as st
from streamlit_tags import st_tags
from Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos
import io, random, os
import base64
from fpdf import FPDF
import JobSearch as JS

# def course_recommender(course_lists):
#     st.subheader("**Courses & Certificates🎓 Recommendations**")
#     c = 0
#     rec_course = []
#     no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 20, 4)
#     for course in course_lists:
#         for c_name, c_link in course:
#             c += 1
#             st.markdown(f"({c}) [{c_name}]({c_link})")
#             rec_course.append(c_name)
#             if c == no_of_reco:
#                 break
#     return rec_course

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
def create_report(user:User):
    pdf = FPDF()
    pdf.add_page()
    
    # Set title
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(0, 51, 102)  # Dark blue
    pdf.cell(0, 10, "Report", ln=True, align='C')
    pdf.ln(10)

    # Basic Details
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Basic Details:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"First Name: {user.fname}", ln=True)
    pdf.cell(0, 10, f"Last Name: {user.lname}", ln=True)
    pdf.cell(0, 10, f"Age: {user.age}", ln=True)
    pdf.cell(0, 10, f"Gender: {user.gender}", ln=True)
    pdf.ln(10)

    # Education
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, "Education:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Highest Education: {user.education}", ln=True)
    pdf.ln(10)

    # Career
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, "Career:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Skills: {', '.join(user.skills)}")
    pdf.multi_cell(0, 10, f"Hobbies: {', '.join(user.hobbies)}")
    pdf.multi_cell(0, 10, f"Interest: {', '.join(user.interests)}")
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
            SAVE_FOLDER = "Report"
            os.makedirs(SAVE_FOLDER, exist_ok=True)
            if st.session_state.User:
                pdf, path = create_report(user)  # Generate PDF
                pdf_path = os.path.join(SAVE_FOLDER, f"{path}.pdf")
                pdf.output(pdf_path)  # Ensure the file is written to disk
                with open(pdf_path, "rb") as f:
                    pdf_data = f.read()
                b64_pdf = base64.b64encode(pdf_data).decode("utf-8")
                download_js = f"""
                    <script>
                        var link = document.createElement('a');
                        link.href = "data:application/pdf;base64,{b64_pdf}";
                        link.download = "{path}.pdf";  // Use correct filename
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
                    </script>
                """
                st.markdown(download_js, unsafe_allow_html=True)
            
            skills=user.skills
            name=user.fname+" "+user.lname
            st.header("**Career Analysis**")
            st.success("Hello " + name)
            st.subheader("**Your Basic info**")
            st.write('Name: ' + name)
            st.write('Email: ' + user.email)
            st.write('Age: ' + str(user.age))
            st.write('Gender: ' + user.gender)

            st.subheader("**Skills Recommendation💡**")
            st.markdown('''<style>
                                .user_skill{
                                    font-size: 25px;
                                    color: red;
                                    display: inline-block;
                                    padding: 5px;
                                    line-height: 2rem;
                                    transition: all 0.2s;
                                }
                                .user_skill:hover{
                                    box-shadow: 0 0 3px 3px #ddd;
                                }
                            </style>''',unsafe_allow_html=True)
            user_skills=', '.join([f'<span class="user_skill">{skill}</span>' for skill in skills])
            st.markdown(f'### Skills that you have: {'\n'+user_skills}',unsafe_allow_html=True)
            
            
            # Skill Recommandations
            if "recommended_skills" not in st.session_state:
                st.session_state.recommended_skills = {}
            # Skill Keywords
            ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning', 'flask', 'streamlit', 'python']
            web_keyword = ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                        'javascript', 'angular js', 'c#', 'flask', 'html', 'css','javascript']
            android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy','java']
            ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
            uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes',
                            'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator',
                            'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro',
                            'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp',
                            'user research', 'user experience']

            # Job Fields & Skills Mapping
            job_fields = {
                "Data Science": (ds_keyword, ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 
                                            'Data Mining', 'Clustering & Classification', 'Data Analytics', 
                                            'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras', 
                                            'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', "Flask", 'Streamlit']),
                "Web Development": (web_keyword, ['React', 'Django', 'Node.js', 'React.js', 'PHP', 'Laravel', 'Magento', 
                                                'WordPress', 'JavaScript', 'Angular JS', 'C#', 'Flask', 'SDK']),
                "Android Development": (android_keyword, ['Android', 'Android Development', 'Flutter', 'Kotlin', 'XML', 
                                                        'Java', 'Kivy', 'GIT', 'SDK', 'SQLite']),
                "IOS Development": (ios_keyword, ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode', 
                                                'Objective-C', 'SQLite', 'Plist', 'StoreKit', "UI-Kit", 'AV Foundation', 
                                                'Auto-Layout']),
                "UI-UX Development": (uiux_keyword, ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 
                                                    'Prototyping', 'Wireframes', 'Storyframes', 'Adobe Photoshop', 
                                                    'Editing', 'Illustrator', 'After Effects', 'Premier Pro', 
                                                    'Indesign', 'Wireframe', 'Solid', 'Grasp', 'User Research'])
            }
            # User Skills (Example)
            user_skills = set([s.lower() for s in skills])
            course_mapping = {
                "Data Science": ds_course,
                "Web Development": web_course,
                "Android Development": android_course,
                "IOS Development": ios_course,
                "UI-UX Development": uiux_course
            }
            
            # Initialize session state for storing recommended skills
            if "recommended_skills" not in st.session_state:
                st.session_state.recommended_skills = {}

            def recommend_jobs():
                recommended_jobs = []
                valid_fields = {}

                # Find relevant fields where the user has matching skills
                for field, (keywords, skills_list) in job_fields.items():
                    if any(skill in keywords for skill in user_skills):  # User must have at least one matching skill
                        valid_fields[field] = skills_list

                # If relevant fields are found, proceed
                if valid_fields:
                    for field, skills_list in valid_fields.items():
                        recommended_jobs.append(field)

                        # Determine missing skills for this field
                        missing_skills = [skill for skill in skills_list if skill.lower() not in user_skills]

                        # Store in session state
                        st.session_state.recommended_skills[field] = missing_skills

                        # Display Job Recommendation
                        st.success(f"**Our analysis says you are looking for {field} Jobs.**")

                        # Display Recommended Skills (If any missing)
                        if missing_skills:
                            st.markdown(
                                '''<style>
                                    .skill {
                                        font-size: 20px;
                                        font-weight: bold;
                                        color: green;
                                    }
                                </style>''', 
                                unsafe_allow_html=True
                            )
                            formatted_skills = ', '.join([f'<span class="skill">`{skill}`</span>' for skill in missing_skills])
                            st.markdown(f"### 🔹 Recommended Skills for **{field}**: {'\n'+formatted_skills}", unsafe_allow_html=True)
                        else:
                            st.success(f"✅ You already have all the required skills for {field}! 🎉")

                        # Display Job Boost Message
                        st.markdown(
                            '''<h4 style='text-align: left; color: #1ed760;'>
                            🚀 Adding these skills to your resume will boost your chances of getting a Job 💼</h4>''',
                            unsafe_allow_html=True
                        )

                        # Recommend Courses (Slider with Unique Key)
                        no_of_reco = st.slider(f'Choose Number of Course Recommendations for {field}:', 
                                            1, 10, 4, key=f"slider_{field}")

                        # Call Course Recommendation
                        course_recommender(course_mapping[field], field, no_of_reco)
                else:
                    st.warning("No job recommendations found. Try adding more skills.")
                    
            # Course Recommendation Function
            def course_recommender(course_list, field_name,records):
                st.subheader(f"**Courses & Certificates 🎓 Recommendations for {field_name}**")
                no_of_reco = records
                
                for idx, (course_name, course_link) in enumerate(course_list[:no_of_reco], start=1):
                    st.markdown(f"({idx}) [{course_name}]({course_link})")
            # Run Recommendation
            recommend_jobs()


            try:                
                export_as_pdf = st.button("Export Report")                                
                    
                if export_as_pdf:
                    pdf,path=create_report(user)
                    # Creating download link
                    pdf_data = pdf.output(dest="S").encode("latin-1")
                    html = create_download_link(pdf_data,path)
                    st.markdown(html, unsafe_allow_html=True)

                # Predefined path to the PDF file
                pdf_path = f"Report/{user.fname}.pdf"
                # Initialize the session state for toggling
                if "show_pdf" not in st.session_state:
                    st.session_state.show_pdf = False

                # Button to toggle PDF visibility
                if st.button("Preview/Hide Report"):
                    st.session_state.show_pdf = not st.session_state.show_pdf

                # Display or hide the PDF based on the session state
                if st.session_state.show_pdf:
                    show_pdf(pdf_path)                    
            except Exception as e:
                print(e)
            
            try:
                JS.run(user.skills)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
