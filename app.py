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

/* FORCE ALL TEXT BLACK (IMPORTANT FIX) */
* {
    color: black !important;
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

    st.markdown(
        "<div class='coming-soon'>UNDER DEVELOPMENT</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-text'>Our new AI-powered platform is under development.</div>",
        unsafe_allow_html=True
    )

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
