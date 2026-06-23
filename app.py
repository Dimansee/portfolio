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

# ── NAVBAR ────────────────────────────────────────────────────────────────────
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
        if (target) target.scrollIntoView({ behavior: 'smooth' });
      });
      nav.appendChild(a);
    });
    parentDoc.body.prepend(nav);
    var appView = parentDoc.querySelector('[data-testid="stAppViewContainer"]')
                  || parentDoc.querySelector('.main');
    if (appView) appView.style.paddingTop = '52px';
  }
  injectNavbar();
  setTimeout(injectNavbar, 500);
  setTimeout(injectNavbar, 1500);
</script>
""", height=0)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="open-to-work-badge">
    <span class="otw-dot"></span> Open to Work
  </div>
  <h1>Mann Choudhary</h1>
  <div class="hero-subtitle">Data Analyst &nbsp;|&nbsp; MIS Analyst &nbsp;|&nbsp; Business Analyst</div>
  <div class="hero-tagline">Building data systems, automations &amp; insights that drive real decisions.</div>
  <div class="location-tag">
    <i class="fas fa-map-marker-alt"></i>&nbsp; Jaipur, India &nbsp;&bull;&nbsp; Open to Relocate
  </div>
</div>
""", unsafe_allow_html=True)

# ── METRICS ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="metrics">
  <div class="metric-item">
    <h3>6</h3>
    <p>ERP Modules Built</p>
  </div>
  <div class="metric-item">
    <h3>20+ Hrs</h3>
    <p>Saved Weekly via Automation</p>
  </div>
  <div class="metric-item">
    <h3>4+ Yrs</h3>
    <p>Data Domain Experience</p>
  </div>
  <div class="metric-item">
    <h3>5+</h3>
    <p>Dashboards Shipped</p>
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
Hi, I'm <b>Mann Choudhary</b> — a Data Analyst based in Jaipur who builds data systems people actually rely on, not dashboards that get one screenshot and disappear.

<p>With <b>4+ years of experience</b> spanning e-commerce, import/export, and fashion-tech, I work at the intersection of data and operations. My edge is that I don't just analyse — I build end-to-end: from raw data ingestion and automated pipelines all the way to the dashboard a founder opens every morning.</p>

<ul class="abt-points">
  <li><b>Analytics &amp; Automation</b> — Python (Pandas, NumPy, Prophet, XGBoost), SQL, Google Apps Script; engineered a <b>6-module ERP</b> on Google Sheets that eliminated 20+ hours of manual work per week across the entire ops team.</li>
  <li><b>Visualization &amp; Reporting</b> — Power BI, Looker Studio, Streamlit; designed multi-platform e-commerce reporting aggregating data from four marketplaces into one live view.</li>
  <li><b>Data Platforms &amp; AI</b> — BigQuery, GCP, MySQL; prompt engineering and AI-assisted development with Claude &amp; Gemini to accelerate delivery and problem-solving.</li>
</ul>

<p>At <b>Baaori Bazaar</b> (Founder's Office), I built the company's entire data infrastructure from the ground up — QC workflows, production tracking, inventory management, and order operations — while leading a 2-person analyst team. Before that, at <b>SAADAA</b>, I cut reporting effort by 40% through automated pipelines and built the dashboards leadership used to run weekly business reviews.</p>

<p>I'm actively looking for <b>Data Analyst, MIS Analyst, or Business Analyst</b> roles in Jaipur, Noida, or Pune — ideally somewhere I can keep building things that matter.</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

_dakshina_b64 = img_to_b64("assets/dakshina_logo.png")
if _dakshina_b64:
    dakshina_logo_html = f'<div class="exp-logo-img"><img src="data:image/png;base64,{_dakshina_b64}" alt="Dakshina"/></div>'
else:
    dakshina_logo_html = '<div class="exp-logo" style="background:rgba(168,85,247,0.12);color:#a855f7;border-color:rgba(168,85,247,0.3);">D</div>'

st.markdown(f"""
<div class="exp-container">

  <!-- Baaori Bazaar -->
  <div class="exp-card">
    <div class="exp-accent-bar" style="background:linear-gradient(to bottom,#10b981,rgba(16,185,129,0.05));"></div>
    <div class="exp-inner">
      <div class="exp-header">
        <div class="exp-logo" style="background:rgba(16,185,129,0.12);color:#10b981;border:1px solid rgba(16,185,129,0.3);width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-size:18px;font-weight:800;flex-shrink:0;">B</div>
        <div class="exp-header-text">
          <div class="exp-role">Data Analyst</div>
          <div class="exp-sub-role">Founder's Office</div>
          <div class="exp-company-row">
            <span class="exp-company" style="color:#34d399;">Baaori Bazaar</span>
            <span class="exp-type-badge" style="background:rgba(16,185,129,0.1);border-color:rgba(16,185,129,0.3);color:#6ee7b7;">Full-time</span>
          </div>
        </div>
        <div class="exp-date-block">
          <div class="exp-date">Apr 2026 — Present</div>
          <div class="exp-duration" style="color:#10b981;font-weight:600;">Current</div>
        </div>
      </div>
      <div class="exp-impact-row">
        <div class="exp-impact-chip" style="border-color:rgba(16,185,129,0.3);background:rgba(16,185,129,0.07);">
          <span class="chip-num" style="color:#34d399;">6</span>
          <span class="chip-label">ERP Modules</span>
        </div>
        <div class="exp-impact-chip" style="border-color:rgba(16,185,129,0.3);background:rgba(16,185,129,0.07);">
          <span class="chip-num" style="color:#34d399;">20+ Hrs</span>
          <span class="chip-label">Saved Weekly</span>
        </div>
        <div class="exp-impact-chip" style="border-color:rgba(16,185,129,0.3);background:rgba(16,185,129,0.07);">
          <span class="chip-num" style="color:#34d399;">2</span>
          <span class="chip-label">Analysts Led</span>
        </div>
      </div>
      <ul class="exp-points">
        <li>Built a <b>6-module ERP system</b> on Google Sheets + Apps Script covering QC management, production tracking, raw materials, and order management — saving 20+ hours per week.</li>
        <li>Designed and own end-to-end <b>e-commerce reporting</b> across four platforms with automated upsert and dispatch tracking.</li>
        <li>Created a <b>BOM (Bill of Materials)</b> system integrated with raw material stock, Ward-wise inventory tracking, and ROL alerts to prevent production stoppages.</li>
        <li>Built a Production WebApp tracking batch flow through RECEIVED → CUTTING → STITCHING → IRONING → DONE with tailor/cutting master assignments and split-batch logic.</li>
        <li>Lead and mentor <b>2 junior analysts</b>, defining data workflows and quality standards across the team.</li>
      </ul>
      <div class="exp-tools-row">
        <span>Google Apps Script</span><span>Google Sheets</span><span>Shopify</span>
        <span>SQL</span><span>ERP Design</span><span>BOM</span><span>E-commerce Analytics</span>
      </div>
    </div>
  </div>

  <!-- SAADAA -->
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

  <!-- Dakshina -->
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
          <div class="exp-date">Jul 2022 — May 2025</div>
          <div class="exp-duration">2 yrs 10 months</div>
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

# ── PROJECTS ─────────────────────────────────────────────────────────────────
st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#64748b;font-size:14px;margin:-10px 0 28px;">Click any card to explore details</p>', unsafe_allow_html=True)

fc_b64   = img_to_b64("assets/forecasting.png")
sd_b64   = img_to_b64("assets/sales_dashboard.png")
sql_b64  = img_to_b64("assets/sql_preview.png")
case_b64 = img_to_b64("assets/sql_project_slides.pdf")

fc_src   = f"data:image/png;base64,{fc_b64}"   if fc_b64   else ""
sd_src   = f"data:image/png;base64,{sd_b64}"   if sd_b64   else ""
sql_src  = f"data:image/png;base64,{sql_b64}"  if sql_b64  else ""
case_src = f"data:application/pdf;base64,{case_b64}" if case_b64 else ""

st.markdown(f"""
<style>
.proj-grid-6 {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  max-width: 1060px;
  margin: 0 auto;
}}
.pcard {{
  position: relative;
  background: #0b162c;
  border: 1px solid rgba(59,130,246,0.18);
  border-radius: 16px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  min-height: 260px;
  display: flex;
  flex-direction: column;
}}
.pcard:hover {{
  transform: translateY(-5px);
  box-shadow: 0 16px 40px rgba(59,130,246,0.2);
  border-color: rgba(59,130,246,0.5);
}}
.pcard-banner {{
  height: 130px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 52px;
  flex-shrink: 0;
}}
.pcard-banner img {{
  width: 100%; height: 100%;
  object-fit: cover;
  border-radius: 0 !important;
  border: none !important;
  display: block;
}}
.pcard-body {{
  padding: 14px 16px 16px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 7px;
}}
.pcard-tags {{ display: flex; flex-wrap: wrap; gap: 5px; }}
.pcard-tags span {{
  background: rgba(59,130,246,0.08);
  border: 1px solid rgba(59,130,246,0.25);
  color: #93c5fd;
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 20px;
  font-weight: 500;
}}
.pcard-title {{
  font-family: 'Syne', sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: #f1f5f9;
  line-height: 1.3;
}}
.pcard-desc {{
  font-size: 12px;
  color: #64748b;
  line-height: 1.55;
  flex: 1;
}}
.pcard-hint {{
  font-size: 10px;
  color: #334155;
  display: flex;
  align-items: center;
  gap: 4px;
  margin-top: 4px;
}}
@media (max-width: 900px) {{ .proj-grid-6 {{ grid-template-columns: repeat(2,1fr); }} }}
@media (max-width: 560px) {{ .proj-grid-6 {{ grid-template-columns: 1fr; }} }}
</style>

<div class="proj-grid-6">

  <div class="pcard" data-proj="0">
    <div class="pcard-banner" style="background:linear-gradient(135deg,#0a1628,#0d1f3c);">
      {"<img src='" + fc_src + "' alt='Forecasting'/>" if fc_src else '<i class="fas fa-chart-line" style="color:#3b82f6;"></i>'}
    </div>
    <div class="pcard-body">
      <div class="pcard-tags"><span>Python</span><span>Prophet</span><span>ML</span><span>Streamlit</span></div>
      <div class="pcard-title">Demand Forecasting Engine</div>
      <div class="pcard-desc">Hybrid SKU-level forecasting using statistical models &amp; Facebook Prophet — live Streamlit app.</div>
      <div class="pcard-hint"><i class="fas fa-hand-pointer"></i> Click to explore</div>
    </div>
  </div>

  <div class="pcard" data-proj="1">
    <div class="pcard-banner" style="background:linear-gradient(135deg,#0a0f28,#1a0f3c);">
      {"<img src='" + sd_src + "' alt='Sales Dashboard'/>" if sd_src else '<i class="fas fa-chart-bar" style="color:#a855f7;"></i>'}
    </div>
    <div class="pcard-body">
      <div class="pcard-tags"><span>Power BI</span><span>DAX</span><span>Power Query</span><span>KPI</span></div>
      <div class="pcard-title">Sales Analytics Dashboard</div>
      <div class="pcard-desc">Interactive KPI dashboard tracking revenue, returns &amp; regional growth trends in Power BI.</div>
      <div class="pcard-hint"><i class="fas fa-hand-pointer"></i> Click to explore</div>
    </div>
  </div>

  <div class="pcard" data-proj="2">
    <div class="pcard-banner" style="background:linear-gradient(135deg,#0a1628,#0c2a1c);">
      <i class="fas fa-sitemap" style="color:#10b981;"></i>
    </div>
    <div class="pcard-body">
      <div class="pcard-tags"><span>Apps Script</span><span>Google Sheets</span><span>ERP</span><span>BOM</span></div>
      <div class="pcard-title">Baaori Bazaar ERP System</div>
      <div class="pcard-desc">6-module ERP built from scratch: QC, Production, BOM, Inventory &amp; Order management.</div>
      <div class="pcard-hint"><i class="fas fa-hand-pointer"></i> Click to explore</div>
    </div>
  </div>

  <div class="pcard" data-proj="3">
    <div class="pcard-banner" style="background:linear-gradient(135deg,#0f1a0a,#1a2a0a);">
      <i class="fas fa-store" style="color:#f59e0b;"></i>
    </div>
    <div class="pcard-body">
      <div class="pcard-tags"><span>Apps Script</span><span>Shopify</span><span>Looker Studio</span><span>SQL</span></div>
      <div class="pcard-title">Multi-Platform E-commerce Reporting</div>
      <div class="pcard-desc">Unified order reporting across 4 marketplaces with automated upsert, dispatch join &amp; daily summaries.</div>
      <div class="pcard-hint"><i class="fas fa-hand-pointer"></i> Click to explore</div>
    </div>
  </div>

  <div class="pcard" data-proj="4">
    <div class="pcard-banner" style="background:linear-gradient(135deg,#0f0a20,#1a0d30);">
      {"<img src='" + sql_src + "' alt='SQL Preview'/>" if sql_src else '<i class="fas fa-database" style="color:#a855f7;"></i>'}
    </div>
    <div class="pcard-body">
      <div class="pcard-tags"><span>SQL</span><span>BigQuery</span><span>Business Analysis</span><span>KPI</span></div>
      <div class="pcard-title">Business Analysis Case Study</div>
      <div class="pcard-desc">End-to-end SQL project: data extraction, KPI analysis, ERD design, and executive slide deck.</div>
      <div class="pcard-hint"><i class="fas fa-hand-pointer"></i> Click to explore</div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── Modal + JS ────────────────────────────────────────────────────────────────
_case_dl = (
    f'<a href="{case_src}" download="Mann_SQL_Case_Study.pdf" '
    'class="pmodal-btn secondary" style="display:inline-flex;align-items:center;gap:7px;'
    'padding:9px 18px;border-radius:9px;font-size:13px;font-weight:600;text-decoration:none;'
    'border:1px solid rgba(59,130,246,0.35);color:#93c5fd;background:transparent;">'
    '<i class="fas fa-download"></i> Download Case Study PDF</a>'
) if case_src else ""

components.html(f"""
<script>
(function() {{
  var parentDoc = window.parent.document;

  if (!parentDoc.getElementById('pmodal-styles')) {{
    var s = parentDoc.createElement('style');
    s.id = 'pmodal-styles';
    s.textContent = `
      .pmodal-backdrop {{
        display: none;
        position: fixed;
        inset: 0;
        background: rgba(2,6,23,0.9);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        z-index: 999999;
        align-items: center;
        justify-content: center;
        padding: 20px;
        font-family: 'DM Sans', sans-serif;
      }}
      .pmodal-backdrop.open {{ display: flex; }}
      .pmodal {{
        background: #0b162c;
        border: 1px solid rgba(59,130,246,0.4);
        border-radius: 20px;
        max-width: 680px;
        width: 100%;
        max-height: 85vh;
        overflow-y: auto;
        box-shadow: 0 24px 80px rgba(0,0,0,0.7);
        position: relative;
        animation: pmodalIn 0.25s ease;
      }}
      @keyframes pmodalIn {{
        from {{ opacity:0; transform:translateY(24px) scale(0.96); }}
        to   {{ opacity:1; transform:translateY(0)    scale(1); }}
      }}
      .pmodal::-webkit-scrollbar {{ width: 4px; }}
      .pmodal::-webkit-scrollbar-track {{ background: transparent; }}
      .pmodal::-webkit-scrollbar-thumb {{ background: rgba(59,130,246,0.3); border-radius: 4px; }}
      .pmodal-header {{
        padding: 24px 28px 0;
        display: flex;
        align-items: flex-start;
        gap: 16px;
      }}
      .pmodal-icon {{
        font-size: 30px;
        width: 56px; height: 56px;
        border-radius: 14px;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
      }}
      .pmodal-title {{
        font-family: 'Syne', sans-serif;
        font-size: 19px;
        font-weight: 800;
        color: #f1f5f9;
        margin: 0 0 4px;
        line-height: 1.25;
      }}
      .pmodal-subtitle {{ font-size: 12px; color: #64748b; margin: 0; }}
      .pmodal-close {{
        position: absolute;
        top: 14px; right: 16px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        color: #94a3b8;
        width: 30px; height: 30px;
        border-radius: 50%;
        font-size: 14px;
        cursor: pointer;
        display: flex; align-items: center; justify-content: center;
        transition: all 0.2s;
        line-height: 1;
      }}
      .pmodal-close:hover {{ background:rgba(239,68,68,0.15); color:#f87171; border-color:rgba(239,68,68,0.3); }}
      .pmodal-divider {{ height:1px; background:rgba(59,130,246,0.12); margin:14px 0; }}
      .pmodal-body {{ padding: 16px 28px 28px; }}
      .pmodal-tags {{ display:flex; flex-wrap:wrap; gap:6px; margin-bottom:14px; }}
      .pmodal-tags span {{
        background:rgba(59,130,246,0.1);
        border:1px solid rgba(59,130,246,0.3);
        color:#60a5fa;
        font-size:11px;
        padding:3px 10px;
        border-radius:20px;
        font-weight:500;
      }}
      .pmodal-desc {{
        font-size:13.5px; color:#cbd5e1;
        line-height:1.75; margin-bottom:16px;
      }}
      .pmodal-section-label {{
        font-size:10px;
        text-transform:uppercase;
        letter-spacing:1.2px;
        color:#475569;
        font-weight:600;
        margin: 18px 0 8px;
      }}
      .pmodal-points {{
        list-style:none; padding:0; margin:0 0 20px;
        display:flex; flex-direction:column; gap:9px;
      }}
      .pmodal-points li {{
        font-size:13px; color:#94a3b8;
        padding-left:18px; position:relative; line-height:1.6;
      }}
      .pmodal-points li::before {{ content:'▸'; position:absolute; left:0; color:#3b82f6; }}
      .pmodal-points li b {{ color:#cbd5e1; }}
      .pmodal-actions {{ display:flex; gap:10px; flex-wrap:wrap; }}
      .pmodal-btn-primary {{
        display:inline-flex; align-items:center; gap:7px;
        padding:9px 18px; border-radius:9px;
        font-size:13px; font-weight:600;
        text-decoration:none;
        background:#3b82f6; color:white;
        border:none;
        box-shadow:0 4px 14px rgba(59,130,246,0.3);
        cursor:pointer; transition:background 0.2s;
      }}
      .pmodal-btn-primary:hover {{ background:#2563eb; }}
      .pmodal-highlight-box {{
        background: rgba(16,185,129,0.06);
        border: 1px solid rgba(16,185,129,0.2);
        border-radius: 10px;
        padding: 14px 16px;
        margin-bottom: 16px;
        font-size: 13px;
        color: #6ee7b7;
        line-height: 1.65;
      }}
      .pmodal-highlight-box strong {{
        color: #34d399;
        font-weight: 700;
      }}
      .pmodal-module-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 16px;
      }}
      .pmodal-module-card {{
        background: rgba(59,130,246,0.05);
        border: 1px solid rgba(59,130,246,0.15);
        border-radius: 10px;
        padding: 12px 14px;
      }}
      .pmodal-module-card .mod-title {{
        font-family: 'Syne', sans-serif;
        font-size: 12px;
        font-weight: 700;
        color: #60a5fa;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        gap: 6px;
      }}
      .pmodal-module-card .mod-desc {{
        font-size: 11.5px;
        color: #64748b;
        line-height: 1.55;
      }}
    `;
    parentDoc.head.appendChild(s);
  }}

  if (!parentDoc.getElementById('projModal')) {{
    var backdrop = parentDoc.createElement('div');
    backdrop.className = 'pmodal-backdrop';
    backdrop.id = 'projModal';
    backdrop.innerHTML = `
      <div class="pmodal" id="projModalBox">
        <button class="pmodal-close" id="pmodalClose">✕</button>
        <div class="pmodal-header">
          <div class="pmodal-icon" id="mIcon"></div>
          <div style="flex:1;min-width:0;">
            <div class="pmodal-title" id="mTitle"></div>
            <div class="pmodal-subtitle" id="mSubtitle"></div>
          </div>
        </div>
        <div class="pmodal-body">
          <div class="pmodal-tags" id="mTags"></div>
          <div class="pmodal-divider"></div>
          <div id="mContent"></div>
          <div class="pmodal-actions" id="mActions"></div>
        </div>
      </div>
    `;
    parentDoc.body.appendChild(backdrop);
    backdrop.addEventListener('click', function(e) {{
      if (e.target === backdrop) closeModal();
    }});
    parentDoc.getElementById('pmodalClose').addEventListener('click', closeModal);
    parentDoc.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') closeModal();
    }});
  }}

  function closeModal() {{
    var b = parentDoc.getElementById('projModal');
    if (b) b.classList.remove('open');
    parentDoc.body.style.overflow = '';
  }}

  var projects = [
    {{
      icon: '<i class="fas fa-chart-line" style="color:#3b82f6;font-size:28px;"></i>',
      iconBg: 'rgba(59,130,246,0.12)',
      title: 'Demand Forecasting Engine',
      subtitle: 'Python · Prophet · Machine Learning · Streamlit',
      tags: ['Python','Prophet','SARIMA','XGBoost','Streamlit','Pandas','NumPy'],
      content: `
        <div class="pmodal-desc">A hybrid SKU-level demand forecasting engine combining SARIMA, Facebook Prophet, and XGBoost to generate accurate multi-horizon forecasts — deployed as a live interactive Streamlit web app.</div>
        <ul class="pmodal-points">
          <li>Compared SARIMA, Prophet, and XGBoost across multiple SKUs to select best-fit model per product</li>
          <li>Built an interactive Streamlit UI where users can select SKU, forecast horizon, and model type</li>
          <li>Visualised forecast vs actuals with confidence intervals and error metrics (MAE, RMSE)</li>
          <li>Deployed on Streamlit Cloud — accessible without any local setup</li>
        </ul>
      `,
      actionHtml: '<a href="https://demand-forecasting-engine-o22shix3vgbi5jgrvi4abg.streamlit.app/" target="_blank" class="pmodal-btn-primary"><i class="fas fa-external-link-alt"></i> View Live App</a>'
    }},
    {{
      icon: '<i class="fas fa-chart-bar" style="color:#a855f7;font-size:28px;"></i>',
      iconBg: 'rgba(168,85,247,0.12)',
      title: 'Sales Analytics Dashboard',
      subtitle: 'Power BI · DAX · Power Query · KPI Tracking',
      tags: ['Power BI','Power Query','DAX','KPI','Data Modelling','Excel'],
      content: `
        <div class="pmodal-desc">An interactive Power BI dashboard giving business leadership a real-time view of sales performance, regional trends, and return rates — replacing manual Excel reports with a live filterable dashboard.</div>
        <ul class="pmodal-points">
          <li>Cleaned and transformed raw sales data using Power Query — handled nulls, type mismatches, and duplicates</li>
          <li>Built a star-schema data model connecting sales, product, region, and time tables</li>
          <li>Created DAX measures for YoY growth, running totals, return rate %, and region-wise contribution</li>
          <li>Designed an interactive layout with slicers for date range, product category, and region</li>
        </ul>
      `,
      actionHtml: ''
    }},
    {{
      icon: '<i class="fas fa-sitemap" style="color:#10b981;font-size:28px;"></i>',
      iconBg: 'rgba(16,185,129,0.12)',
      title: 'Baaori Bazaar ERP System',
      subtitle: 'Google Apps Script · Google Sheets · 6 Modules · Built from Scratch',
      tags: ['Google Apps Script','Google Sheets','ERP','BOM','QC','Automation','WebApp','Inventory'],
      content: `
        <div class="pmodal-highlight-box">
          <strong>The problem:</strong> The entire company ran on WhatsApp messages and scattered spreadsheets. There was no system to track what fabric passed QC, which batches were in production, what stock was available, or which orders were ready to dispatch. I built one — from scratch.
        </div>
        <div class="pmodal-desc">
          A fully custom, 6-module ERP system built on Google Sheets + Google Apps Script for a growing fashion brand. This replaced informal, error-prone WhatsApp-based workflows with structured, automated systems that the entire operations team now depends on daily — saving <strong style="color:#34d399;">20+ hours per week</strong> across the business.
        </div>
        <div class="pmodal-section-label">The 6 Modules</div>
        <div class="pmodal-module-grid">
          <div class="pmodal-module-card">
            <div class="mod-title"><i class="fas fa-search-plus"></i> QC Management</div>
            <div class="mod-desc">Three-stage quality control: Raw Fabric QC, Production QC, and Pre-Dispatch QC. Each stage has its own pass/fail tracking, rejection logging, and status dashboard — so nothing slips through unchecked.</div>
          </div>
          <div class="pmodal-module-card">
            <div class="mod-title"><i class="fas fa-industry"></i> Production Tracker</div>
            <div class="mod-desc">A WebApp that tracks every batch through 5 production stages: RECEIVED → CUTTING → STITCHING → IRONING → DONE. Supports tailor & cutting master assignments, split-batch logic, and live stage visibility.</div>
          </div>
          <div class="pmodal-module-card">
            <div class="mod-title"><i class="fas fa-boxes"></i> BOM & Raw Materials</div>
            <div class="mod-desc">A Bill of Materials system linked directly to raw material stock. When a production batch is created, the BOM auto-calculates fabric consumption, deducts from live inventory, and triggers ROL (Reorder Level) alerts before stock runs out.</div>
          </div>
          <div class="pmodal-module-card">
            <div class="mod-title"><i class="fas fa-warehouse"></i> Inventory (Ward System)</div>
            <div class="mod-desc">Ward-wise inventory tracking across multiple storage locations. Stock movements — inward, outward, transfers — are logged in real time and always reconciled against the BOM consumption records.</div>
          </div>
          <div class="pmodal-module-card">
            <div class="mod-title"><i class="fas fa-shopping-cart"></i> Order Management</div>
            <div class="mod-desc">A WebApp that imports Shopify orders, runs priority-based stock allocation logic, and generates dispatch-ready picking sheets — replacing a fully manual process that previously took hours each day.</div>
          </div>
          <div class="pmodal-module-card">
            <div class="mod-title"><i class="fas fa-link"></i> Cross-Module Sync</div>
            <div class="mod-desc">All modules are connected. A finished production batch automatically updates inventory. An allocated order pulls from live stock. BOM consumption reflects immediately in raw material levels. Nothing is siloed.</div>
          </div>
        </div>
        <div class="pmodal-section-label">What this replaced</div>
        <ul class="pmodal-points">
          <li><b>Before:</b> QC status tracked in WhatsApp groups — no history, no accountability</li>
          <li><b>Before:</b> Production stages tracked in memory or verbal updates — batches were lost, delays went unnoticed</li>
          <li><b>Before:</b> Raw material stock counted manually — no reorder alerts, frequent production stoppages</li>
          <li><b>Before:</b> Orders managed in Excel files sent over WhatsApp — duplicate allocations, missed dispatches</li>
        </ul>
        <div class="pmodal-section-label">Impact</div>
        <ul class="pmodal-points">
          <li>Saved <b>20+ hours per week</b> across the operations team by eliminating manual tracking and WhatsApp coordination</li>
          <li>Zero production stoppages due to raw material stockouts since ROL alerts went live</li>
          <li>Full traceability from fabric purchase to finished order — something the company never had before</li>
          <li>The entire ops team (production, QC, warehouse, dispatch) now works from one connected system</li>
        </ul>
      `,
      actionHtml: ''
    }},
    {{
      icon: '<i class="fas fa-store" style="color:#f59e0b;font-size:28px;"></i>',
      iconBg: 'rgba(245,158,11,0.12)',
      title: 'Multi-Platform E-commerce Reporting',
      subtitle: 'Google Apps Script · Shopify · 4 Marketplaces',
      tags: ['Apps Script','Shopify','Looker Studio','SQL','Reporting','Automation'],
      content: `
        <div class="pmodal-desc">Automated reporting that aggregates daily orders from four platforms (Shopify, Amazon, Flipkart, Myntra) into one unified dashboard — eliminating all manual download-and-paste work.</div>
        <ul class="pmodal-points">
          <li>Built platform-specific parsers handling different date formats, ID types, and schemas per marketplace</li>
          <li>Implemented upsert logic using order line ID as the key — no duplicates on re-run</li>
          <li>Fixed scientific notation ID issue that was corrupting Flipkart order IDs in Google Sheets</li>
          <li>Automated dispatch sheet joins to flag shipped vs pending orders per platform</li>
          <li>Rebuilt PDF/email report export using server-side HTML generation</li>
          <li>Aggregated daily volume, revenue, returns, and fulfilment rate into a Looker Studio dashboard</li>
        </ul>
      `,
      actionHtml: ''
    }},
    {{
      icon: '<i class="fas fa-database" style="color:#a855f7;font-size:28px;"></i>',
      iconBg: 'rgba(168,85,247,0.12)',
      title: 'Business Analysis Case Study',
      subtitle: 'SQL · BigQuery · ERD · Executive Storytelling',
      tags: ['SQL','BigQuery','KPI Analysis','ERD','Business Analysis','Slide Deck'],
      content: `
        <div class="pmodal-desc">An end-to-end SQL business analysis project covering data extraction, transformation, KPI analysis, trend identification, and C-suite storytelling — with a full ERD and downloadable slide deck.</div>
        <ul class="pmodal-points">
          <li>Wrote complex SQL queries with multi-table joins, CTEs, window functions, and aggregations in BigQuery</li>
          <li>Designed a normalised Entity Relationship Diagram (ERD) documenting all table relationships</li>
          <li>Identified top-performing categories, seasonal trends, and underperforming product segments</li>
          <li>Built a slide deck with visual charts and narrative suitable for executive presentation</li>
        </ul>
      `,
      actionHtml: '{_case_dl}'
    }}
  ];

  function attachClicks() {{
    var cards = parentDoc.querySelectorAll('.pcard[data-proj]');
    cards.forEach(function(card) {{
      if (card.dataset.wired) return;
      card.dataset.wired = '1';
      card.addEventListener('click', function() {{
        var idx = parseInt(card.getAttribute('data-proj'));
        openProj(idx);
      }});
    }});
  }}

  function openProj(i) {{
    var p = projects[i];
    parentDoc.getElementById('mIcon').innerHTML = p.icon;
    parentDoc.getElementById('mIcon').style.background = p.iconBg;
    parentDoc.getElementById('mTitle').textContent = p.title;
    parentDoc.getElementById('mSubtitle').textContent = p.subtitle;
    parentDoc.getElementById('mTags').innerHTML = p.tags.map(function(t) {{
      return '<span>' + t + '</span>';
    }}).join('');
    parentDoc.getElementById('mContent').innerHTML = p.content;
    parentDoc.getElementById('mActions').innerHTML = p.actionHtml;
    parentDoc.getElementById('projModal').classList.add('open');
    parentDoc.body.style.overflow = 'hidden';
  }}

  attachClicks();
  setTimeout(attachClicks, 600);
  setTimeout(attachClicks, 1500);
}})();
</script>
""", height=0)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── SKILLS ───────────────────────────────────────────────────────────────────
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
    Node(id="Apps Script",        label="Apps Script",         size=45, shape="circle", color=colors["tech"],   font={"size": 8,  "color": "white"}),
    Node(id="ERP Design",         label="ERP Design",          size=45, shape="circle", color=colors["biz"],    font={"size": 8,  "color": "white"}),
    Node(id="Streamlit",          label="Streamlit",           size=45, shape="circle", color=colors["tech"],   font={"size": 8,  "color": "white"}),
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
    Edge(source="T",  target="Apps Script"),
    Edge(source="T",  target="Streamlit"),
    Edge(source="B",  target="ERP Design"),
]

config = Config(
    width=900,
    height=600,
    physics=True,
    nodeHighlightBehavior=True,
    collapsible=False,
)
agraph(nodes=nodes, edges=edges, config=config)

st.markdown('<div class="section-title" style="font-size:24px; margin-top:30px;">Core Skill Stack</div>', unsafe_allow_html=True)

tags = [
    "Data Analyst", "MIS Analyst", "Business Analyst",
    "Python", "SQL", "Google Apps Script", "Streamlit",
    "Power BI", "Looker Studio", "Tableau", "Excel", "Google Sheets",
    "BigQuery", "MySQL", "GCP",
    "Pandas", "NumPy", "Prophet", "XGBoost", "SARIMA",
    "ERP Design", "E-commerce Analytics", "Shopify", "BOM", "Inventory Management",
    "KPI Analysis", "Forecasting", "BRD / FRD", "Stakeholder Management",
    "Data Visualization", "Reporting Automation", "Agile"
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
      <div class="cert-title">Business Analyst Career Program</div>
      <div class="cert-issuer">Skill Academy by Testbook</div>
      <div class="cert-status completed">Completed</div>
    </div>
  </div>
  <div class="cert-card">
    <div class="cert-icon" style="color:#a855f7;"><i class="fas fa-brain"></i></div>
    <div class="cert-body">
      <div class="cert-title">Data Science</div>
      <div class="cert-issuer">Tutedude</div>
      <div class="cert-status in-progress">In Progress</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────────────────────────
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; color:#94a3b8; margin-bottom:10px; font-size:16px;">
  Open to Data Analyst, MIS Analyst, and Business Analyst roles.
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
  <p>Built with love using Python &amp; Streamlit &nbsp;&bull;&nbsp; Mann Choudhary 2026</p>
</div>
""", unsafe_allow_html=True)

# ── FLOATING ACTION BAR ───────────────────────────────────────────────────────
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
    body.light-theme .fixed-navbar {{
      background: rgba(241,245,249,0.97) !important;
      border-bottom: 1px solid rgba(59,130,246,0.2) !important;
    }}
    body.light-theme .fixed-navbar a {{ color: #475569 !important; }}
    body.light-theme .fixed-navbar a:hover {{ color: #2563eb !important; border-bottom-color: #2563eb !important; }}
    body.light-theme,
    body.light-theme [data-testid="stAppViewContainer"],
    body.light-theme [data-testid="stApp"],
    body.light-theme .block-container {{
      background-color: #f1f5f9 !important;
      color: #0f172a !important;
    }}
    body.light-theme .metrics {{ background: #ffffff !important; border-color: rgba(59,130,246,0.15) !important; }}
    body.light-theme .metric-item h3 {{ color: #2563eb !important; }}
    body.light-theme .metric-item p  {{ color: #64748b !important; }}
    body.light-theme .exp-card {{ background: #ffffff !important; border-color: rgba(59,130,246,0.15) !important; }}
    body.light-theme .exp-role {{ color: #0f172a !important; }}
    body.light-theme .exp-points li {{ color: #334155 !important; }}
    body.light-theme .pcard {{ background: #ffffff !important; border-color: rgba(59,130,246,0.15) !important; }}
    body.light-theme .pcard-title {{ color: #0f172a !important; }}
    body.light-theme .cert-card {{ background: #ffffff !important; border-color: rgba(59,130,246,0.15) !important; }}
    body.light-theme .cert-title {{ color: #0f172a !important; }}
    body.light-theme .contact-card {{ background: #ffffff !important; border-color: rgba(59,130,246,0.15) !important; }}
    body.light-theme .contact-value {{ color: #0f172a !important; }}
    body.light-theme .section-title {{ color: #0f172a !important; }}
    body.light-theme .tag {{ background: #ffffff !important; border-color: #cbd5e1 !important; color: #334155 !important; }}
    body.light-theme .fab-btn {{ background: rgba(255,255,255,0.95) !important; border-color: rgba(59,130,246,0.25) !important; color: #475569 !important; }}
  `;
  parentDoc.head.appendChild(style);

  var bar = parentDoc.createElement('div');
  bar.className = 'fab-bar';

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

  var topBtn = parentDoc.createElement('button');
  topBtn.className = 'fab-btn';
  topBtn.innerHTML = '↑';
  topBtn.setAttribute('data-tip', 'Back to Top');
  topBtn.style.fontSize = '20px';
  topBtn.style.fontWeight = '700';
  topBtn.addEventListener('click', function() {{
    var selectors = [
      '[data-testid="stAppViewContainer"]',
      '[data-testid="stMainBlockContainer"]',
      '.main > div',
      '.block-container',
      'section.main',
      '.stApp',
      'main'
    ];
    for (var i = 0; i < selectors.length; i++) {{
      var el = parentDoc.querySelector(selectors[i]);
      if (el && el.scrollHeight > el.clientHeight) {{
        el.scrollTo({{ top: 0, behavior: 'smooth' }});
        break;
      }}
    }}
    var all = parentDoc.querySelectorAll('*');
    for (var j = 0; j < all.length; j++) {{
      if (all[j].scrollTop > 0) all[j].scrollTo({{ top: 0, behavior: 'smooth' }});
    }}
    parentDoc.documentElement.scrollTo({{ top: 0, behavior: 'smooth' }});
    parentDoc.body.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});

  var resumeBtn = parentDoc.createElement('a');
  resumeBtn.className = 'fab-btn';
  resumeBtn.innerHTML = '📄';
  resumeBtn.setAttribute('data-tip', 'Download Resume');
  resumeBtn.href = 'data:application/pdf;base64,' + resumeB64;
  resumeBtn.download = 'Mann_Choudhary_Resume.pdf';

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
