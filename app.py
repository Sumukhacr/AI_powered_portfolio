import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# === Insert Groq API KEY here ===
GROQ_API_KEY = st.secrets["GROQ_API"] # <-- Replace before deploy

# === Custom Prompt Template ===
PROMPT_TEMPLATE = """
You are an expert assistant for Sumukha C R. Answer ONLY using the information in the resume below. Reply professionally.
You are an AI chatbot created by Sumukha, an AI enthusiast. 
Your job is to represent sumukha in the best possible way when recruiters, hiring managers, or visitors interact with you. 

Guidelines:
- Always answer in simple English and bullet points. 
- Never say anything negative or admit lack of skills. 
- Always explain things positively, highlighting strengths, adaptability, and potential. 
- Indirectly praise sumukha by showing confidence, passion, and capability. 
- If asked about skills, projects, or experiences → highlight them with enthusiasm. 
- If a job description is provided → map the required skills to sumukha’s strengths and explain why he is a perfect fit. 
- If asked general/personal questions → reply warmly, always leaving a professional impression. 
- The tone should be polite, professional, and subtly persuasive, making sumukha look like the best candidate. 

Remember: 
- Recruiters are visiting the portfolio, so always frame sumukha as highly capable, motivated, and a great team fit. 
- Never reveal limitations, weaknesses, or doubts. 
- Your role is to convince indirectly that sumukha is the best choice.
- When describing sumukha, always use confident and positive language to highlight adaptability, quick learning, and reliability.  
- Use examples from experiences and projects to show problem-solving skills and innovative thinking.  
- Emphasize a strong work ethic, teamwork, and dedication without stating them outright—let them be felt in the tone.  
- Convey enthusiasm for challenges and continuous improvement, aligning with whatever the recruiter values most.  
- Make sumukha come across as the candidate who naturally fits the company culture and role expectations, encouraging trust and interest.  
- try output in bullet points if possible and simple english crisp and simple, beacause the visitors don't have much time to read paragraphs.
Resume:
{resume_information}
Question:
{user_question}
Answer:
"""

# --- Resume content with detailed projects added ---
RESUME_TEXT = """
SUMUKHA C R
Software Engineer | Bengaluru, India
sumukhacr03@gmail.com | +91 7338445388
LinkedIn: https://www.linkedin.com/in/sumukha-c-r-83bbb32a9

Education:
B.E. in Electronics & Communication (HKBK College of Engineering, 2021-2025)

Skills:
C/C++, Python, HTML, Go, SQL, Shell scripting, Git/Github, Jenkins, Ansible, Terraform, Docker, AWS, Kubernetes, Linux, Excel, Power BI, Apache Spark, SnowFlake, N8N
Libraries: NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, Keras, Langchain, LangGraph, CrewAI

Courses:
Data Structures, Algorithms, Networking, OS, OOP, DBMS, DevOps, Cloud, ML, MLOps, Data Science, Generative AI, Agentic AI

Experience:
- Coding Samurai (C developer intern): Developed C++ applications with proficiency in OOP and DSA.
- GLEAMATOR Technologies (AWS Intern): Designed scalable and secure AWS cloud solutions.

Projects:
• Complete CICD Pipeline for Microservices
  Implemented end-to-end CICD pipelines for microservices using Jenkins, Docker, and EKS, reducing deployment time by 50%.
  Automated infrastructure with Terraform and integrated SonarQube and ArgoCD for code quality and GitOps-driven Kubernetes deployments.

• Cloud-Based Portfolio Hosting with AWS S3 and Terraform
  Deployed a public portfolio website using AWS S3 static hosting, showcasing cloud infrastructure expertise.
  Automated deployment with Terraform IaC for scalable, repeatable S3 bucket provisioning and website configuration.

• Library Management System (C++)
  Developed a C Library Management System using unordered_map for efficient ISBN-based book storage and retrieval.
  Implemented core features add, search, issue, return, delete with a user-friendly menu-driven interface.

• Sales Insights Data Analysis
  Performed sales insight data analysis to identify trends, patterns, and KPIs driving business performance.
  Built dashboards and reports to visualize insights, supporting data-driven decision-making.

• IPL Score Prediction (Machine Learning)
  Developed a machine learning model to predict cricket match scores by analyzing historical performance data.
  Applied data preprocessing, model training, and evaluation techniques to generate actionable insights.

• AI Powered Portfolio
  Developed a dynamic AI-powered personal portfolio using Streamlit, LangChain, and Groq, enabling real-time Q&A on career information.
  This project showcases applied skills in modern AI with full-stack deployment.

• Spam-Ham Classification (NLP)
  Built an NLP model for classifying email and SMS messages into spam or ham,
  employing text preprocessing, feature engineering, and machine learning algorithms for automated message filtering.

• Twitter Sentiment Analysis (NLP)
  Designed a sentiment analysis pipeline for tweets using natural language processing techniques,
  extracting and visualizing public sentiment on trending topics for actionable insights.

• Stock Market Prediction (Machine Learning)
  Developed a predictive analytics model using historical stock data and advanced machine learning algorithms,
  enabling data-driven investment decisions through trend analysis and forecasting.

Certificates:
IT Support (Google), Cybersecurity (Cisco), Git/Jenkins/Docker/Ansible/K8s/Terraform (KodeKloud),
Generative AI (Google Cloud), GitHub (Microsoft), Project Management (Great Learning),
Azure Fundamentals (Microsoft), Problem Solving (HackerRank)
"""

# ------- Streamlit UI --------
st.image("https://i.ibb.co/pBbD8H2H/1757252535757.png", caption="", width=250)
st.set_page_config(page_title="Sumukha C R | AI Portfolio", page_icon=":briefcase:", layout="wide")
st.title("Sumukha C R")
st.caption("Software Engineer | Bengaluru, India")
st.markdown("[LinkedIn](https://www.linkedin.com/in/sumukha-c-r-83bbb32a9) | [Github](https://github.com/sumukhacr)")

col1, col2 = st.columns([2.4, 1])

with col1:
    st.markdown("### 💼 About")
    st.write("An independent, self-motivated software engineer with expertise in cloud and AI technologies, dedicated to delivering scalable solutions.")
    st.markdown("### 🎓 Education")
    st.write("- **HKBK College of Engineering** (2021–2025), B.E. in Electronics & Communication")
    st.markdown("### 🛠️ Skills & Tools")
    st.write("C/C++, Python, Go, SQL, Shell, HTML, Git, Jenkins, Ansible, Terraform, Docker, AWS, Kubernetes, Excel, Linux, Power BI, Spark, SnowFlake, N8N")
    st.write("Libraries: NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, Keras, Langchain, LangGraph, CrewAI")
    st.markdown("### 📚 Courses")
    st.write("""
- Data structures & Algorithms
- Computer networking,
- Operating systems
- Object oriented Programming
- Database management systems
- DevOps and Cloud computing
- Machine Learning and MLOPS
- Data science and Analysis
- Generative AI and Agentic AI""")
    st.markdown("### 🧑‍💻 Experience")
    st.write("• **Coding Samurai (C Developer Intern):** Developed C++ applications with OOP and DSA proficiency")
    st.write("• **GLEAMATOR Technologies (AWS Intern):** Cloud design, deployment, and security on AWS")
    st.markdown("### 🚀 Projects")
    st.write("""
- **Complete CICD Pipeline for Microservices**  
Implemented end-to-end CICD pipelines for microservices using Jenkins, Docker, and EKS, reducing deployment time by 50%. Automated infrastructure with Terraform, SonarQube and ArgoCD integrations for GitOps-driven Kubernetes deployments.

- **Cloud-Based Portfolio Hosting with AWS S3 and Terraform**  
Deployed a public portfolio website with AWS S3 static hosting, automating infrastructure as code using Terraform for scalable repeatable deployments.

- **Library Management System (C++)**  
Developed a C++ library system using unordered_map for ISBN-based book tracking with features like add, search, issue, return, and delete via menu-driven interface.

- **Sales Insights Data Analysis**  
Analyzed sales data to discover trends, identify KPIs and design dashboards to inform decision-making.

- **IPL Score Prediction (Machine Learning)**  
Built ML models to predict cricket match scores leveraging historical data, data preprocessing and evaluation techniques.

- **AI Powered Portfolio**  
Created a Streamlit-based AI portfolio integrating LangChain and Groq for real-time career Q&A in an interactive UI showcasing AI & cloud skills.

- **Spam-Ham Classification (NLP)**  
Designed an NLP classifier for spam detection in emails and SMS using feature engineering and machine learning methods.

- **Twitter Sentiment Analysis (NLP)**  
Built a sentiment analysis tool for Twitter data to extract and visualize public sentiments toward trending topics.

- **Stock Market Prediction (Machine Learning)**  
Implemented ML models utilizing historical stock market data for price forecasting and investment insight.
""")

    st.markdown("### 🥇 Certifications")
    st.write("""
- IT Support (Google)
- Cybersecurity (Cisco)
- Git/Jenkins/Docker/Ansible/K8s/Terraform (KodeKloud)
- Generative AI (Google Cloud)
- GitHub (Microsoft)
- Project Management (Great Learning)
- Azure Fundamentals (Microsoft)
- Problem Solving (HackerRank)
""")

    st.success("""Ask about my resume, skills, experience, or projects! in chat """)
with col2:
    st.markdown("## 💬 AI Chat About Me")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    user_input = st.text_input("Ask anything about Sumukha:", key="user_question")
    send_btn = st.button("Send")
    llm_reply = ""
    if send_btn and user_input:
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama-3.1-8b-instant",
        )
        formatted_input = prompt_template.format(
            resume_information=RESUME_TEXT,
            user_question=user_input,
        )
        try:
            answer = llm.invoke(formatted_input)
            llm_reply = answer.content if hasattr(answer, "content") else str(answer)
        except Exception as e:
            llm_reply = f"❌ Error: {str(e)}"
        st.session_state.chat_history.append((user_input, llm_reply))
    for q, a in reversed(st.session_state.chat_history):
        with st.expander(f"Q: {q}", expanded=True):
            st.markdown(f"**A:** {a}")

st.markdown("---")
st.write("Built with Streamlit, LangChain, and Groq | © Sumukha C R | Powered by Llama-3")

st.markdown(
    """
    <style>
    .st-expanderHeader {font-size: 1.05rem;}
    .stButton>button {width:100%;}
    .stTextInput input {font-size: 1.05rem;}
    </style>
    """, unsafe_allow_html=True,
)
