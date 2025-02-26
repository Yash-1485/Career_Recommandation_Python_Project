import streamlit as st
import pandas as pd

# Sample job data (Replace this with actual job database/API)
def run(skills):
    jobs = pd.DataFrame([
        {"titles": ["Data Scientist", "Machine Learning Engineer"], "industry": "Tech", "skills": "Python, TensorFlow, SQL", "location": "Bangalore, India", "company_size": "500-1000", "salary": 1200000},
        {"titles": ["Data Analyst", "BI Analyst"], "industry": "Finance", "skills": "SQL, Excel, Power BI", "location": "Mumbai, India", "company_size": "1000-5000", "salary": 1000000},
        {"titles": ["Web Developer", "Frontend Developer"], "industry": "Tech", "skills": "HTML, CSS, JavaScript, React", "location": "New York, USA", "company_size": "200-500", "salary": 90000},
        {"titles": ["Full Stack Developer", "MERN Stack Developer"], "industry": "Tech", "skills": "MongoDB, Express, React, Node.js", "location": "Delhi, India", "company_size": "50-200", "salary": 800000},
        {"titles": ["Backend Developer", "Software Engineer"], "industry": "Tech", "skills": "Django, Python, PostgreSQL", "location": "London, UK", "company_size": "500-1000", "salary": 85000},
        {"titles": ["iOS Developer", "Mobile Developer"], "industry": "Tech", "skills": "Swift, Xcode, Firebase", "location": "San Francisco, USA", "company_size": "1000-5000", "salary": 110000},
        {"titles": ["Android Developer", "Kotlin Developer"], "industry": "Tech", "skills": "Kotlin, Java, Firebase", "location": "Berlin, Germany", "company_size": "500-1000", "salary": 95000},
        {"titles": ["Data Engineer", "Big Data Developer"], "industry": "Tech", "skills": "Hadoop, Spark, Python", "location": "Hyderabad, India", "company_size": "1000-5000", "salary": 1400000},
        {"titles": ["AI Engineer", "Deep Learning Engineer"], "industry": "Tech", "skills": "PyTorch, TensorFlow, NLP", "location": "Toronto, Canada", "company_size": "200-500", "salary": 100000},
        {"titles": ["Data Scientist", "ML Researcher"], "industry": "Tech", "skills": "Python, Scikit-learn, Deep Learning", "location": "Singapore", "company_size": "500-1000", "salary": 90000},
        {"titles": ["UX Designer", "UI/UX Researcher"], "industry": "Design", "skills": "Figma, Adobe XD, Prototyping", "location": "Sydney, Australia", "company_size": "200-500", "salary": 85000},
        {"titles": ["UI Designer", "Product Designer"], "industry": "Design", "skills": "Sketch, Figma, Wireframing", "location": "Chennai, India", "company_size": "1000-5000", "salary": 700000},
        {"titles": ["Web Designer", "Frontend Engineer"], "industry": "Tech", "skills": "CSS, JavaScript, Bootstrap", "location": "Los Angeles, USA", "company_size": "500-1000", "salary": 88000},
        {"titles": ["Data Analyst", "BI Consultant"], "industry": "Finance", "skills": "Power BI, SQL, Tableau", "location": "Hong Kong", "company_size": "1000-5000", "salary": 95000},
        {"titles": ["Full Stack Developer", "Web Engineer"], "industry": "Tech", "skills": "Vue.js, Laravel, MySQL", "location": "Kolkata, India", "company_size": "50-200", "salary": 850000},
        {"titles": ["Flutter Developer", "Mobile App Engineer"], "industry": "Tech", "skills": "Dart, Flutter, Firebase", "location": "Dubai, UAE", "company_size": "500-1000", "salary": 92000},
        {"titles": ["Backend Engineer", "API Developer"], "industry": "Tech", "skills": "Node.js, Express, MongoDB", "location": "Paris, France", "company_size": "500-1000", "salary": 87000},
        {"titles": ["Front-end Developer", "React Developer"], "industry": "Tech", "skills": "React, TypeScript, Redux", "location": "Pune, India", "company_size": "1000-5000", "salary": 900000},
        {"titles": ["Java Developer", "Spring Boot Engineer"], "industry": "Tech", "skills": "Java, Spring Boot, Hibernate", "location": "Stockholm, Sweden", "company_size": "500-1000", "salary": 94000},
        {"titles": ["iOS Engineer", "Swift Developer"], "industry": "Tech", "skills": "Swift, Core Data, UI Kit", "location": "Bangkok, Thailand", "company_size": "500-1000", "salary": 80000},
        {"titles": ["Android Engineer", "React Native Developer"], "industry": "Tech", "skills": "React Native, JavaScript, Firebase", "location": "Amsterdam, Netherlands", "company_size": "500-1000", "salary": 92000},
        {"titles": ["Data Engineer", "ETL Developer"], "industry": "Tech", "skills": "ETL, Apache Kafka, AWS", "location": "Gurgaon, India", "company_size": "1000-5000", "salary": 1300000},
        {"titles": ["DevOps Engineer", "Cloud Engineer"], "industry": "Tech", "skills": "AWS, Docker, Kubernetes", "location": "Bangalore, India", "company_size": "1000-5000", "salary": 1500000},
        {"titles": ["AI Researcher", "Machine Learning Scientist"], "industry": "Tech", "skills": "Computer Vision, AI Research, PyTorch", "location": "Tokyo, Japan", "company_size": "500-1000", "salary": 110000},
    ])


    st.title("\U0001F50D Job Search & Filtering")

    # Filters
    job_title = st.text_input("Search by Job Title (eg.Software Engineer, Full Stack Developer, Front-end Engineer, iOS Developer)")
    industry = st.text_input("Search by Industry (eg.Tech, Finance, Design, etc.)")
    location = st.text_input("Filter by Location (eg. Banglore, Berlin, Toronto, etc.)")
    salary_range = st.slider("Salary Range", min_value=30000, max_value=150000, value=(40000, 100000))
    
    if "show_all" not in st.session_state:
        st.session_state.show_all = False
    if "apply_filters" not in st.session_state:
        st.session_state.apply_filters = False
    if "matching_skills" not in st.session_state:
        st.session_state.matching_skills = False

    col1, col2,col3,col4 = st.columns(4)
    with col1:
        if st.button("Show All Jobs"):
            st.session_state.show_all = not st.session_state.show_all
            st.session_state.apply_filters = False
            st.session_state.matching_skills=False
    with col2:
        if st.button("Apply Filters"):
            st.session_state.apply_filters = True
            st.session_state.show_all = False
            st.session_state.matching_skills=False
    with col3:
        if st.button("Matching Skills"):
            st.session_state.apply_filters = False
            st.session_state.show_all = False
            st.session_state.matching_skills=True
    with col4:
        if st.button("Close Job Searching"):
            st.session_state.apply_filters = False
            st.session_state.show_all = False
            st.session_state.matching_skills=False

    if st.session_state.show_all:
        st.success('Shown all jobs')
        filtered_jobs = jobs
    elif st.session_state.apply_filters and job_title and industry and location and salary_range:
        st.success('Shown jobs based on filter')
        filtered_jobs = jobs[
            (jobs["titles"].apply(lambda titles: any(job_title.lower() in title.lower() for title in titles)) if job_title else True) |
            (jobs["industry"].str.contains(industry, case=False, na=False) if industry else True) &
            (jobs["location"].str.contains(location, case=False, na=False) if location else True) &
            (jobs["salary"] >= salary_range[0]) & (jobs["salary"] <= salary_range[1])
        ]
    elif st.session_state.matching_skills:
        st.success('Shown jobs based on matching skills')
        filtered_jobs = jobs[jobs["skills"].apply(lambda s: any(skill.lower() in s.lower() for skill in skills))]
    elif not st.session_state.show_all and not st.session_state.apply_filters and not st.session_state.matching_skills:
        filtered_jobs={}
    else:
        st.info('Fill out required fields for filter')
        st.success('Shown jobs based on matching skills')
        filtered_jobs = jobs[jobs["skills"].apply(lambda s: any(skill.lower() in s.lower() for skill in skills))]

    # Display results
    st.subheader("📃 Job Listings")
    if not st.session_state.show_all and not st.session_state.apply_filters and not st.session_state.matching_skills:
        st.info('Closed Job Searching')
    elif filtered_jobs.empty:
        st.write("❌ No jobs found matching your criteria.")
    else:
        for _, job in filtered_jobs.iterrows():
            missing_skills = find_missing_elements([skill.strip() for skill in list(eval(str(job['skills'].split(','))))], skills)
            if missing_skills:
                st.markdown(f"""
                <p style="font-size: larger;font-weight: bold;">{', '.join(job['titles'])}</p>  
                <p style="font-size: large;">📍Location: {job['location']} </p>
                <p style="font-size: large;">🏢Company Size: {job['company_size']} employees</p>  
                <p style="font-size: large;">💰Salary: ₹{job['salary']}</p>  
                <p style="font-size: large;">🏭Industry: {job['industry']}</p>  
                <p style="font-size: large;">📋Required Skills: {', '.join(job['skills'].split(','))}</p> 
                <p style="font-size: large;">📋✅Skills you have: {', '.join(skills)}</p> 
                <p style="font-size: large;">📋❌Missing skills: {', '.join(missing_skills)}</p> 
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <p style="font-size: larger;font-weight: bold;">{', '.join(job['titles'])}</p>  
                <p style="font-size: large;">📍Location: {job['location']} </p>
                <p style="font-size: large;">🏢Company Size: {job['company_size']} employees</p>  
                <p style="font-size: large;">💰Salary: ₹{job['salary']}</p>  
                <p style="font-size: large;">🏭Industry: {job['industry']}</p>  
                <p style="font-size: large;">📋Required Skills: {', '.join(job['skills'].split(','))}</p> 
                <p style="font-size: large;">📋✅Skills you have: {', '.join(skills)}</p> 
                <p style="font-size: large;">📋❌Missing skills: No missing skill, All skills you already have.</p> 
                """, unsafe_allow_html=True)
                # st.balloons()

def find_missing_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    # Elements that are in one list but not in both
    uncommon = list(set1.difference(set2))
    
    return uncommon
