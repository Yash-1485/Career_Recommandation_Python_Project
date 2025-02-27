import streamlit as st

# Sample job data (Replace this with actual job database/API)
jobs = [
        {"titles": ["Data Scientist", "Machine Learning Engineer"], "industry": "Tech", "skills": "Python, TensorFlow, SQL", "location": "Bangalore, India", "company_size": "500-1000", "salary": 1200000},
        {"titles": ["Data Analyst", "BI Analyst"], "industry": "Finance", "skills": "SQL, Excel, Power BI", "location": "Mumbai, India", "company_size": "1000-5000", "salary": 1000000},
        {"titles": ["Web Developer", "Frontend Developer"], "industry": "Tech", "skills": "HTML, CSS, JavaScript, React", "location": "New York, USA", "company_size": "200-500", "salary": 90000},
        {"titles": ["Full Stack Developer", "MERN Stack Developer"], "industry": "Tech", "skills": "MongoDB, Express, React, Node.js", "location": "Delhi, India", "company_size": "50-200", "salary": 800000},
        {"titles": ["Backend Developer", "Software Engineer"], "industry": "Tech", "skills": "Django, Python, PostgreSQL", "location": "London, UK", "company_size": "500-1000", "salary": 85000},
        {"titles": ["iOS Developer", "Mobile Developer"], "industry": "Tech", "skills": "Swift, Xcode, Firebase", "location": "San Francisco, USA", "company_size": "1000-5000", "salary": 110000},
        {"titles": ["Android Developer", "Kotlin Developer"], "industry": "Tech", "skills": "Kotlin, Java, Firebase", "location": "Berlin, Germany", "company_size": "500-1000", "salary": 95000},
        {"titles": ["Cybersecurity Analyst", "Security Engineer"], "industry": "Tech", "skills": "Network Security, SIEM, Firewalls", "location": "Boston, USA", "company_size": "1000-5000", "salary": 120000},
        {"titles": ["AI Engineer", "Deep Learning Engineer"], "industry": "Tech", "skills": "PyTorch, TensorFlow, NLP", "location": "Toronto, Canada", "company_size": "200-500", "salary": 100000},
        {"titles": ["Blockchain Developer", "Smart Contract Engineer"], "industry": "Tech", "skills": "Solidity, Ethereum, Web3.js", "location": "Singapore", "company_size": "500-1000", "salary": 130000},
        {"titles": ["UX Designer", "UI/UX Researcher"], "industry": "Design", "skills": "Figma, Adobe XD, Prototyping", "location": "Sydney, Australia", "company_size": "200-500", "salary": 85000},
        {"titles": ["Network Engineer", "Systems Administrator"], "industry": "Tech", "skills": "Cisco, Linux, Cloud Networking", "location": "Dubai, UAE", "company_size": "1000-5000", "salary": 115000},
        {"titles": ["Cloud Architect", "DevOps Engineer"], "industry": "Tech", "skills": "AWS, Kubernetes, Terraform", "location": "Seattle, USA", "company_size": "1000-5000", "salary": 140000},
        {"titles": ["Product Manager", "Agile Coach"], "industry": "Management", "skills": "Scrum, Agile, Product Roadmaps", "location": "Los Angeles, USA", "company_size": "500-1000", "salary": 130000},
        {"titles": ["Game Developer", "Unity Developer"], "industry": "Gaming", "skills": "Unity, C#, Unreal Engine", "location": "Tokyo, Japan", "company_size": "500-1000", "salary": 125000},
        {"titles": ["Full Stack Engineer", "Backend Engineer"], "industry": "Tech", "skills": "Node.js, GraphQL, PostgreSQL", "location": "Paris, France", "company_size": "500-1000", "salary": 105000},
        {"titles": ["Front-end Developer", "React Developer"], "industry": "Tech", "skills": "React, TypeScript, Redux", "location": "Pune, India", "company_size": "1000-5000", "salary": 900000},
        {"titles": ["SEO Specialist", "Digital Marketer"], "industry": "Marketing", "skills": "SEO, Google Ads, Social Media", "location": "Berlin, Germany", "company_size": "500-1000", "salary": 70000},
        {"titles": ["Java Developer", "Spring Boot Engineer"], "industry": "Tech", "skills": "Java, Spring Boot, Hibernate", "location": "Stockholm, Sweden", "company_size": "500-1000", "salary": 94000},
        {"titles": ["iOS Engineer", "Swift Developer"], "industry": "Tech", "skills": "Swift, Core Data, UI Kit", "location": "Bangkok, Thailand", "company_size": "500-1000", "salary": 80000},
        {"titles": ["Machine Learning Researcher", "AI Scientist"], "industry": "Tech", "skills": "AI, Deep Learning, Computer Vision", "location": "Helsinki, Finland", "company_size": "200-500", "salary": 135000},
        {"titles": ["Finance Analyst", "Investment Analyst"], "industry": "Finance", "skills": "Financial Modeling, Excel, SQL", "location": "Zurich, Switzerland", "company_size": "1000-5000", "salary": 140000},
    ]

def run(skills):
    st.title("\U0001F50D Job Search & Filtering")

    job_titles = sorted(set(title for job in jobs for title in job["titles"]))
    industries = sorted(set(job["industry"] for job in jobs))
    locations = sorted(set(job["location"] for job in jobs))

    # Streamlit Selection Lists (Dropdowns)
    # st.title("🔍 Job Search Filters")

    job_title = st.selectbox("Select Job Title:", job_titles, index=0)
    industry = st.selectbox("Select Industry:", industries, index=0)
    location = st.selectbox("Select Location:", locations, index=0)

    # Display Selected Filters
    st.markdown(f"**Selected Job Title:** {job_title}")
    st.markdown(f"**Selected Industry:** {industry}")
    st.markdown(f"**Selected Location:** {location}")
    salary_range = st.slider("Salary Range", min_value=30000, max_value=1500000, value=(40000, 1000000))

    if "show_all" not in st.session_state:
        st.session_state.show_all = False
    if "apply_filters" not in st.session_state:
        st.session_state.apply_filters = False
    if "matching_skills" not in st.session_state:
        st.session_state.matching_skills = False

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Show All Jobs"):
            st.session_state.show_all = not st.session_state.show_all
            st.session_state.apply_filters = False
            st.session_state.matching_skills = False
    with col2:
        if st.button("Apply Filters"):
            st.session_state.apply_filters = True
            st.session_state.show_all = False
            st.session_state.matching_skills = False
    with col3:
        if st.button("Matching Skills"):
            st.session_state.apply_filters = False
            st.session_state.show_all = False
            st.session_state.matching_skills = True
    with col4:
        if st.button("Close Job Searching"):
            st.session_state.apply_filters = False
            st.session_state.show_all = False
            st.session_state.matching_skills = False

    # Filtering Logic
    filtered_jobs = []
    if st.session_state.show_all:
        st.success('Showing all jobs')
        filtered_jobs = jobs
    elif st.session_state.apply_filters and job_title and industry and location and salary_range:
        st.success('Showing jobs based on filters')
        filtered_jobs = [
            job for job in jobs
            if (not job_title or any(job_title.lower() in title.lower() for title in job["titles"])) and
               (not industry or industry.lower() in job["industry"].lower()) and
               (not location or location.lower() in job["location"].lower()) and
               (salary_range[0] <= job["salary"] <= salary_range[1])
        ]
    elif st.session_state.matching_skills:
        st.success('Showing jobs based on matching skills')
        filtered_jobs = [
            job for job in jobs
            if any(skill.lower() in job["skills"].lower() for skill in skills)
        ]
    elif not st.session_state.show_all and not st.session_state.apply_filters and not st.session_state.matching_skills:
        filtered_jobs=[]
    else:
        st.info('Fill out required fields for filter')
        st.success('Showing jobs based on matching skills')
        filtered_jobs = [
            job for job in jobs
            if any(skill.lower() in job["skills"].lower() for skill in skills)
        ]

    # Display results
    st.subheader("📃 Job Listings")
    if not st.session_state.show_all and not st.session_state.apply_filters and not st.session_state.matching_skills:
        st.info('Closed Job Searching')
    elif not filtered_jobs:
        st.write("❌ No jobs found matching your criteria.")
    else:
        for job in filtered_jobs:
            job_skills = [s.strip().lower() for s in job["skills"].split(",")]
            user_skills = [s.lower() for s in skills]

            missing_skills = find_missing_elements(job_skills, user_skills)

            st.markdown(f"""
                <p style="font-size: larger; font-weight: bold;">{', '.join(job['titles'])}</p>  
                <p style="font-size: large;">📍 Location: {job['location']} </p>
                <p style="font-size: large;">🏢 Company Size: {job['company_size']} employees</p>  
                <p style="font-size: large;">💰 Salary: ₹{job['salary']}</p>  
                <p style="font-size: large;">🏭 Industry: {job['industry']}</p>  
                <p style="font-size: large;">📋 Required Skills: {', '.join(job['skills'].split(','))}</p> 
                <p style="font-size: large;">📋 ✅ Skills you have: {', '.join(skills)}</p> 
                <p style="font-size: large;">📋 ❌ Missing skills: {', '.join(missing_skills) if missing_skills else 'No missing skills, all skills are matched!'}</p> 
            """, unsafe_allow_html=True)

def find_missing_elements(list1, list2):
    """Find missing skills that the user does not have."""
    return list(set(list1) - set(list2))
