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

    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Tabs styling */
    div[data-baseweb="tab-list"] {
        justify-content: center;
        gap: 40px;
        margin-top: 10px;
    }

    button[data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
    }

    /* Coming Soon Text */
    .coming-soon {
        text-align: center;
        font-size: 80px;
        font-weight: bold;
        color: #4CAF50;
        margin-top: 120px;
    }

    .sub-text {
        text-align: center;
        font-size: 24px;
        color: gray;
        margin-top: 20px;
    }

    </style>
""", unsafe_allow_html=True)

# ======================================
# TOP HEADER WITH LOGO
# ======================================
col1, col2 = st.columns([1, 6])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.markdown(
        "<h1 style='padding-top:20px;'>Genesis Digital</h1>",
        unsafe_allow_html=True
    )

# ======================================
# HORIZONTAL MENU
# ======================================
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
