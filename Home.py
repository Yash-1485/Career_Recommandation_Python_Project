import DB_Creation as crt_db
import mysql.connector as conn
from User import User
import streamlit as st
from streamlit_tags import st_tags
from Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos
import io, random

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
            print(rec_course)
            # st.write(rec_course)


    except Exception as e:
        print(e)
