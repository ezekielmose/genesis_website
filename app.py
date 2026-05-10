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
with tabs[1]:

    st.title("AI Analyzer")

    ai_menu = st.radio(
        "Select Analyzer",
        ["Profile Finder", "Reels Analyzer"],
        horizontal=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # PROFILE FINDER
    if ai_menu == "Profile Finder":

        st.markdown(
            "<div class='submenu-title'>Profile Finder</div>",
            unsafe_allow_html=True
        )

        st.write("Upload profile-related files for AI analysis.")

        uploaded_file = st.file_uploader(
            "Upload Profile File",
            type=["csv", "txt", "pdf"],
            key="profile"
        )

        if uploaded_file:
            st.success("Profile file uploaded successfully!")

    # REELS ANALYZER
    elif ai_menu == "Reels Analyzer":

        st.markdown(
            "<div class='submenu-title'>Reels Analyzer</div>",
            unsafe_allow_html=True
        )

        st.write("Upload reels data for AI-powered insights.")

        uploaded_file = st.file_uploader(
            "Upload Reels File",
            type=["mp4"],
            key="reels"
        )

        if uploaded_file:
            st.success("Reels file uploaded successfully!")

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
#===============================
# FOOTER
#===============================

st.markdown(
    """
    <style>
    .footer {
        background: linear-gradient(135deg, #0d47a1, #1565c0);
        color: white;
        padding: 40px 20px 20px 20px;
        margin-top: 60px;
        font-family: Arial, sans-serif;
    }

    .footer-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        max-width: 1100px;
        margin: auto;
        gap: 30px;
    }

    .footer-col {
        flex: 1;
        min-width: 200px;
    }

    .footer h3 {
        margin-bottom: 12px;
        font-size: 16px;
        color: #ffffff;
    }

    .footer a {
        display: block;
        color: #dbe9ff;
        text-decoration: none;
        margin: 6px 0;
        font-size: 14px;
        transition: 0.3s;
    }

    .footer a:hover {
        color: #ffffff;
        padding-left: 5px;
    }

    .social-icons {
        display: flex;
        gap: 12px;
        margin-top: 10px;
    }

    .social-icons a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: rgba(255,255,255,0.15);
        transition: 0.3s;
    }

    .social-icons a:hover {
        background: white;
        transform: translateY(-2px);
    }

    .social-icons svg {
        width: 18px;
        height: 18px;
        fill: white;
    }

    .social-icons a:hover svg {
        fill: #0d47a1;
    }

    .footer-bottom {
        text-align: center;
        margin-top: 30px;
        font-size: 13px;
        border-top: 1px solid rgba(255,255,255,0.2);
        padding-top: 15px;
        color: #e3f2fd;
    }

    /* MOBILE RESPONSIVENESS */
    @media (max-width: 768px) {
        .footer-container {
            flex-direction: column;
            text-align: center;
        }

        .social-icons {
            justify-content: center;
        }
    }
    </style>

    <div class="footer">

        <div class="footer-container">

            <div class="footer-col">
                <h3>About Us</h3>
                <p style="font-size:14px; color:#dbe9ff;">
                    We blend creativity and technology to deliver powerful digital experiences that scale globally.
                </p>
            </div>

            <div class="footer-col">
                <h3>Quick Links</h3>
                <a href="#">Home</a>
                <a href="#">Services</a>
                <a href="#">Portfolio</a>
                <a href="#">Contact</a>
            </div>

            <div class="footer-col">
                <h3>Contact</h3>
                <a href="#">Email: info@yourbrand.com</a>
                <a href="#">Phone: +254 700 000 000</a>

                <div class="social-icons">

                    <a href="#">
                        <svg viewBox="0 0 24 24">
                            <path d="M22 12a10 10 0 1 0-11.5 9.9v-7H8v-3h2.5V9.5c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12H17l-.4 3h-2.6v7A10 10 0 0 0 22 12z"/>
                        </svg>
                    </a>

                    <a href="#">
                        <svg viewBox="0 0 24 24">
                            <path d="M22 5.9c-.7.3-1.4.5-2.2.6.8-.5 1.3-1.2 1.6-2.1-.8.5-1.6.8-2.5 1A3.7 3.7 0 0 0 12 8.2c0 .3 0 .6.1.9A10.5 10.5 0 0 1 3 4.9a3.7 3.7 0 0 0 1.1 4.9c-.6 0-1.2-.2-1.7-.5v.1a3.7 3.7 0 0 0 3 3.6c-.5.1-1 .2-1.5.1.4 1.3 1.6 2.3 3.1 2.3A7.5 7.5 0 0 1 2 17.6 10.5 10.5 0 0 0 7.7 19c6.9 0 10.7-5.7 10.7-10.7v-.5c.7-.5 1.3-1.2 1.6-1.9z"/>
                        </svg>
                    </a>

                    <a href="#">
                        <svg viewBox="0 0 24 24">
                            <path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm10 2H7a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3zm-5 3.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 0 1 12 7.5zm0 2A2.5 2.5 0 1 0 14.5 12 2.5 2.5 0 0 0 12 9.5zM17.8 6.2a1 1 0 1 1-1 1 1 1 0 0 1 1-1z"/>
                        </svg>
                    </a>

                </div>
            </div>

        </div>

        <div class="footer-bottom">
            © 2026 Genesis Digital | All Rights Reserved
        </div>

    </div>
    """,
    unsafe_allow_html=True
)
