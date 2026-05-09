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
# CUSTOM CSS
# ======================================
st.markdown("""
<style>

/* Entire App Background */
.stApp {
    background-color: #eaeaea;
}

/* Hide Streamlit default items */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Reduce top spacing */
.block-container {
    padding-top: 1rem;
}

/* =====================================
   TOP NAVIGATION BAR
===================================== */
div[data-baseweb="tab-list"] {
    background-color: #0057b8;
    padding: 15px 20px;
    border-radius: 10px;
    align-items: center;
    gap: 40px;
    margin-top: 0px;
}

/* Menu Buttons */
button[data-baseweb="tab"] {
    color: white !important;
    font-size: 18px;
    font-weight: bold;
    background-color: transparent;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
}

/* Hover Effect */
button[data-baseweb="tab"]:hover {
    background-color: red !important;
    color: white !important;
    transition: 0.3s;
}

/* Active Tab */
button[aria-selected="true"] {
    background-color: #003f85 !important;
    color: white !important;
}

/* =====================================
   COMING SOON SECTION
===================================== */
.coming-soon {
    text-align: center;
    font-size: 90px;
    font-weight: bold;
    color: #0057b8;
    margin-top: 140px;
}

.sub-text {
    text-align: center;
    font-size: 28px;
    color: #555555;
    margin-top: 20px;
}

/* Logo spacing */
.logo-container {
    margin-bottom: -20px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER SECTION
# ======================================
col1, col2 = st.columns([1, 8])

with col1:
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    st.image("logo.png", width=120)
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================
# HORIZONTAL MENU
# ======================================
with col2:
    tabs = st.tabs([
        "Home",
        "Our Services",
        "AI Analyzer",
        "About",
        "Contact"
    ])

# ======================================
# HOME PAGE
# ======================================
with tabs[0]:

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
with tabs[1]:

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
with tabs[2]:

    st.title("AI Analyzer")

    uploaded_file = st.file_uploader(
        "Upload a file",
        type=["csv", "txt", "pdf"]
    )

    if uploaded_file:
        st.success("File uploaded successfully!")

# ======================================
# ABOUT PAGE
# ======================================
with tabs[3]:

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
with tabs[4]:

    st.title("Contact Us")

    st.write("📧 Email: mose@genesisdigital.in")
    st.write("📞 Phone: +254748468634")
