import streamlit as st

# ======================================
# PAGE CONFIGURATION
# ======================================
st.set_page_config(
    page_title="Genesis Digital",
    page_icon="🌐",
    layout="wide"
)

# ======================================
# GLOBAL CSS
# ======================================
st.markdown("""
<style>

/* GLOBAL SETTINGS */
.stApp {
    background-color: #eaeaea;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 0.5rem;
}

.stMarkdown, .stText, p, label, span {
    color: black;
}

a {
    color: blue !important;
}

/* HEADER */
.logo-row {
    display: flex;
    align-items: center;
    margin-bottom: -15px;
}

/* TOP MENU */
div[data-baseweb="tab-list"] {
    background-color: #0057b8;
    padding: 12px 20px;
    border-radius: 10px;
    gap: 35px;
    margin-top: 18px;
}

button[data-baseweb="tab"] {
    color: white !important;
    font-size: 18px;
    font-weight: bold;
    background: transparent !important;
    border: none !important;
    padding: 10px 16px;
    border-radius: 5px;
}

button[data-baseweb="tab"]:hover {
    background-color: red !important;
    transition: 0.3s;
}

button[aria-selected="true"] {
    background-color: #003f85 !important;
}

/* HOME CARDS */
.card {
    border: 2px solid #0dcfff;
    background: white;
    padding: 30px 25px;
    border-radius: 10px;
    min-height: 260px;
    margin-bottom: 20px;
}

.card-title {
    color: #0057b8 !important;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 18px;
}

.card-text {
    font-size: 18px;
    line-height: 1.8;
}

/* FOOTER */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: blue;
    text-align: center;
    padding: 10px;
    font-size: 13px;
    z-index: 999;
}

/* MOBILE */
@media only screen and (max-width: 768px) {

    .logo-row {
        flex-direction: column;
        align-items: flex-start;
    }

    img {
        width: 90px !important;
    }

    div[data-baseweb="tab-list"] {
        flex-wrap: wrap !important;
        gap: 10px !important;
        padding: 10px !important;
    }

    button[data-baseweb="tab"] {
        font-size: 14px !important;
        padding: 8px 10px !important;
    }

    .card-title {
        font-size: 22px !important;
    }

    .card-text {
        font-size: 15px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER
# ======================================
col1, col2 = st.columns([1, 8])

with col1:
    st.image("logo.png", width=120)

# ======================================
# TOP MENU
# ======================================
with col2:
    tabs = st.tabs([
        "Home",
        "AI Analyzer",
        "Our Services",
        "About",
        "Contact"
    ])

# ======================================
# HOME PAGE
# ======================================
with tabs[0]:

    st.markdown("### OUR EDGE")
    st.markdown("# Why Genesis Digital Stands Out")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Art Meets Technology</div>
            <div class="card-text">
                We fuse creative storytelling with cutting-edge digital infrastructure.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Industry Expertise</div>
            <div class="card-text">
                Deep domain knowledge across hospitality, travel, and digital media.
            </div>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">Client-Centric Approach</div>
            <div class="card-text">
                Every project is custom-architected to your needs.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-title">Scalable Execution</div>
            <div class="card-text">
                From small to large scale video production seamlessly.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ======================================
# AI ANALYZER PAGE
# ======================================
with tabs[1]:

    # CUSTOM BUTTON CSS
    st.markdown("""
    <style>

    /* BUTTON STYLE */
    div.stButton > button {
        background-color: #0057b8 !important;
        font-color: white !important;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        width: 150%;
        height: 50px;
        margin-bottom: 20px;
        transition: 0.3s;
    }

    /* HOVER EFFECT */
    div.stButton > button:hover {
        background-color: red !important;
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.write("Choose an AI Tool Below")

    # LEFT AND RIGHT LAYOUT
    left_col, right_col = st.columns([1, 3])

    # =========================
    # LEFT SIDE BUTTONS
    # =========================
    with left_col:

        profile_clicked = st.button("Profile Finder")

        video_clicked = st.button("Analyze a Video")

    # =========================
    # RIGHT SIDE RESULTS
    # =========================
    with right_col:

        if profile_clicked:
            st.subheader("Profile Finder")
            st.write("Profile Finder Selected")

        elif video_clicked:
            st.subheader("Analyze a Video")
            st.write("Analyze a Video Selected")

# ======================================
# SERVICES PAGE
# ======================================
with tabs[2]:

    st.title("Our Services")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Video Sourcing")

    with col2:
        st.subheader("AI Solutions")

    with col3:
        st.subheader("Data Analysis")

# ======================================
# ABOUT PAGE
# ======================================
with tabs[3]:

    st.title("About Us")
    st.write("AI, Automation, and Digital Solutions Company.")

# ======================================
# CONTACT PAGE
# ======================================
with tabs[4]:

    st.title("Contact Us")
    st.write("📧 mose@genesisdigital.in")
    st.write("📞 +254748468634")

# ======================================
# FOOTER
# ======================================
st.markdown("""
<div class="footer">
    © 2026 Genesis Digital | All Rights Reserved
</div>
""", unsafe_allow_html=True)
