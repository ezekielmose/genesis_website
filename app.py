import streamlit as st

# ======================================
# PAGE CONFIGURATION
# ======================================
st.set_page_config(
    page_title="Genesis Website",
    page_icon="🌐",
    layout="wide"
)

# ======================================
# SESSION STATE
# ======================================
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "ai_submenu" not in st.session_state:
    st.session_state.ai_submenu = "Profile Finder"

# ======================================
# CUSTOM CSS
# ======================================
st.markdown("""
<style>

/* =====================================
   GLOBAL SETTINGS
===================================== */

.stApp {
    background-color: #eaeaea !important;
}

/* Hide Streamlit default items */
#MainMenu,
footer,
header {
    visibility: hidden;
}

/* Reduce spacing */
.block-container {
    padding-top: 0.5rem;
}

/* FORCE ALL TEXT BLACK */
p, h1, h2, h3, h4, h5, h6, span, label, div {
    color: black !important;
}

/* Links remain blue */
a {
    color: blue !important;
}

/* =====================================
   NAVIGATION BAR
===================================== */

.navbar {
    background-color: #0057b8;
    padding: 10px 20px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

/* Logo */
.logo img {
    vertical-align: middle;
}

/* Main menu */
.menu {
    display: flex;
    gap: 25px;
    align-items: center;
}

/* Menu items */
.menu-item {
    position: relative;
    color: white !important;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    padding: 10px 15px;
    border-radius: 5px;
    text-decoration: none;
}

/* Hover effect */
.menu-item:hover {
    background-color: red;
    transition: 0.3s;
}

/* Dropdown submenu */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #0057b8;
    min-width: 220px;
    top: 45px;
    left: 0;
    border-radius: 8px;
    overflow: hidden;
    z-index: 999;
}

/* Submenu items */
.dropdown-content div {
    color: white !important;
    padding: 12px 16px;
    cursor: pointer;
    font-weight: bold;
}

/* Hover submenu */
.dropdown-content div:hover {
    background-color: red;
}

/* Show dropdown on hover */
.dropdown:hover .dropdown-content {
    display: block;
}

/* =====================================
   COMING SOON
===================================== */

.coming-soon {
    text-align: center;
    font-size: 90px;
    font-weight: bold;
    color: #0057b8 !important;
    margin-top: 140px;
}

.sub-text {
    text-align: center;
    font-size: 28px;
    color: black !important;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# TOP SECTION
# ======================================
col1, col2 = st.columns([1, 8])

with col1:
    st.image("logo.png", width=110)

with col2:

    selected_menu = st.radio(
        "",
        ["Home", "Our Services", "AI Analyzer", "About", "Contact"],
        horizontal=True,
        label_visibility="collapsed"
    )

# ======================================
# HOME PAGE
# ======================================
if selected_menu == "Home":

    st.markdown(
        "<div class='coming-soon'>COMING SOON</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-text'>Our new AI-powered platform is under development.</div>",
        unsafe_allow_html=True
    )

# ======================================
# OUR SERVICES PAGE
# ======================================
elif selected_menu == "Our Services":

    st.title("Our Services")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Web Development")
        st.write("Modern websites and applications.")

    with col2:
        st.subheader("AI Solutions")
        st.write("AI-powered business tools.")

    with col3:
        st.subheader("Data Analysis")
        st.write("Professional data insights.")

# ======================================
# AI ANALYZER PAGE
# ======================================
elif selected_menu == "AI Analyzer":

    st.title("AI Analyzer")

    ai_submenu = st.radio(
        "",
        ["Profile Finder", "Reels Analyzer"],
        horizontal=True,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # PROFILE FINDER
    if ai_submenu == "Profile Finder":

        st.subheader("Profile Finder")

        st.write("Upload profile-related files for AI analysis.")

        uploaded_file = st.file_uploader(
            "Upload Profile File",
            type=["csv", "txt", "pdf"],
            key="profile"
        )

        if uploaded_file:
            st.success("Profile file uploaded successfully!")

    # REELS ANALYZER
    elif ai_submenu == "Reels Analyzer":

        st.subheader("Reels Analyzer")

        st.write("Upload reels data for AI-powered insights.")

        uploaded_file = st.file_uploader(
            "Upload Reels File",
            type=["csv", "mp4", "txt"],
            key="reels"
        )

        if uploaded_file:
            st.success("Reels file uploaded successfully!")

# ======================================
# ABOUT PAGE
# ======================================
elif selected_menu == "About":

    st.title("About Us")

    st.write("""
    We are a technology company focused on:

    - Artificial Intelligence
    - Automation
    - Modern Web Solutions
    """)

# ======================================
# CONTACT PAGE
# ======================================
elif selected_menu == "Contact":

    st.title("Contact Us")

    st.write("📧 Email: mose@genesisdigital.in")
    st.write("📞 Phone: +254748468634")
