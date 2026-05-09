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
    
    /* Remove Streamlit default menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Top Navigation Styling */
    div[data-baseweb="tab-list"] {
        justify-content: center;
        gap: 40px;
    }

    button[data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
    }

    </style>
""", unsafe_allow_html=True)

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

    st.title("Welcome to Genesis Website")

    st.write("""
    We provide modern digital solutions powered by Artificial Intelligence.
    """)

    st.image(
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
        use_container_width=True
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