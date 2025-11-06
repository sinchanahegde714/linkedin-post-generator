import streamlit as st
from post_generator import generate_post

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="LinkedIn Post Generator 🚀",
    page_icon="🚀",
    layout="wide"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0a0f24 0%, #1a1449 50%, #0d0f2d 100%);
    font-family: 'Segoe UI', sans-serif;
}

div[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0f24 0%, #1a1449 50%, #0d0f2d 100%);
}

h1, label, .section-title {
    color: #ffffff !important;
}

.section-title {
    font-size: 32px; 
    font-weight: 700;
    margin-bottom: 10px;
}

p, .stMarkdown, .stText {
    color: #e6e6ff;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.45);
    border: 1px solid rgba(255,255,255,0.25);
    margin-top: 12px;
}

.stButton button {
    background: #5a2dd8 !important; 
    color: white !important;
    border-radius: 10px;
    height: 48px;
    border: none;
    font-size: 18px;
    font-weight: 600;
}

.stButton button:hover {
    background: #4319b8 !important;
    border: 1px solid #ffffff;
}

.header-box {
    text-align:center; 
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# ------------------- HEADER -------------------
st.markdown("""
<div class="header-box">
    <h1 style="font-size:42px; font-weight:800;">
        LinkedIn Post Generator 🚀
    </h1>
    <p style="font-size:18px; color:#bdbdfc;">
        Craft premium LinkedIn content that attracts employers & recruiters 🎯
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------- INPUT UI -------------------
topics = ["Productivity", "Leadership", "Career Advice", "AI", "Startups", "Motivation", "Learning", "Sapne"]
lengths = ["Short", "Medium", "Long"]

# ✅ Updated languages
languages = ["English", "Hindi", "Kannada"]

col1, col2, col3 = st.columns(3)

with col1:
    topic = st.selectbox("📌 Select Topic", topics)

with col2:
    length = st.selectbox("📝 Select Post Length", lengths)

with col3:
    language = st.selectbox("🌐 Select Language", languages)

generate = st.button("✨ Generate Post")

# ------------------- OUTPUT -------------------
if generate:
    result = generate_post(topic, length, language)

    st.markdown(f"<div class='card'><div class='section-title'>Generated Post 👇</div>", unsafe_allow_html=True)
    st.write(result["post"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card'>
        <div class='section-title'>🔥 Engagement Score</div>
        <p style='font-size:22px; font-weight:700; color:#c7b3ff;'>{result["engagement"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card'>
        <div class='section-title'>🔗 Hashtags</div>
        <p style='font-size:18px; font-weight:500; color:#e6e6ff;'>{' '.join(result["hashtags"])}</p>
    </div>
    """, unsafe_allow_html=True)
