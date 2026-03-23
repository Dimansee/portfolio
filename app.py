import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_agraph import agraph, Node, Edge, Config

# PAGE CONFIG
st.set_page_config(
    page_title="Mann Choudhary | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# FONT AWESOME
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

# LOAD CSS
def load_css():
    with open("styles/style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Helper — convert any image file to base64 for embedding in HTML
import os

def img_to_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# ── TYPING ANIMATION ─────────────────────────────────────────────────────────
components.html("""
<div style="text-align:center; font-size:26px; font-weight:600;
            color:#60a5fa; padding:20px 0 12px 0; line-height:1.5;
            background:transparent;">
  <span id="typing"></span>
</div>
<style>
  body { margin:0; padding:0; background:transparent; overflow:hidden; }
  #typing::after {
    content: "|";
    animation: blink 1s infinite;
    margin-left: 2px;
  }
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0; }
  }
</style>
<script>
  const texts = ["Data Analyst","SQL Developer","Analytics Engineer",
                 "Python Developer","Data Engineer","Business Analyst"];
  let count = 0, index = 0;
  (function type() {
    const current = texts[count % texts.length];
    const letter  = current.slice(0, ++index);
    document.getElementById("typing").textContent = letter;
    if (letter.length === current.length) {
      count++; index = 0;
      setTimeout(type, 1400);
    } else {
      setTimeout(type, 80);
    }
  })();
</script>
""", height=80)

# ── NAVBAR — injected into parent document so it stays fixed while scrolling ──
components.html("""
<style>
  .fixed-navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 99999;
    display: flex;
    justify-content: center;
    gap: 32px;
    padding: 13px 20px;
    background: rgba(2, 6, 23, 0.96);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(59, 130, 246, 0.18);
    font-family: 'DM Sans', sans-serif;
    box-shadow: 0 2px 20px rgba(0,0,0,0.4);
  }
  .fixed-navbar a {
    text-decoration: none;
    color: #94a3b8;
    font-weight: 500;
    font-size: 14px;
    letter-spacing: 0.3px;
    padding-bottom: 3px;
    border-bottom: 2px solid transparent;
    transition: color 0.2s, border-color 0.2s;
    cursor: pointer;
  }
  .fixed-navbar a:hover {
    color: #60a5fa;
    border-bottom-color: #60a5fa;
  }
</style>
<script>
  function injectNavbar() {
    var parentDoc = window.parent.document;

    if (parentDoc.querySelector('.fixed-navbar')) return;

    // Inject styles
    var style = parentDoc.createElement('style');
    style.textContent = `
      .fixed-navbar {
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 99999;
        display: flex;
        justify-content: center;
        gap: 32px;
        padding: 13px 20px;
        background: rgba(2, 6, 23, 0.96);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(59, 130, 246, 0.18);
        font-family: 'DM Sans', sans-serif;
        box-shadow: 0 2px 20px rgba(0,0,0,0.4);
      }
      .fixed-navbar a {
        text-decoration: none;
        color: #94a3b8;
        font-weight: 500;
        font-size: 14px;
        letter-spacing: 0.3px;
        padding-bottom: 3px;
        border-bottom: 2px solid transparent;
        transition: color 0.2s, border-color 0.2s;
        cursor: pointer;
      }
      .fixed-navbar a:hover {
        color: #60a5fa;
        border-bottom-color: #60a5fa;
      }
    `;
    parentDoc.head.appendChild(style);

    // Create navbar
    var nav = parentDoc.createElement('div');
    nav.className = 'fixed-navbar';

    var links = [
      ['About','about'],
      ['Experience','experience'],
      ['Projects','projects'],
      ['Skills','skills'],
      ['Certifications','certifications'],
      ['Contact','contact']
    ];

    links.forEach(function(item) {
      var a = parentDoc.createElement('a');
      a.textContent = item[0];
      a.addEventListener('click', function() {
        var target = parentDoc.getElementById(item[1]);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      });
      nav.appendChild(a);
    });

    parentDoc.body.prepend(nav);

    // Push content down so navbar doesn't cover hero
    var appView = parentDoc.querySelector('[data-testid="stAppViewContainer"]')
                  || parentDoc.querySelector('.main');
    if (appView) appView.style.paddingTop = '52px';
  }

  // Run immediately and also after a short delay (Streamlit loads async)
  injectNavbar();
  setTimeout(injectNavbar, 500);
  setTimeout(injectNavbar, 1500);
</script>
""", height=0)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">

  <!-- FIX 6: Open to Work badge -->
  <div class="open-to-work-badge">
    <span class="otw-dot"></span> Open to Work
  </div>

  <h1>Mann Choudhary</h1>
  <div class="hero-subtitle">Data Analyst &nbsp;|&nbsp; Python &nbsp;|&nbsp; SQL &nbsp;|&nbsp; Power BI</div>
  <div class="hero-tagline">Transforming raw data into actionable insights &amp; analytical solutions.</div>

  <!-- FIX 5: location tag -->
  <div class="location-tag">
    <i class="fas fa-map-marker-alt"></i>&nbsp; Jaipur, India &nbsp;&bull;&nbsp; Open to Remote
  </div>

</div>
""", unsafe_allow_html=True)

# ── METRICS ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="metrics">
  <div class="metric-item">
    <h3>40%</h3>
    <p>Reporting Automation</p>
  </div>
  <div class="metric-item">
    <h3>12+</h3>
    <p>KPI Dashboards Built</p>
  </div>
  <div class="metric-item">
    <h3>10+</h3>
    <p>Projects Completed</p>
  </div>
  <div class="metric-item">
    <h3>4+ Yrs</h3>
    <p>Data Domain Experience</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SOCIAL ICONS ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="social-icons">
  <a href="https://www.linkedin.com/in/mann-choudhary-data-analyst" target="_blank" title="LinkedIn">
    <i class="fab fa-linkedin"></i>
  </a>
  <a href="https://github.com/Dimansee" target="_blank" title="GitHub">
    <i class="fab fa-github"></i>
  </a>
  <a href="mailto:manndimansee@gmail.com" title="Email">
    <i class="fas fa-envelope"></i>
  </a>
  <a href="tel:+919079914384" title="Phone">
    <i class="fas fa-phone"></i>
  </a>
  <a href="https://drive.google.com/drive/folders/1194SlTr1R6lMtXK-In2ulQKZCCgkdSxr?usp=sharing"
     target="_blank" title="Portfolio Files">
    <i class="fab fa-google-drive"></i>
  </a>
</div>
""", unsafe_allow_html=True)

# ── HERO BUTTONS ─────────────────────────────────────────────────────────────
with open("assets/resume.pdf", "rb") as f:
    b64_pdf = base64.b64encode(f.read()).decode()

download_link = f"""
<a href="data:application/pdf;base64,{b64_pdf}"
   download="Mann_Choudhary_Resume.pdf"
   class="hero-btn secondary">
  <i class="fas fa-download"></i>&nbsp; Download Resume
</a>
"""

st.markdown(f"""
<div class="hero-buttons-grid">
  <a href="#projects" class="hero-btn primary">
    <i class="fas fa-folder-open"></i>&nbsp; View Projects
  </a>
  {download_link}
  <a href="mailto:manndimansee@gmail.com" class="hero-btn secondary">
    <i class="fas fa-paper-plane"></i>&nbsp; Contact Me
  </a>
  <a href="https://drive.google.com/drive/folders/1194SlTr1R6lMtXK-In2ulQKZCCgkdSxr?usp=sharing"
     target="_blank" class="hero-btn secondary">
    <i class="fas fa-briefcase"></i>&nbsp; Portfolio Files
  </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── ABOUT ────────────────────────────────────────────────────────────────────
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.image("assets/profile.png", width=220)
with col2:
    st.markdown("""
Hi, I'm <b>Mann Choudhary</b> — a Data Analyst passionate about turning raw data into meaningful insights
that help businesses make smarter decisions.

<p>With <b>2+ years of experience</b> in data operations and MIS reporting, I have worked with large datasets,
built reports, and developed analytical solutions that improve business visibility and performance.</p>

<ul class="abt-points">
  <li><b>Data Analysis &amp; Programming</b> — Python (Pandas, NumPy), SQL (joins, aggregations, performance queries)</li>
  <li><b>Visualization &amp; Reporting</b> — Power BI, Looker Studio, Excel (pivot tables, advanced formulas), Google Sheets</li>
  <li><b>Data Platforms</b> — BigQuery (large-scale querying), GCP, SQL databases</li>
</ul>

<p>Recently I built and deployed a <b>SKU-level demand forecasting engine</b> using statistical models, Prophet,
and machine learning — accessible via a Streamlit application. I'm continuously expanding my skills in
advanced analytics, predictive modelling, and data storytelling.</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

# Pre-compute logos outside f-string to avoid nested quote syntax errors
_dakshina_b64 = img_to_b64("assets/dakshina_logo.png")
if _dakshina_b64:
    dakshina_logo_html = f'<div class="exp-logo-img"><img src="data:image/png;base64,{_dakshina_b64}" alt="Dakshina"/></div>'
else:
    dakshina_logo_html = '<div class="exp-logo" style="background:rgba(168,85,247,0.12);color:#a855f7;border-color:rgba(168,85,247,0.3);">D</div>'

st.markdown(f"""
<div class="exp-container">

  <div class="exp-card">
    <div class="exp-accent-bar"></div>
    <div class="exp-inner">
      <div class="exp-header">
        <div class="exp-logo-img"><img src="https://www.google.com/s2/favicons?domain=saadaa.in&sz=64" alt="SAADAA" style="padding:6px;"/></div>
        <div class="exp-header-text">
          <div class="exp-role">Senior Executive — Data Analyst</div>
          <div class="exp-sub-role">Founder's Office</div>
          <div class="exp-company-row">
            <span class="exp-company">SAADAA</span>
            <span class="exp-type-badge">Full-time</span>
          </div>
        </div>
        <div class="exp-date-block">
          <div class="exp-date">May 2025 — Dec 2025</div>
          <div class="exp-duration">8 months</div>
        </div>
      </div>
      <div class="exp-impact-row">
        <div class="exp-impact-chip">
          <span class="chip-num">40%</span>
          <span class="chip-label">Reporting Automated</span>
        </div>
        <div class="exp-impact-chip">
          <span class="chip-num">12+</span>
          <span class="chip-label">KPIs Tracked</span>
        </div>
        <div class="exp-impact-chip">
          <span class="chip-num">5+</span>
          <span class="chip-label">Dashboards Built</span>
        </div>
      </div>
      <ul class="exp-points">
        <li>Integrated multiple business data sources to build <b>centralized analytics systems</b> for reporting and decision-making.</li>
        <li>Validated and audited API data from frontend systems to ensure accuracy and data consistency.</li>
        <li>Designed interactive dashboards tracking KPIs across sales, returns, and marketing performance.</li>
        <li>Reduced reporting effort by <b>40%</b> through automated pipelines and templated reports.</li>
        <li>Collaborated with cross-functional teams — marketing, supply chain, finance, logistics — to translate business requirements into analytics solutions.</li>
        <li>Supported weekly and monthly performance reviews using real-time dashboards.</li>
      </ul>
      <div class="exp-tools-row">
        <span>BigQuery</span><span>SQL</span><span>Looker Studio</span>
        <span>Excel</span><span>Google Sheets</span><span>Analytics Reporting</span>
      </div>
    </div>
  </div>

  <div class="exp-card">
    <div class="exp-accent-bar" style="background:linear-gradient(to bottom,#a855f7,rgba(168,85,247,0.05));"></div>
    <div class="exp-inner">
      <div class="exp-header">
        {dakshina_logo_html}
        <div class="exp-header-text">
          <div class="exp-role">Data Entry Operator / MIS Analyst</div>
          <div class="exp-sub-role">Operations &amp; Reporting</div>
          <div class="exp-company-row">
            <span class="exp-company" style="color:#a855f7;">Dakshina Overseas</span>
            <span class="exp-type-badge" style="background:rgba(168,85,247,0.1);border-color:rgba(168,85,247,0.3);color:#c084fc;">Full-time</span>
          </div>
        </div>
        <div class="exp-date-block">
          <div class="exp-date">Jul 2022 — Dec 2024</div>
          <div class="exp-duration">2.5 years</div>
        </div>
      </div>
      <div class="exp-impact-row">
        <div class="exp-impact-chip" style="border-color:rgba(168,85,247,0.3);background:rgba(168,85,247,0.07);">
          <span class="chip-num" style="color:#c084fc;">10K+</span>
          <span class="chip-label">Records Managed</span>
        </div>
        <div class="exp-impact-chip" style="border-color:rgba(168,85,247,0.3);background:rgba(168,85,247,0.07);">
          <span class="chip-num" style="color:#c084fc;">2.5 Yrs</span>
          <span class="chip-label">Domain Experience</span>
        </div>
        <div class="exp-impact-chip" style="border-color:rgba(168,85,247,0.3);background:rgba(168,85,247,0.07);">
          <span class="chip-num" style="color:#c084fc;">High</span>
          <span class="chip-label">Data Accuracy</span>
        </div>
      </div>
      <ul class="exp-points">
        <li>Managed <b>10K+ operational records</b> ensuring high data accuracy and integrity.</li>
        <li>Created MIS reports using Excel Pivot Tables, VLOOKUP, and advanced formulas.</li>
        <li>Built dashboards and summaries to support operational tracking and reporting.</li>
        <li>Maintained transactional data using WolfePak software and internal reporting systems.</li>
        <li>Assisted teams in data organization, validation, and report generation for business operations.</li>
      </ul>
      <div class="exp-tools-row">
        <span>Microsoft Excel</span><span>Google Sheets</span>
        <span>MIS Reporting</span><span>WolfePak</span><span>Data Management</span>
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── PROJECTS — stacked card overlay style ────────────────────────────────────
st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)



fc_b64  = img_to_b64("assets/forecasting.png")
sd_b64  = img_to_b64("assets/sales_dashboard.png")
sql_b64 = img_to_b64("assets/sql_preview.png")

fc_src  = f"data:image/png;base64,{fc_b64}"  if fc_b64  else ""
sd_src  = f"data:image/png;base64,{sd_b64}"  if sd_b64  else ""
sql_src = f"data:image/png;base64,{sql_b64}" if sql_b64 else ""

st.markdown(f"""
<div class="projects-grid">

  <!-- Card 1 -->
  <div class="proj-card">
    <div class="proj-img-wrap">
      {"<img src='" + fc_src + "' class='proj-img' alt='Demand Forecasting'/>" if fc_src else "<div class='proj-img-placeholder'><i class='fas fa-chart-line'></i></div>"}
      <div class="proj-overlay">
        <div class="proj-overlay-content">
          <div class="proj-overlay-title">Demand Forecasting Engine</div>
          <div class="proj-overlay-desc">Hybrid SKU-level forecasting using Prophet &amp; ML.</div>
          <a href="https://demand-forecasting-engine-o22shix3vgbi5jgrvi4abg.streamlit.app/"
             target="_blank" class="overlay-btn">
            <i class="fas fa-external-link-alt"></i>&nbsp; View Live App
          </a>
        </div>
      </div>
    </div>
    <div class="proj-body">
      <div class="proj-tags">
        <span>Python</span><span>Prophet</span><span>ML</span><span>Streamlit</span>
      </div>
      <div class="proj-title">Demand Forecasting Engine</div>
      <div class="proj-desc">Hybrid SKU-level forecasting engine using statistical models,
      Facebook Prophet, and ML — deployed as a live Streamlit app.</div>
    </div>
  </div>

  <!-- Card 2 -->
  <div class="proj-card">
    <div class="proj-img-wrap">
      {"<img src='" + sd_src + "' class='proj-img' alt='Sales Dashboard'/>" if sd_src else "<div class='proj-img-placeholder'><i class='fas fa-chart-bar'></i></div>"}
      <div class="proj-overlay">
        <div class="proj-overlay-content">
          <div class="proj-overlay-title">Sales Analytics Dashboard</div>
          <div class="proj-overlay-desc">Interactive KPI tracking across sales, growth &amp; returns.</div>
          <span class="overlay-tag-badge">Power BI Project</span>
        </div>
      </div>
    </div>
    <div class="proj-body">
      <div class="proj-tags">
        <span>Power BI</span><span>Power Query</span><span>DAX</span><span>KPI</span>
      </div>
      <div class="proj-title">Sales Analytics Dashboard</div>
      <div class="proj-desc">Cleaned and transformed data using Power Query. Analyzed yearly
      and region-wise sales trends. Built interactive KPI dashboard tracking revenue,
      growth, and returns.</div>
    </div>
  </div>

  <!-- Card 3 — full width -->
  <div class="proj-card proj-card-wide">
    <div class="proj-wide-left">
      <div class="proj-tags">
        <span>SQL</span><span>BigQuery</span><span>Business Analysis</span><span>KPI</span>
      </div>
      <div class="proj-title">Business Analysis Case Study</div>
      <div class="proj-desc">End-to-end SQL project covering data extraction, transformation,
      and business insights. Covers KPI analysis, trend identification, and executive-level
      storytelling with a full ERD and slide deck.</div>
      <a href="assets/sql_project_slides.pdf" download="Mann_SQL_Case_Study.pdf"
         class="proj-download-btn">
        <i class="fas fa-download"></i>&nbsp; Download Case Study PDF
      </a>
    </div>
    <div class="proj-wide-right">
      {"<img src='" + sql_src + "' alt='SQL Preview'/>" if sql_src else "<div class='proj-img-placeholder' style='height:220px;border-radius:0 12px 12px 0;'><i class='fas fa-database'></i></div>"}
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── SKILLS — EXACT original agraph ───────────────────────────────────────────
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

colors = {
    "center": "#1E293B",
    "tech":   "#3B82F6",
    "biz":    "#A855F7",
    "soft":   "#10B981",
    "ai":     "#F59E0B",
    "vis":    "#4206cf"
}

nodes = [
    Node(id="Me",                 label="My Expertise",       size=80, shape="circle", color=colors["center"], font={"size": 12, "color": "white"}),
    Node(id="T",                  label="Technical",           size=60, shape="circle", color=colors["tech"],   font={"size": 10, "color": "white"}),
    Node(id="B",                  label="Business",            size=60, shape="circle", color=colors["biz"],    font={"size": 10, "color": "white"}),
    Node(id="P",                  label="Professional",        size=60, shape="circle", color=colors["soft"],   font={"size": 10, "color": "white"}),
    Node(id="A",                  label="AI Tools",            size=60, shape="circle", color=colors["ai"],     font={"size": 10, "color": "white"}),
    Node(id="Python",             label="Python",              size=45, shape="circle", color=colors["tech"],   font={"size": 8,  "color": "white"}),
    Node(id="SQL",                label="SQL",                 size=45, shape="circle", color=colors["tech"],   font={"size": 8,  "color": "white"}),
    Node(id="Visualization",      label="Visualization",       size=45, shape="circle", color=colors["vis"],    font={"size": 8,  "color": "white"}),
    Node(id="Looker Studio",      label="Looker Studio",       size=45, shape="circle", color=colors["vis"],    font={"size": 8,  "color": "white"}),
    Node(id="Power BI",           label="Power BI",            size=45, shape="circle", color=colors["vis"],    font={"size": 8,  "color": "white"}),
    Node(id="Tableau",            label="Tableau",             size=45, shape="circle", color=colors["vis"],    font={"size": 8,  "color": "white"}),
    Node(id="Forecasting",        label="Forecasting",         size=45, shape="circle", color=colors["biz"],    font={"size": 8,  "color": "white"}),
    Node(id="Storytelling",       label="Storytelling",        size=45, shape="circle", color=colors["biz"],    font={"size": 8,  "color": "white"}),
    Node(id="KPI Analysis",       label="KPI Analysis",        size=45, shape="circle", color=colors["biz"],    font={"size": 8,  "color": "white"}),
    Node(id="ChatGPT",            label="ChatGPT",             size=45, shape="circle", color=colors["ai"],     font={"size": 8,  "color": "white"}),
    Node(id="Gemini",             label="Gemini",              size=45, shape="circle", color=colors["ai"],     font={"size": 8,  "color": "white"}),
    Node(id="Prompt Engineering", label="Prompt Engineering",  size=45, shape="circle", color=colors["ai"],     font={"size": 8,  "color": "white"}),
    Node(id="Communication",      label="Communication",       size=45, shape="circle", color=colors["soft"],   font={"size": 8,  "color": "white"}),
    Node(id="Collaboration",      label="Collaboration",       size=45, shape="circle", color=colors["soft"],   font={"size": 8,  "color": "white"}),
    Node(id="Problem Solving",    label="Problem Solving",     size=45, shape="circle", color=colors["soft"],   font={"size": 8,  "color": "white"}),
]

edges = [
    Edge(source="Me", target="T"),
    Edge(source="Me", target="B"),
    Edge(source="Me", target="P"),
    Edge(source="Me", target="A"),
    Edge(source="T",  target="Python"),
    Edge(source="T",  target="SQL"),
    Edge(source="T",  target="Visualization"),
    Edge(source="Visualization", target="Looker Studio"),
    Edge(source="Visualization", target="Power BI"),
    Edge(source="Visualization", target="Tableau"),
    Edge(source="B",  target="Forecasting"),
    Edge(source="B",  target="Storytelling"),
    Edge(source="B",  target="KPI Analysis"),
    Edge(source="A",  target="ChatGPT"),
    Edge(source="A",  target="Gemini"),
    Edge(source="A",  target="Prompt Engineering"),
    Edge(source="P",  target="Communication"),
    Edge(source="P",  target="Collaboration"),
    Edge(source="P",  target="Problem Solving"),
]

config = Config(
    width=900,
    height=600,
    physics=True,
    nodeHighlightBehavior=True,
    collapsible=False,
)
agraph(nodes=nodes, edges=edges, config=config)

# SKILL TAGS
st.markdown('<div class="section-title" style="font-size:24px; margin-top:30px;">Core Skill Stack</div>', unsafe_allow_html=True)

tags = [
    "Data Analyst", "Python", "SQL", "Power BI", "Tableau", "Looker Studio",
    "BigQuery", "GCP", "Excel", "Google Sheets", "BRDs",
    "Forecasting", "Data Visualization", "Business Intelligence",
    "Data Storytelling", "Reporting", "KPI Analysis",
    "Pandas", "NumPy", "Matplotlib", "Streamlit", "Collaboration", "Communication"
]

st.markdown(
    '<div class="tags">' +
    "".join([f'<span class="tag">{tag}</span>' for tag in tags]) +
    '</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── CERTIFICATIONS ────────────────────────────────────────────────────────────
st.markdown('<div id="certifications" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cert-grid">

  <div class="cert-card">
    <div class="cert-icon"><i class="fas fa-brain"></i></div>
    <div class="cert-body">
      <div class="cert-title">Data Science</div>
      <div class="cert-issuer">Tutedude</div>
      <div class="cert-status in-progress">In Progress</div>
    </div>
  </div>

  <div class="cert-card">
    <div class="cert-icon" style="color:#0078d4;"><i class="fab fa-python"></i></div>
    <div class="cert-body">
      <div class="cert-title">Python</div>
      <div class="cert-issuer">Skill Academy (Testbook)</div>
      <div class="cert-status completed">Completed</div>
    </div>
  </div>

  <div class="cert-card">
    <div class="cert-icon" style="color:#f59e0b;"><i class="fas fa-database"></i></div>
    <div class="cert-body">
      <div class="cert-title">SQL</div>
      <div class="cert-issuer">Skill Academy (Testbook)</div>
      <div class="cert-status completed">Completed</div>
    </div>
  </div>

  <div class="cert-card">
    <div class="cert-icon" style="color:#10b981;"><i class="fas fa-chart-bar"></i></div>
    <div class="cert-body">
      <div class="cert-title">Business Analyst</div>
      <div class="cert-issuer">Skill Academy (Testbook)</div>
      <div class="cert-status completed">Completed</div>
    </div>
  </div>

</div>

<p style="text-align:center; color:#475569; font-size:13px; margin-top:18px;">
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────────────────────────
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; color:#94a3b8; margin-bottom:10px; font-size:16px;">
  Open to Data Analyst, Analytics Engineer, and BI roles.
</p>
<p style="text-align:center; color:#64748b; margin-bottom:30px; font-size:14px;">
  <i class="fas fa-map-marker-alt" style="color:#3b82f6;"></i>
  &nbsp;Jaipur, Rajasthan, India &nbsp;&bull;&nbsp; Open to Remote &amp; Hybrid
</p>

<div class="contact-grid">
  <a href="mailto:manndimansee@gmail.com" class="contact-card">
    <i class="fas fa-envelope"></i>
    <div>
      <div class="contact-label">Email</div>
      <div class="contact-value">manndimansee@gmail.com</div>
    </div>
  </a>
  <a href="https://www.linkedin.com/in/mann-choudhary-data-analyst" target="_blank" class="contact-card">
    <i class="fab fa-linkedin"></i>
    <div>
      <div class="contact-label">LinkedIn</div>
      <div class="contact-value">mann-choudhary-data-analyst</div>
    </div>
  </a>
  <a href="https://github.com/Dimansee" target="_blank" class="contact-card">
    <i class="fab fa-github"></i>
    <div>
      <div class="contact-label">GitHub</div>
      <div class="contact-value">github.com/Dimansee</div>
    </div>
  </a>
  <a href="tel:+919079914384" class="contact-card">
    <i class="fas fa-phone"></i>
    <div>
      <div class="contact-label">Phone</div>
      <div class="contact-value">+91 90799 14384</div>
    </div>
  </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <p>Built with love using Python &amp; Streamlit &nbsp;&bull;&nbsp; Mann Choudhary 2025</p>
</div>
""", unsafe_allow_html=True)

# FLOATING ACTION BAR — theme toggle, back to top, resume download, LinkedIn
components.html(f"""
<script>
var resumeB64 = "{b64_pdf}";

function injectFAB() {{
  var parentDoc = window.parent.document;
  if (parentDoc.querySelector('.fab-bar')) return;

  var style = parentDoc.createElement('style');
  style.textContent = `
    .fab-bar {{
      position: fixed;
      bottom: 28px;
      right: 24px;
      z-index: 99999;
      display: flex;
      flex-direction: column;
      gap: 10px;
      align-items: center;
    }}
    .fab-btn {{
      width: 46px;
      height: 46px;
      border-radius: 50%;
      border: 1px solid rgba(59,130,246,0.35);
      background: rgba(11,22,44,0.92);
      backdrop-filter: blur(10px);
      color: #94a3b8;
      font-size: 17px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.25s ease;
      box-shadow: 0 4px 16px rgba(0,0,0,0.4);
      text-decoration: none;
      position: relative;
    }}
    .fab-btn:hover {{
      background: rgba(59,130,246,0.18);
      border-color: #3b82f6;
      color: #60a5fa;
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(59,130,246,0.3);
    }}
    .fab-btn::before {{
      content: attr(data-tip);
      position: absolute;
      right: 54px;
      background: rgba(11,22,44,0.96);
      color: #cbd5e1;
      font-size: 11px;
      font-family: DM Sans, sans-serif;
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(59,130,246,0.2);
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s;
    }}
    .fab-btn:hover::before {{ opacity: 1; }}

    /* ── LIGHT THEME — full coverage ── */

    /* Page background + default text */
    body.light-theme,
    body.light-theme [data-testid="stAppViewContainer"],
    body.light-theme [data-testid="stApp"],
    body.light-theme [data-testid="stVerticalBlock"],
    body.light-theme [data-testid="stMarkdownContainer"],
    body.light-theme .block-container {{
      background-color: #f1f5f9 !important;
      color: #0f172a !important;
    }}

    /* All plain text elements */
    body.light-theme p,
    body.light-theme li,
    body.light-theme span,
    body.light-theme div,
    body.light-theme label {{
      color: #1e293b !important;
    }}

    /* Navbar */
    body.light-theme .fixed-navbar {{
      background: rgba(241,245,249,0.97) !important;
      border-bottom: 1px solid rgba(59,130,246,0.2) !important;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08) !important;
    }}
    body.light-theme .fixed-navbar a {{ color: #475569 !important; }}
    body.light-theme .fixed-navbar a:hover {{ color: #2563eb !important; border-bottom-color: #2563eb !important; }}

    /* Hero */
    body.light-theme .hero h1 {{
      background: linear-gradient(135deg, #0f172a 30%, #2563eb 100%) !important;
      -webkit-background-clip: text !important;
      background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
    }}
    body.light-theme .hero-subtitle {{ color: #334155 !important; }}
    body.light-theme .hero-tagline  {{ color: #64748b !important; }}
    body.light-theme .location-tag  {{ color: #64748b !important; }}

    /* Open to Work badge — keep green, just slightly adjust */
    body.light-theme .open-to-work-badge {{
      background: rgba(16,185,129,0.08) !important;
      color: #059669 !important;
    }}

    /* Metrics bar */
    body.light-theme .metrics {{
      background: #ffffff !important;
      border-color: rgba(59,130,246,0.15) !important;
      box-shadow: 0 2px 16px rgba(0,0,0,0.06) !important;
    }}
    body.light-theme .metric-item {{ border-right-color: rgba(59,130,246,0.1) !important; }}
    body.light-theme .metric-item h3 {{ color: #2563eb !important; }}
    body.light-theme .metric-item p  {{ color: #64748b !important; }}

    /* Social icon buttons */
    body.light-theme .social-icons a {{
      color: #475569 !important;
      border-color: #cbd5e1 !important;
      background: #ffffff !important;
    }}
    body.light-theme .social-icons a:hover {{
      color: #2563eb !important;
      border-color: #2563eb !important;
    }}

    /* Hero buttons */
    body.light-theme .hero-btn.secondary {{
      border-color: #cbd5e1 !important;
      color: #334155 !important;
    }}
    body.light-theme .hero-btn.secondary:hover {{
      border-color: #2563eb !important;
      color: #2563eb !important;
    }}

    /* Section titles */
    body.light-theme .section-title {{ color: #0f172a !important; }}
    body.light-theme .section-divider {{
      background: linear-gradient(90deg, transparent, rgba(59,130,246,0.3), transparent) !important;
    }}

    /* About text */
    body.light-theme .abt-points li {{ color: #334155 !important; }}

    /* Experience cards */
    body.light-theme .exp-card {{
      background: #ffffff !important;
      border-color: rgba(59,130,246,0.15) !important;
      box-shadow: 0 2px 16px rgba(0,0,0,0.06) !important;
    }}
    body.light-theme .exp-card:hover {{
      box-shadow: 0 8px 28px rgba(59,130,246,0.14) !important;
    }}
    body.light-theme .exp-role      {{ color: #0f172a !important; }}
    body.light-theme .exp-sub-role  {{ color: #64748b !important; }}
    body.light-theme .exp-date      {{ color: #475569 !important; }}
    body.light-theme .exp-duration  {{ color: #94a3b8 !important; }}
    body.light-theme .exp-points li {{ color: #334155 !important; }}
    body.light-theme .exp-impact-chip {{
      background: rgba(37,99,235,0.06) !important;
      border-color: rgba(37,99,235,0.18) !important;
    }}
    body.light-theme .chip-num   {{ color: #2563eb !important; }}
    body.light-theme .chip-label {{ color: #64748b !important; }}
    body.light-theme .exp-tools-row {{
      border-top-color: rgba(59,130,246,0.12) !important;
    }}
    body.light-theme .exp-tools-row span {{
      background: rgba(37,99,235,0.06) !important;
      border-color: rgba(37,99,235,0.18) !important;
      color: #2563eb !important;
    }}
    body.light-theme .exp-type-badge {{
      background: rgba(37,99,235,0.07) !important;
      border-color: rgba(37,99,235,0.2) !important;
      color: #2563eb !important;
    }}
    body.light-theme .exp-logo {{
      background: rgba(37,99,235,0.08) !important;
      border-color: rgba(37,99,235,0.2) !important;
      color: #2563eb !important;
    }}

    /* Project cards */
    body.light-theme .proj-card {{
      background: #ffffff !important;
      border-color: rgba(59,130,246,0.15) !important;
      box-shadow: 0 2px 16px rgba(0,0,0,0.06) !important;
    }}
    body.light-theme .proj-title {{ color: #0f172a !important; }}
    body.light-theme .proj-desc  {{ color: #475569 !important; }}
    body.light-theme .proj-tags span {{
      background: rgba(37,99,235,0.07) !important;
      border-color: rgba(37,99,235,0.2) !important;
      color: #2563eb !important;
    }}
    body.light-theme .proj-wide-left {{ background: #ffffff !important; }}
    body.light-theme .proj-download-btn {{
      border-color: rgba(37,99,235,0.3) !important;
      color: #2563eb !important;
    }}
    body.light-theme .proj-download-btn:hover {{
      background: rgba(37,99,235,0.07) !important;
    }}

    /* Certifications */
    body.light-theme .cert-card {{
      background: #ffffff !important;
      border-color: rgba(59,130,246,0.15) !important;
      box-shadow: 0 2px 16px rgba(0,0,0,0.06) !important;
    }}
    body.light-theme .cert-title  {{ color: #0f172a !important; }}
    body.light-theme .cert-issuer {{ color: #64748b !important; }}

    /* Skill tags */
    body.light-theme .tag {{
      background: #ffffff !important;
      border-color: #cbd5e1 !important;
      color: #334155 !important;
    }}
    body.light-theme .tag:hover {{
      border-color: #2563eb !important;
      color: #2563eb !important;
      background: rgba(37,99,235,0.05) !important;
    }}

    /* Contact cards */
    body.light-theme .contact-card {{
      background: #ffffff !important;
      border-color: rgba(59,130,246,0.15) !important;
      box-shadow: 0 2px 16px rgba(0,0,0,0.06) !important;
    }}
    body.light-theme .contact-label {{ color: #94a3b8 !important; }}
    body.light-theme .contact-value {{ color: #0f172a !important; }}

    /* Footer */
    body.light-theme .footer {{
      color: #94a3b8 !important;
      border-top-color: rgba(59,130,246,0.1) !important;
    }}

    /* FAB buttons */
    body.light-theme .fab-btn {{
      background: rgba(255,255,255,0.95) !important;
      border-color: rgba(59,130,246,0.25) !important;
      color: #475569 !important;
      box-shadow: 0 4px 14px rgba(0,0,0,0.1) !important;
    }}
    body.light-theme .fab-btn:hover {{
      background: rgba(37,99,235,0.08) !important;
      color: #2563eb !important;
      border-color: #2563eb !important;
    }}
    body.light-theme .fab-btn::before {{
      background: rgba(255,255,255,0.97) !important;
      color: #334155 !important;
      border-color: rgba(59,130,246,0.2) !important;
    }}
  `;
  parentDoc.head.appendChild(style);

  var bar = parentDoc.createElement('div');
  bar.className = 'fab-bar';

  // 1. Theme toggle
  var isDark = true;
  var themeBtn = parentDoc.createElement('button');
  themeBtn.className = 'fab-btn fab-theme';
  themeBtn.innerHTML = '☀️';
  themeBtn.setAttribute('data-tip', 'Light Mode');
  themeBtn.addEventListener('click', function() {{
    isDark = !isDark;
    if (isDark) {{
      parentDoc.body.classList.remove('light-theme');
      themeBtn.innerHTML = '☀️';
      themeBtn.setAttribute('data-tip', 'Light Mode');
    }} else {{
      parentDoc.body.classList.add('light-theme');
      themeBtn.innerHTML = '🌙';
      themeBtn.setAttribute('data-tip', 'Dark Mode');
    }}
  }});

  // 2. Back to top
  var topBtn = parentDoc.createElement('button');
  topBtn.className = 'fab-btn';
  topBtn.innerHTML = '↑';
  topBtn.setAttribute('data-tip', 'Back to Top');
  topBtn.style.fontSize = '20px';
  topBtn.style.fontWeight = '700';
  topBtn.addEventListener('click', function() {{
    // Try every possible Streamlit scroll container
    var selectors = [
      '[data-testid="stAppViewContainer"]',
      '[data-testid="stMainBlockContainer"]',
      '.main > div',
      '.block-container',
      'section.main',
      '.stApp',
      'main'
    ];
    var scrolled = false;
    for (var i = 0; i < selectors.length; i++) {{
      var el = parentDoc.querySelector(selectors[i]);
      if (el && el.scrollHeight > el.clientHeight) {{
        el.scrollTo({{ top: 0, behavior: 'smooth' }});
        scrolled = true;
        break;
      }}
    }}
    // Also scroll every element that has scrolled down (belt & suspenders)
    var all = parentDoc.querySelectorAll('*');
    for (var j = 0; j < all.length; j++) {{
      if (all[j].scrollTop > 0) {{
        all[j].scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}
    // Fallback: scroll the window itself
    parentDoc.documentElement.scrollTo({{ top: 0, behavior: 'smooth' }});
    parentDoc.body.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});

  // 3. Resume download
  var resumeBtn = parentDoc.createElement('a');
  resumeBtn.className = 'fab-btn';
  resumeBtn.innerHTML = '📄';
  resumeBtn.setAttribute('data-tip', 'Download Resume');
  resumeBtn.href = 'data:application/pdf;base64,' + resumeB64;
  resumeBtn.download = 'Mann_Choudhary_Resume.pdf';

  // 4. LinkedIn
  var liBtn = parentDoc.createElement('a');
  liBtn.className = 'fab-btn';
  liBtn.setAttribute('data-tip', 'LinkedIn');
  liBtn.href = 'https://www.linkedin.com/in/mann-choudhary-data-analyst';
  liBtn.target = '_blank';
  liBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>';

  bar.appendChild(themeBtn);
  bar.appendChild(topBtn);
  bar.appendChild(resumeBtn);
  bar.appendChild(liBtn);
  parentDoc.body.appendChild(bar);
}}

injectFAB();
setTimeout(injectFAB, 800);
setTimeout(injectFAB, 2000);
</script>
""", height=0)
