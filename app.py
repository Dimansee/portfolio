import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_agraph import agraph, Node, Edge, Config


# FOR SOCIAL MEDIA IMAGE
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

# NAME
st.set_page_config(
    page_title="Mann Choudhary Portfolio",
    layout="wide"
)

# LOAD CSS
def load_css():
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# AFTER NAME COMPONENTS

components.html(
"""
<div style="text-align:center; font-size:28px; font-weight:600; color:#60a5fa;">
<span id="typing"></span>
</div>

<style>
#typing::after{
content:"|";
animation:blink 1s infinite;
margin-left:5px;
}

@keyframes blink{
0%{opacity:1;}
50%{opacity:0;}
100%{opacity:1;}
}
</style>

<script>

const texts = [
"Data Analyst",
"SQL Developer",
"Analytics Engineer",
"Python Developer",
"Data Engineer",
"Business Analyst"
];

let count = 0;
let index = 0;
let currentText = "";
let letter = "";

(function type(){

if(count === texts.length){
count = 0;
}

currentText = texts[count];
letter = currentText.slice(0, ++index);

document.getElementById("typing").textContent = letter;

if(letter.length === currentText.length){
count++;
index = 0;
setTimeout(type, 1200);
}
else{
setTimeout(type, 80);
}

})();

</script>
""",
height=80
)

# NAVBAR
st.markdown("""
<div class="navbar">
<a href="#about">About</a>
<a href="#experience">Experience</a>
<a href="#projects">Projects</a>
<a href="#skills">Skills</a>
<a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# HERO SECTION

st.markdown("""
<div class="hero">

<h1>Mann Choudhary</h1>

<h2 class="hero-subtitle">
Data Analyst | Python | SQL | Power BI
</h2>

<p>Transforming data into actionable insights and building analytical solutions.</p>

</div>
""", unsafe_allow_html=True)

# Recruiter-Friendly Metrics Section

st.markdown("""
<div class="metrics">

<div>
<h3>40%</h3>
<p>Reporting Automation</p>
</div>

<div>
<h3>12+</h3>
<p>KPI Dashboards Built</p>
</div>

<div>
<h3>10+</h3>
<p>Dashboard Completed</p>
</div>

<div>
<h3>4+ Yrs</h3>
<p>Data Domain Experience</p>
</div>

</div>
""", unsafe_allow_html=True)

# SOCIAL ICONS

st.markdown("""
<div class="social-icons">

<a href="https://www.linkedin.com/in/mann-choudhary-data-analyst" target="_blank">
<i class="fab fa-linkedin"></i>
</a>

<a href="https://github.com/Dimansee" target="_blank">
<i class="fab fa-github"></i>
</a>

<a href="mailto:manndimansee@gmail.com">
<i class="fas fa-envelope"></i>
</a>

<a href="tel:+919079914384">
<i class="fas fa-phone"></i>
</a>

<a href="https://drive.google.com/drive/folders/1194SlTr1R6lMtXK-In2ulQKZCCgkdSxr?usp=sharing" target="_blank">
<i class="fab fa-google-drive"></i>
</a>

</div>
""", unsafe_allow_html=True)

# RESUME BUTTON, VIEW PROJECT BUTTON, OTHER BUTTONS

# Read resume
with open("assets/resume.pdf", "rb") as f:
    pdf_bytes = f.read()

b64_pdf = base64.b64encode(pdf_bytes).decode()

download_link = f"""
<a href="data:application/pdf;base64,{b64_pdf}"
download="Mann_Choudhary_Resume.pdf"
class="hero-btn secondary">
Download Resume
</a>
"""

#BUTTONS

st.markdown(f"""
<div class="hero-buttons-grid">

<a href="#projects" class="hero-btn primary">
View Projects
</a>

{download_link}

<a href="mailto:manndimansee@gmail.com" class="hero-btn secondary">
Contact Me
</a>

<a href="https://drive.google.com/drive/folders/1194SlTr1R6lMtXK-In2ulQKZCCgkdSxr?usp=sharing" target="_blank" class="hero-btn secondary">
Portfolio Files
</a>

</div>
""", unsafe_allow_html=True)

# ABOUT SECTION

st.markdown('<div id="about" class="section fade-in">', unsafe_allow_html=True)

st.markdown('<div id="about" class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.image("assets/profile.png", width=220)

with col2:
    st.write("""
Hi, I'm <b>Mann Choudhary</b>, a Data Analyst passionate about turning raw data into meaningful insights that help businesses make smarter decisions.

With 2+ years of experience in data operations and MIS reporting, I have worked with large datasets, built reports, and developed analytical solutions that improve business visibility and performance.

I work with a variety of tools and technologies to analyze, transform, and visualize data:

<ul class="abt-points">
<b>Data Analysis & Programming</b>
<li>Python (Pandas, NumPy, data analysis)</li>
<li>SQL (data extraction, joins, aggregations, performance queries)</li>
</ul>

<ul class="abt-points">
<b>Data Visualization & Reporting</b>
<li>Power BI – interactive dashboards and KPI tracking</li>
<li>Microsoft Excel – advanced formulas, pivot tables, and data analysis</li>
<li>Google Sheets – reporting, collaboration, and automation</li>
</ul>

<ul class="abt-points">
<b>Data Platforms & Databases</b>
<li>BigQuery – querying large-scale datasets</li>
<li>SQL databases for structured data analysis</li>
</ul>

I enjoy solving business problems using data-driven approaches, forecasting models, and analytical thinking. Recently, I built and deployed a SKU-level demand forecasting engine using statistical models, Prophet, and machine learning, making the insights accessible through a Streamlit application.

I am continuously expanding my skills in advanced analytics, predictive modeling, and data storytelling while building projects that demonstrate real-world business impact.
""", unsafe_allow_html=True)

# EXPERIENCE SECTION

st.markdown("""
<div id="experience" class="section">
<h2 class="section-title">Experience</h2>
<div class="timeline">
<div class="timeline-item">
<div class="timeline-dot"></div>
<div class="timeline-card">

<div class="timeline-title">Senior Executive – Data Analyst | Founder’s Office</div>

<div class="timeline-company">SAADAA</div>
<div class="timeline-date">May 2025 – Dec 2025</div>

<ul class="exp-points">
<li>Integrated multiple business data sources to build centralized analytics systems for reporting and decision-making.
<li>Validated and audited API data from frontend systems to ensure accuracy and data consistency.
<li>Designed 5+ interactive dashboards.
<li>Tracking 12+ KPIs across sales, returns, and marketing performance.
<li>Reducing reporting effort by 40%.
<li>Collaborated with cross-functional teams (marketing, supply chain, finance, logistics) to translate business requirements into analytics solutions.
<li>Supported weekly and monthly performance reviews using real-time dashboards and analytics insights.
<ul>

<b>Tools Used: BigQuery • Excel • Google Sheets • Looker Studio • SQL • Analytics Reporting<b>
</div>
</div>

<div class="timeline-item">
<div class="timeline-dot"></div>
<div class="timeline-card">

<div class="timeline-title">Data Entry Operator</div>

<div class="timeline-company">Dakshina Overseas</div>

<div class="timeline-date">Jul 2022 – Dec 2024</div>

<ul class="exp-points">
<li>Managed 10K+ operational records ensuring high data accuracy and integrity.
<li>Created MIS reports using Excel Pivot Tables, VLOOKUP, and advanced formulas.
<li>Built basic dashboards and summaries to support operational tracking and reporting.
<li>Maintained transactional data using WolfePak software and internal reporting systems.
<li>Assisted teams in data organization, validation, and report generation for business operations.
<ul>

<b>Tools Used: Microsoft Excel • Google Sheets • MIS Reporting • Data Management<b>

</div>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# PROJECTS SECTION

st.markdown('<div id="projects" class="section fade-in">', unsafe_allow_html=True)

st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

# ---------- FIRST ROW ----------
col1, col2 = st.columns(2)

# Project 1
with col1:

    st.image("assets/forecasting.png")

    st.markdown("### Demand Forecasting Engine")

    st.write("Hybrid forecasting using statistical and ML models.")

    st.link_button(
        "View Live App",
        "https://demand-forecasting-engine-o22shix3vgbi5jgrvi4abg.streamlit.app/"
    )


# Project 2
with col2:

    st.image("assets/sales_dashboard.png")

    st.markdown("### Sales Analytics Dashboard | Power BI")

    st.write("""
• Cleaned and transformed data using Power Query  
• Analyzed yearly and region-wise sales trends  
• Built interactive dashboard tracking KPIs
""")


# ---------- THIRD PROJECT ----------

import streamlit as st

pdf_file = "assets/sql_project_slides.pdf"

st.markdown("### Business Analysis Case Study")

st.write("Project presentation explaining business insights and analytics strategy.")

with open(pdf_file, "rb") as pdf:
    st.download_button(
        "📄 Download Presentation",
        pdf,
        file_name="SQL_Project_Case_Study.pdf"
    )

st.image("assets/sql_preview.png")

# SKILLS SECTION

import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

def display_skills_graph():
    st.markdown("<h2 style='text-align: center; color: white;'>Skills</h2>", unsafe_allow_html=True)

    # 1. THE CSS FIX
    # We use 'position: absolute' to ensure the border wraps the actual graph area
    st.markdown("""
        <style>
        /* This targets the specific container Streamlit creates for the component */
        [data-testid="stVerticalBlock"] > div:has(iframe) {
            border: 2px solid rgba(59, 130, 246, 0.6);
            border-radius: 20px;
            background-color: rgba(2, 6, 23, 0.95);
            background-image: 
                linear-gradient(rgba(59, 130, 246, 0.1) 1px, transparent 1px), 
                linear-gradient(90deg, rgba(59, 130, 246, 0.1) 1px, transparent 1px);
            background-size: 30px 30px;
            padding: 15px;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.2);
            margin: 10px auto;
            max-width: 950px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. DATA SETUP
    colors = {"center": "#1E293B", "tech": "#3B82F6", "biz": "#A855F7", "soft": "#10B981", "ai": "#F59E0B", "vis": "#4206cf"}
    
    nodes = [
        Node(id="Me", label="My Expertise", size=80, shape="circle", color=colors["center"], font={"size": 12, "color": "white"}),
        
        Node(id="T", label="Technical", size=60, shape="circle", color=colors["tech"], font={"size": 10, "color": "white"}),
        
        Node(id="B", label="Business", size=60, shape="circle", color=colors["biz"], font={"size": 10, "color": "white"}),
        
        Node(id="P", label="Professional", size=60, shape="circle", color=colors["soft"], font={"size": 10, "color": "white"}),
        
        Node(id="A", label="AI Tools", size=60, shape="circle", color=colors["ai"], font={"size": 10, "color": "white"}),
        
        Node(id="Python", label="Python", size=45, shape="circle", color=colors["tech"], font={"size": 8, "color": "white"}),
        Node(id="SQL", label="SQL", size=45, shape="circle", color=colors["tech"], font={"size": 8, "color": "white"}),

        Node(id="Visualization", label="Visualization", size=45, shape="circle", color=colors["vis"], font={"size": 8, "color": "white"}),
        Node(id="Looker Studio", label="Looker Studio", size=45, shape="circle", color=colors["vis"], font={"size": 8, "color": "white"}),
        Node(id="Power BI", label="Power BI", size=45, shape="circle", color=colors["vis"], font={"size": 8, "color": "white"}),
        Node(id="Tableau", label="Tableau", size=45, shape="circle", color=colors["vis"], font={"size": 8, "color": "white"}),
        
        Node(id="Forecasting", label="Forecasting", size=45, shape="circle", color=colors["biz"], font={"size": 8, "color": "white"}),
        Node(id="Storytelling", label="Storytelling", size=45, shape="circle", color=colors["biz"], font={"size": 8, "color": "white"}),
        Node(id="KPI Analysis", label="KPI Analysis", size=45, shape="circle", color=colors["biz"], font={"size": 8, "color": "white"}),
        
        Node(id="ChatGPT", label="ChatGPT", size=45, shape="circle", color=colors["ai"], font={"size": 8, "color": "white"}),
        Node(id="Gemini", label="Gemini", size=45, shape="circle", color=colors["ai"], font={"size": 8, "color": "white"}),
        Node(id="Prompt Engineering", label="Prompt Engineering", size=45, shape="circle", color=colors["ai"], font={"size": 8, "color": "white"}),
        
        Node(id="Communication", label="Communication", size=45, shape="circle", color=colors["soft"], font={"size": 8, "color": "white"}),
        Node(id="Collaboration", label="Collaboration", size=45, shape="circle", color=colors["soft"], font={"size": 8, "color": "white"}),
        Node(id="Problem Solving", label="Problem Solving", size=45, shape="circle", color=colors["soft"], font={"size": 8, "color": "white"}),
    ]
    
    edges = [
        Edge(source="Me", target="T"), 
        Edge(source="Me", target="B"),
        Edge(source="Me", target="P"), 
        Edge(source="Me", target="A"),
        
        Edge(source="T", target="Python"), 
        Edge(source="T", target="SQL"),
        Edge(source="T", target="Visualization"),
        
        Edge(source="Visualization", target="Looker Studio"),
        Edge(source="Visualization", target="Power BI"),
        Edge(source="Visualization", target="Tableau"),
         
        Edge(source="B", target="Forecasting"),
        Edge(source="B", target="Storytelling"),
        Edge(source="B", target="KPI Analysis"),
        
        Edge(source="A", target="ChatGPT"),
        Edge(source="A", target="Gemini"),
        Edge(source="A", target="Prompt Engineering"),
        
        Edge(source="P", target="Communication"),
        Edge(source="P", target="Collaboration"),
        Edge(source="P", target="Problem Solving"),
        
    ]

    # 3. CONFIG
    config = Config(
        width=900, 
        height=600, 
        physics=True, 
        nodeHighlightBehavior=True,
        collapsible=False,
    )

    # 4. EXECUTION
    # Notice: We don't use <div> tags here anymore. 
    # The CSS selector above automatically finds the graph and draws the box around it.
    return agraph(nodes=nodes, edges=edges, config=config)

display_skills_graph()

# TAGS OF SKILL

st.markdown("<h2 style='text-align: center; color: white;'>Core Skill Stack</h2>", unsafe_allow_html=True)

tags = [
"Data Analyst",
"Excel",
"Google Sheet",
"BRDs",
"Python",
"SQL",
"Power BI",
"Tableau",
"Looker Studio",
"BigQuery",
"GCP",
"Forecasting",
"Data Visualization",
"Business Intelligence",
"Data Storytelling",
"Collaboration",
"Communication",
"Reporting",
"Matplotlib",
"Pandas",
"NumPy",
"Streamlit"
]

st.markdown(
"""
<div class="tags">
""" +
"".join([f"<span>{tag}</span>" for tag in tags]) +
"""
</div>
""",
unsafe_allow_html=True
)

# CONTACT SECTION

st.markdown('<div id="contact" class="section fade-in">', unsafe_allow_html=True)

st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)

st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

st.write("📧 Email: manndimansee@gmail.com")

st.write("🔗 LinkedIn: https://www.linkedin.com/in/mann-choudhary-data-analyst")

st.markdown('</div>', unsafe_allow_html=True)

# JAVASCRIPT FOR ACTIVE NAVBAR

st.markdown("""
<script>

const sections = document.querySelectorAll(".section");
const navLinks = document.querySelectorAll(".navbar a");

window.addEventListener("scroll", () => {

let current = "";

sections.forEach(section => {

const sectionTop = section.offsetTop;
const sectionHeight = section.clientHeight;

if (pageYOffset >= sectionTop - 200) {
current = section.getAttribute("id");
}

});

navLinks.forEach(a => {

a.classList.remove("active");

if (a.getAttribute("href").includes(current)) {
a.classList.add("active");
}

});

});

</script>
""", unsafe_allow_html=True)

# JAVASCRIPT FOR SCROLL ANIMATION

st.markdown("""
<script>

const observer = new IntersectionObserver(entries => {
entries.forEach(entry => {
if(entry.isIntersecting){
entry.target.classList.add("show");
}
});
});

document.querySelectorAll(".fade-in").forEach(el => {
observer.observe(el);
});

</script>

""", unsafe_allow_html=True)






