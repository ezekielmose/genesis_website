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
# CUSTOM CSS
# ======================================
st.markdown("""
<style>

/* =====================================
   GLOBAL SETTINGS
===================================== */

.stApp {
    background-color: #eaeaea;
}

/* Hide Streamlit Items */
#MainMenu,
footer,
header {
    visibility: hidden;
}

/* Reduce top spacing */
.block-container {
    padding-top: 0.5rem;
}

/* Default Streamlit text */
.stMarkdown,
.stText,
p,
label,
span {
    color: black;
}

/* Keep links blue */
a {
    color: blue !important;
}

/* =====================================
   HEADER ALIGNMENT
===================================== */

.logo-row {
    display: flex;
    align-items: center;
    margin-bottom: -15px;
}

.logo-container img {
    margin-top: 0px;
}

/* =====================================
   TOP MENU BAR
===================================== */

div[data-baseweb="tab-list"] {
    background-color: #0057b8;
    padding: 12px 20px;
    border-radius: 10px;
    align-items: center;
    gap: 35px;
    margin-top: 18px;
}

/* Menu Buttons */
button[data-baseweb="tab"] {
    color: white !important;
    font-size: 18px;
    font-weight: bold;
    background-color: transparent !important;
    border: none !important;
    padding: 10px 16px;
    border-radius: 5px;
}

/* Hover Effect */
button[data-baseweb="tab"]:hover {
    background-color: red !important;
    color: white !important;
    transition: 0.3s;
}

/* Active Menu */
button[aria-selected="true"] {
    background-color: #003f85 !important;
    color: white !important;
}

/* =====================================
   COMING SOON SECTION
===================================== */

.coming-soon {
    text-align: center;
    font-size: 70px;
    font-weight: bold;
    color: #0057b8;
    margin-top: 140px;
}

.sub-text {
    text-align: center;
    font-size: 28px;
    color: black;
    margin-top: 20px;
}

/* =====================================
   SUBMENU
===================================== */

.submenu-title {
    color: #0057b8;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* =====================================
   MOBILE RESPONSIVENESS FIX
===================================== */

@media only screen and (max-width: 768px) {

    /* Stack logo and menu nicely */
    .logo-row {
        flex-direction: column;
        align-items: flex-start;
    }

    /* Reduce logo size on mobile */
    img {
        width: 90px !important;
    }

    /* Make tabs wrap instead of overflow */
    div[data-baseweb="tab-list"] {
        flex-wrap: wrap !important;
        gap: 10px !important;
        padding: 10px !important;
    }

    /* Smaller menu buttons */
    button[data-baseweb="tab"] {
        font-size: 14px !important;
        padding: 8px 10px !important;
    }

    /* Prevent horizontal scrolling */
    html, body {
        overflow-x: hidden;
    }

    /* Reduce big headings */
    .coming-soon {
        font-size: 50px !important;
    }

    .sub-text {
        font-size: 18px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER SECTION
# ======================================
col1, col2 = st.columns([1, 8])

with col1:
    st.image("logo.png", width=120)

# ======================================
# HORIZONTAL MENU
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

    # HOME CSS
    st.markdown("""
    <style>

    .home-wrapper {
        background: linear-gradient(to right, #020d2b, #031a52);
        padding: 40px 30px;
        border-radius: 14px;
        margin-top: 20px;
    }

    .mini-title {
        text-align: center;
        color: #00d9ff !important;
        font-size: 14px;
        font-weight: bold;
        letter-spacing: 4px;
    }

    .main-title {
        text-align: center;
        color: #00d9ff !important;
        font-size: 52px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .line {
        width: 130px;
        height: 4px;
        background-color: #00d9ff;
        margin: auto;
        border-radius: 20px;
        margin-bottom: 40px;
    }

    /* CARD DESIGN */

    .card {
        border: 2px solid #0dcfff;
        background-color: white;
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
        color: black !important;
        font-size: 18px;
        line-height: 1.8;
    }

    @media only screen and (max-width: 768px) {

        .main-title {
            font-size: 34px !important;
        }

        .card {
            min-height: auto;
            padding: 24px 20px;
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

    # OPEN MAIN SECTION
    # st.markdown('<div class="home-wrapper">', unsafe_allow_html=True)

    # TITLES
    st.markdown(
        '<div class="mini-title">OUR EDGE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-title">Why Genesis Digital Stands Out</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="line"></div>',
        unsafe_allow_html=True
    )

    # FIRST ROW
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="card-title">Art Meets Technology</div>
                <div class="card-text">
                    We fuse creative storytelling with cutting-edge digital
                    infrastructure to produce content that captivates and converts.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # FIRST ROW
    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="card-title">Industry Expertise</div>
                <div class="card-text">
                    Our team brings deep domain knowledge across hospitality,
                    travel, and digital media, ensuring every project exceeds
                    industry benchmarks.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # SECOND ROW
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="card-title">Client-Centric Approach</div>
                <div class="card-text">
                    Every partnership is custom-architected. We adapt to your
                    vision, goals, and quality standards with precision and agility.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            """
            <div class="card">
                <div class="card-title">Scalable Execution</div>
                <div class="card-text">
                    From dozens to thousands of videos, our proven workflow scales
                    seamlessly — delivering consistent quality at any volume.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # CLOSE MAIN SECTION
    st.markdown('</div>', unsafe_allow_html=True)



# ======================================
# AI ANALYZER PAGE
# ======================================


# ======================================
# OUR SERVICES PAGE
# ======================================
with tabs[2]:

    st.title("Our Services")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Videos Sourcing")
        st.write("We specialize in videos sourcing meeting the suggested guidelines.")

    with col2:
        st.subheader("AI Solutions")
        st.write("AI-powered business tools.")

    with col3:
        st.subheader("Data Analysis")
        st.write("Professional data insights.")

# ======================================
# ABOUT PAGE
# ======================================
with tabs[3]:

    st.title("About Us")

    st.write("We are a technology company focused on:")

    st.write("- Artificial Intelligence")
    st.write("- Automation")
    st.write("- Videos Sourcing")

# ======================================
# CONTACT PAGE
# ======================================
with tabs[4]:

    st.title("Contact Us")

    st.write("📧 Email: mose@genesisdigital.in")
    st.write("📞 Phone: +254748468634")

# =================================
#FOOTER
#=============================
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: blue;
        font-color: white;
        text-align: center;
        padding: 10px;
        font-size: 13px;
        border-top: 1px solid #ddd;
        z-index: 999;
    }
    </style>

    <div class="footer">
        © 2026 Genesis Digital | All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True
)
