import streamlit as st
import streamlit.components.v1 as components

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

/* ======================================
   GLOBAL BACKGROUND
====================================== */
.stApp {
    background: linear-gradient(
        135deg,
        #d9d9d9 0%,
        #eeeeee 40%,
        #ffffff 100%
    );
}

/* HIDE STREAMLIT DEFAULTS */
#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 0.5rem;
}

/* GLOBAL TEXT */
p, label, div {
    color: black;
}

/* ======================================
   HOME SECTION TITLE
====================================== */
.home-title {

    text-align: center;

    color: #0057b8;

    font-weight: 900;
}

.home-subtitle {

    text-align: center;

    color: #0057b8;

    font-size: 28px;

    font-weight: 800;

    letter-spacing: 1px;
}

a {
    color: blue !important;
}

/* ======================================
   HEADER
====================================== */
.logo-row {
    display: flex;
    align-items: center;
    margin-bottom: -15px;
}

/* ======================================
   TOP MENU CONTAINER
====================================== */
div[data-baseweb="tab-list"] {

    background: transparent !important;

    border: none !important;

    gap: 45px;

    padding-top: 15px;

    padding-bottom: 10px;

    margin-top: 18px;

    justify-content: center !important;

    display: flex !important;

    width: 100%;
}

/* REMOVE BLUE ACTIVE TAB BACKGROUND */
button[role="tab"] {

    background: transparent !important;

    border: none !important;

    color: black !important;

    font-size: 18px !important;

    font-weight: 900 !important;

    font-family: Arial, sans-serif !important;

    padding: 10px 0px !important;

    border-radius: 0px !important;

    transition: 0.3s ease;

    justify-content: center !important;
}

/* HOVER EFFECT */
button[role="tab"]:hover {

    color: red !important;
}

/* ACTIVE TAB */
button[aria-selected="true"] {

    color: black !important;

    border-bottom: 3px solid red !important;
}

/* REMOVE BLUE LINE UNDER TABS */
div[data-baseweb="tab-border"] {
    display: none !important;
}

/* ======================================
   HOME CARDS
====================================== */
.card {

    border: 2px solid #0dcfff;

    background: rgba(255,255,255,0.88);

    backdrop-filter: blur(10px);

    padding: 30px 25px;

    border-radius: 14px;

    min-height: 260px;

    margin-bottom: 20px;

    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
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
/* ======================================
   HERO IMAGE SLIDER
====================================== */
.hero-slider {

    width: 100%;

    height: 420px;

    overflow: hidden;

    position: relative;

    border-radius: 18px;

    margin-top: 20px;

    margin-bottom: 35px;

    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.hero-track {

    display: flex;

    width: 300%;

    height: 100%;

    animation: slideHero 90s infinite;
}

.hero-slide {

    width: 100%;

    height: 420px;

    position: relative;

    flex-shrink: 0;
}

.hero-slide img {

    width: 100%;

    height: 100%;

    object-fit: cover;
}

/* DARK OVERLAY */
.hero-overlay {

    position: absolute;

    top: 0;

    left: 0;

    width: 100%;

    height: 100%;

    background: rgba(0,0,0,0.45);

    display: flex;

    flex-direction: column;

    justify-content: center;

    padding-left: 70px;

    padding-right: 70px;
}

/* SLIDE TITLE */
.hero-heading {

    color: white;

    font-size: 44px;

    font-weight: 900;

    margin-bottom: 18px;
}

/* SLIDE TEXT */
.hero-text {

    color: white;

    font-size: 20px;

    max-width: 750px;

    line-height: 1.8;
}

/* SLIDE ANIMATION */
@keyframes slideHero {

    0% {
        transform: translateX(0%);
    }

    30% {
        transform: translateX(0%);
    }

    33% {
        transform: translateX(-100%);
    }

    63% {
        transform: translateX(-100%);
    }

    66% {
        transform: translateX(-200%);
    }

    96% {
        transform: translateX(-200%);
    }

    100% {
        transform: translateX(0%);
    }
}

/* MOBILE */
@media only screen and (max-width: 768px) {

    .hero-slider {

        height: 300px;
    }

    .hero-slide {

        height: 300px;
    }

    .hero-overlay {

        padding-left: 25px;

        padding-right: 25px;
    }

    .hero-heading {

        font-size: 28px;
    }

    .hero-text {

        font-size: 15px;
    }
}
/* ======================================
   FOOTER
====================================== */
.footer {

    position: fixed;

    bottom: 0;

    left: 0;

    width: 100%;

    background-color: #0057b8;

    color: white;

    text-align: center;

    padding: 10px;

    font-size: 13px;

    z-index: 999;
}

/* ======================================
   MOBILE RESPONSIVE
====================================== */
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

        gap: 16px !important;
    }

    button[role="tab"] {

        font-size: 14px !important;

        padding: 6px 0px !important;
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
        "About Us"
    ])

# ======================================
# HOME PAGE
# ======================================
with tabs[0]:
# ======================================
# HERO IMAGE SLIDER
# ======================================
    hero_slider = """
    <!DOCTYPE html>
    <html>
    
    <head>
    
    <style>
    
    /* MAIN SLIDER */
    .hero-slider {
    
        width: 100%;
    
        height: 420px;
    
        overflow: hidden;
    
        position: relative;
    
        border-radius: 18px;
    
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }
    
    /* TRACK */
    .hero-track {
    
        display: flex;
    
        width: 300%;
    
        height: 100%;
    
        animation: slideHero 45s infinite;
    }
    
    /* EACH SLIDE */
    .hero-slide {
    
        width: 100%;
    
        height: 420px;
    
        position: relative;
    
        overflow: hidden;
    
        flex-shrink: 0;
    }
    
    /* IMAGE */
    .hero-slide img {
    
        width: 100%;
    
        height: 100%;
    
        object-fit: cover;
    
        animation: zoomImage 15s ease-in-out infinite alternate;
    }
    
    /* OVERLAY */
    .hero-overlay {
    
        position: absolute;
    
        top: 0;
    
        left: 0;
    
        width: 100%;
    
        height: 100%;
    
        background: rgba(0,0,0,0.45);
    
        display: flex;
    
        flex-direction: column;
    
        justify-content: center;
    
        padding-left: 70px;
    
        padding-right: 70px;
    }
    
    /* TITLE */
    .hero-heading {
    
        color: white;
    
        font-size: 44px;
    
        font-weight: 900;
    
        margin-bottom: 18px;
    }
    
    /* TEXT */
    .hero-text {
    
        color: white;
    
        font-size: 20px;
    
        max-width: 700px;
    
        line-height: 1.8;
    }
    
    /* SLIDE LEFT ANIMATION */
    @keyframes slideHero {
    
        0% {
            transform: translateX(0%);
        }
    
        30% {
            transform: translateX(0%);
        }
    
        33% {
            transform: translateX(-100%);
        }
    
        63% {
            transform: translateX(-100%);
        }
    
        66% {
            transform: translateX(-200%);
        }
    
        96% {
            transform: translateX(-200%);
        }
    
        100% {
            transform: translateX(0%);
        }
    }
    
    /* IMAGE ZOOM */
    @keyframes zoomImage {
    
        0% {
            transform: scale(1);
        }
    
        100% {
            transform: scale(1.12);
        }
    }
    
    /* MOBILE */
    @media only screen and (max-width: 768px) {
    
        .hero-slider {
    
            height: 280px;
        }
    
        .hero-slide {
    
            height: 280px;
        }
    
        .hero-overlay {
    
            padding-left: 25px;
    
            padding-right: 25px;
        }
    
        .hero-heading {
    
            font-size: 28px;
        }
    
        .hero-text {
    
            font-size: 15px;
        }
    }
    
    </style>
    
    </head>
    
    <body>
    
    <div class="hero-slider">
    
        <div class="hero-track">
    
            <!-- SLIDE 1 -->
            <div class="hero-slide">
    
                <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1600&auto=format&fit=crop">
    
                <div class="hero-overlay">
    
                    <div class="hero-heading">
                        Who We Are
                    </div>
    
                    <div class="hero-text">
                        Genesis Digital is a next-generation creative and AI-powered
                        company focused on digital transformation and analytics solutions.
                    </div>
    
                </div>
    
            </div>
    
            <!-- SLIDE 2 -->
            <div class="hero-slide">
    
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1600&auto=format&fit=crop">
    
                <div class="hero-overlay">
    
                    <div class="hero-heading">
                        What We Do
                    </div>
    
                    <div class="hero-text">
                        We provide AI solutions, media sourcing,
                        hospitality intelligence, and digital infrastructure.
                    </div>
    
                </div>
    
            </div>
    
            <!-- SLIDE 3 -->
            <div class="hero-slide">
    
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=1600&auto=format&fit=crop">
    
                <div class="hero-overlay">
    
                    <div class="hero-heading">
                        What Makes Us Different
                    </div>
    
                    <div class="hero-text">
                        We combine creativity, automation,
                        operational excellence, and scalable execution.
                    </div>
    
                </div>
    
            </div>
    
        </div>
    
    </div>
    
    </body>
    </html>
    """
    
    components.html(hero_slider, height=420)
    
    st.markdown(
        '<div class="home-subtitle">OUR EDGE</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div class="home-title">Why Genesis Digital Stands Out</div>',
        unsafe_allow_html=True
    )
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
    # OUR PARTNERS TITLE
    # ======================================
    st.markdown("""
    <div style="
        text-align:center;
        color:#0057b8;
        font-size:34px;
        font-weight:900;
        margin-top:40px;
        margin-bottom:25px;
    ">
        Our Partners
    </div>
    """, unsafe_allow_html=True)
    
    # ======================================
    # PARTNERS SLIDER
    # ======================================
    partners_slider = """
    <!DOCTYPE html>
    <html>
        
    <head>
        
    <style>
        
     /* MAIN CONTAINER */
    .partners-slider {
        
        width: 100%;
        
        overflow: hidden;
        
        position: relative;
        
        padding-top: 10px;
        
        padding-bottom: 20px;
    }
        
    /* MOVING TRACK */
    .partners-track {
        
        display: flex;
        
        align-items: center;
        
        gap: 60px;
        
        width: max-content;
        
        animation: scrollPartners 35s linear infinite;
    }
        
    /* LOGO CARD */
    .partner-logo {
        
        width: 180px;
        
        height: 90px;
        
        background: white;
        
        border-radius: 14px;
        
        display: flex;
        
        align-items: center;
        
        justify-content: center;
        
        padding: 15px;
        
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        
        flex-shrink: 0;
    }
        
    /* LOGO IMAGE */
    .partner-logo img {
        
        max-width: 100%;
        
        max-height: 100%;
        
        object-fit: contain;
    }
        
    /* CONTINUOUS SLIDE */
    @keyframes scrollPartners {
        
        0% {
            transform: translateX(0);
        }
        
        100% {
            transform: translateX(-50%);
        }
    }
        
    /* MOBILE */
    @media only screen and (max-width: 768px) {
        
        .partner-logo {
        
            width: 130px;
        
            height: 70px;
        }
        
        .partners-track {
        
            gap: 30px;
        }
    }
        
    </style>
        
    </head>
        
    <body>
        
    <div class="partners-slider">
        
        <div class="partners-track">
        
            <!-- PARTNER 1 -->
            <div class="partner-logo">
                <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/unravel.JPG">
            </div>
        
            <!-- PARTNER 2 -->
            <div class="partner-logo">
                <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/booking.JPG">
            </div>
        
            <!-- PARTNER 3 -->
                <div class="partner-logo">
                    <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/yafreeka.JPG">
                </div>
        
                <!-- PARTNER 4 -->
                <div class="partner-logo">
                    <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/airtel.JPG">
                </div>
        
                <!-- DUPLICATES FOR SMOOTH LOOP -->
        
                <div class="partner-logo">
                    <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/unravel.JPG">
                </div>
        
                <div class="partner-logo">
                    <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/booking.JPG">
                </div>
        
                <div class="partner-logo">
                    <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/yafreeka.JPG">
                </div>
        
                <div class="partner-logo">
                    <img src="https://raw.githubusercontent.com/ezekielmose/genesis_website/main/airtel.JPG">
                </div>
        
        </div>
        
    </div>
        
    </body>
    </html>
    """
        
    components.html(partners_slider, height=160)

    
# ======================================
# NUMBERS SECTION
# ======================================
    numbers_section = """
    <!DOCTYPE html>
    <html>
    
    <head>
    
    <style>
    
    /* SECTION */
    .numbers-section {
    
        width: 100%;
    
        padding-top: 30px;
    
        padding-bottom: 40px;
    
        margin-top: 50px;
    
        background: transparent;
    }
    
    /* TITLE */
    .numbers-title {
    
        text-align: center;
    
        color: #0057b8;
    
        font-size: 32px;
    
        font-weight: 800;
    
        margin-bottom: 35px;
    
        font-family: Arial, sans-serif;
    
        letter-spacing: 1px;
    }
    
    /* CARDS ROW */
    .numbers-row {
    
        display: flex;
    
        justify-content: center;
    
        gap: 45px;
    
        flex-wrap: wrap;
    }
    
    /* ======================================
       MODERN 3D GLASS CARD
    ====================================== */
    .number-card {
    
        width: 290px;
    
        height: 360px;
    
        border-radius: 28px;
    
        position: relative;
    
        overflow: hidden;
    
        background: rgba(255,255,255,0.18);
    
        backdrop-filter: blur(16px);
    
        -webkit-backdrop-filter: blur(16px);
    
        border: 1px solid rgba(255,255,255,0.25);
    
        display: flex;
    
        align-items: center;
    
        justify-content: center;
    
        transition: all 0.45s ease;
    
        box-shadow:
            0 10px 30px rgba(0,0,0,0.12),
            0 20px 60px rgba(0,87,184,0.12);
    
        cursor: pointer;
    }
    
    /* GLOW EFFECT */
    .number-card::before {
    
        content: "";
    
        position: absolute;
    
        top: -80px;
    
        left: -80px;
    
        width: 180px;
    
        height: 180px;
    
        background: rgba(0,87,184,0.18);
    
        border-radius: 50%;
    
        filter: blur(35px);
    
        transition: 0.5s ease;
    }
    
    /* HOVER EFFECT */
    .number-card:hover {
    
        transform: translateY(-12px) scale(1.03);
    
        box-shadow:
            0 18px 40px rgba(0,0,0,0.16),
            0 25px 70px rgba(0,87,184,0.22);
    }
    
    /* MOVE GLOW ON HOVER */
    .number-card:hover::before {
    
        top: -40px;
    
        left: -30px;
    }
    
    /* CARD CONTENT */
    .number-content {
    
        position: relative;
    
        z-index: 5;
    
        text-align: center;
    
        color: white;
    }
    
    /* BIG NUMBER */
    .number-value {
    
        font-size: 92px;
    
        font-weight: 900;
    
        line-height: 1;
    
        margin-bottom: 22px;
    
        font-family: Arial Black, sans-serif;
    }
    
    /* LABEL */
    .number-label {
    
        font-size: 22px;
    
        line-height: 1.5;
    
        font-family: Arial, sans-serif;
    }
    
    /* MOBILE */
    @media only screen and (max-width: 768px) {
    
        .numbers-title {
    
            font-size: 24px;
        }
    
        .number-card {
    
            width: 220px;
    
            height: 330px;
        }
    
        .number-value {
    
            font-size: 62px;
        }
    
        .number-label {
    
            font-size: 18px;
        }
    }
    
    </style>
    
    </head>
    
    <body>
    
    <div class="numbers-section">
    
        <div class="numbers-title">
            THE NUMBERS DON'T LIE
        </div>
    
        <div class="numbers-row">
    
            <!-- CARD 1 -->
            <div class="number-card">
    
                <div class="number-content">
    
                    <div class="number-value" id="videosShared">
                        0
                    </div>
    
                    <div class="number-label">
                        Videos<br>Shared
                    </div>
    
                </div>
    
            </div>
    
            <!-- CARD 2 -->
            <div class="number-card">
    
                <div class="number-content">
    
                    <div class="number-value" id="videosApproved">
                        0
                    </div>
    
                    <div class="number-label">
                        Videos<br>Approved
                    </div>
    
                </div>
    
            </div>
    
            <!-- CARD 3 -->
            <div class="number-card">
    
                <div class="number-content">
    
                    <div class="number-value">
                        80%
                    </div>
    
                    <div class="number-label">
                        Approval<br>Rate
                    </div>
    
                </div>
    
            </div>
    
        </div>
    
    </div>
    
    <script>
    
    /* =========================
       COUNTER FUNCTION
    ========================= */
    function animateValue(id, start, end, duration, suffix="") {
    
        let obj = document.getElementById(id);
    
        let current = start;
    
        let increment = 0.1;
    
        let stepTime = duration / ((end - start) / increment);
    
        let timer = setInterval(function() {
    
            current += increment;
    
            /* ROUND TO 1 DECIMAL */
            current = Math.round(current * 10) / 10;
    
            /* UPDATE VALUE */
            obj.innerHTML = current.toFixed(1) + suffix;
    
            /* STOP AT MAX VALUE */
            if (current >= end) {
    
                obj.innerHTML = end + suffix;
    
                clearInterval(timer);
            }
    
        }, stepTime);
    }
    
    /* RUN COUNTERS */
    animateValue("videosShared", 0, 28, 12000, "k+");
    
    animateValue("videosApproved", 0, 19.7, 14000, "k+");
    
    </script>
    
    </body>
    </html>
    """
    components.html(numbers_section, height=520)
# ======================================
# AI ANALYZER PAGE
# ======================================
with tabs[1]:

    import pandas as pd

    # CUSTOM BUTTON CSS
    st.markdown("""
    <style>

    /* BUTTON STYLE */
    div.stButton > button {
        background-color: #0057b8 !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        width: 120% !important;
        height: 50px !important;
        margin-bottom: 20px !important;
        transition: 0.3s !important;
    }

    /* BUTTON TEXT */
    div.stButton > button p {
        color: white !important;
    }

    /* HOVER EFFECT */
    div.stButton > button:hover {
        background-color: red !important;
        color: white !important;
    }

    div.stButton > button:hover p {
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
    
        if st.button("A Profile Finder"):
            st.session_state.active_tool = "profile"

        if st.button("Analyze a Video"):
            st.session_state.active_tool = "video"
        # =========================
        # UPLOAD TO AIR BUTTON
        # =========================
       # if st.button("Upload to Air"):
        
           # st.markdown(
              #  """
               # <script>
                  #  window.open(
                      #  'https://app.air.inc/d/fc799c155',
                      #  '_blank'
                   # );
               # </script>
               # """,
              #  unsafe_allow_html=True
            #)
    


    # =========================
    # RIGHT SIDE RESULTS
    # =========================
    with right_col:

        # ======================================
        # PROFILE FINDER SECTION
        # ======================================
        if st.session_state.get("active_tool") == "profile":

            st.subheader("Hotel Profiles Analyzer")

            st.write("Find the best matching Instagram profile for a hotel.")

            # -----------------------------
            # GOOGLE SHEET CONFIG
            # -----------------------------
            SHEET_ID = "1gh2QMj4vngL-JLf6SPmWvjSuCgl9uItTAMteY3acVNg"
            SHEET_GID = "204054788"

            SHEET_URL = (
                f"https://docs.google.com/spreadsheets/d/"
                f"{SHEET_ID}/export?format=csv&gid={SHEET_GID}"
            )

            @st.cache_data
            def Loading_():
                return pd.read_csv(SHEET_URL, dtype=str)

            def clean_id(value):
                return str(value).strip().lower() if value else ""

            # -----------------------------
            # AUTO FILL SECTION
            # -----------------------------
            st.subheader(" Auto Fill from Item ID")

            item_id = st.text_input(
                "Item ID",
                placeholder="e.g. 846e9ee4-e5e4-434d-b6ac-ef67c301b3e8"
            )

            if st.button(" Auto Fill"):

                if item_id:

                    try:
                        df = Loading_()

                        id_column = df.iloc[:, 1].apply(clean_id)

                        input_id = clean_id(item_id)

                        match = df[id_column == input_id]

                        if not match.empty:

                            st.session_state.hotel_name = str(
                                match.iloc[0, 2]
                            ).strip()

                            st.session_state.city = str(
                                match.iloc[0, 3]
                            ).strip()

                            st.session_state.country = str(
                                match.iloc[0, 4]
                            ).strip()

                            st.success("✅ Auto-filled successfully!")

                        else:
                            st.error("❌ Item ID not found in sheet.")

                    except Exception as e:
                        st.error(f"Error loading sheet: {e}")

                else:
                    st.warning("⚠️ Please enter an Item ID.")

            # -----------------------------
            # INPUT FIELDS
            # -----------------------------
            hotel_name = st.text_input(
                "Hotel Name",
                value=st.session_state.get("hotel_name", "")
            )

            city = st.text_input(
                "City",
                value=st.session_state.get("city", "")
            )

            country = st.text_input(
                "Country",
                value=st.session_state.get("country", "")
            )
            
                # =========================
                # INSTAGRAM PAGE BUTTON (SERPAPI VERSION)
                # =========================
                
            if st.button("Instagram Page"):
                
                if hotel_name:
                
                    import requests
                    import urllib.parse
                
                    query = f"{hotel_name} {city} {country} Instagram".strip()
                
                    #st.write("Search Query:", query)
                
                    instagram_link = None
                
                        # =========================
                        # SERPAPI SEARCH
                        # =========================
                    try:
                        SERPAPI_KEY = "c8e0fb2951ecb7f988a06e141ba0318c76749e8bf548e25468f3eba84ea242bc"
                
                        params = {
                            "engine": "google",
                            "q": query,
                            "api_key": SERPAPI_KEY
                        }
                
                        response = requests.get("https://serpapi.com/search.json", params=params)
                        data = response.json()
                
                        # extract organic results
                        for result in data.get("organic_results", []):
                            link = result.get("link", "")
                
                            if "instagram.com" in link:
                                instagram_link = link
                                break
                
                    except Exception as e:
                        st.warning(f"SerpAPI failed: {e}")
                
                        # =========================
                        # OUTPUT LOGIC
                        # =========================
                    if instagram_link:
                
                        st.success("Instagram Profile Found 🎯")
                
                        st.markdown(
                            f"""
                            <a href="{instagram_link}" target="_blank"
                                style="
                                    color:#0057b8;
                                    font-size:18px;
                                    font-weight:bold;
                                    text-decoration:none;
                                ">
                                Open Instagram Profile
                            </a>
                            """,
                            unsafe_allow_html=True
                        )
                
                    else:
                
                        google_url = (
                            "https://www.google.com/search?q="
                            + urllib.parse.quote(query)
                        )
                
                        st.warning("No Instagram profile found — opening Google results")
                
                        st.markdown(
                            f"""
                            <a href="{google_url}" target="_blank"
                                style="
                                    color:#0057b8;
                                    font-size:18px;
                                    font-weight:bold;
                                    text-decoration:none;
                                ">
                                Search on Google
                            </a>
                            """,
                            unsafe_allow_html=True
                        )
                
                else:
                    st.warning("⚠️ Please fill in hotel details first.")


        
        # ======================================
        # ANALYZE VIDEO SECTION
        # ======================================
        
        elif st.session_state.get("active_tool") == "video":
        
            import tempfile
            import os
            import base64
        
            st.subheader("🎬 Analyze a Video")
        
            st.write("Upload a video from your device for analysis.")
        
            # =========================
            # CUSTOM CSS
            # =========================
            st.markdown("""
            <style>
        
            /* =========================
               INNER DROP AREA
               (200MB per file • MP4, MOV)
            ========================= */
            [data-testid="stFileUploaderDropzone"] {
                background-color: white !important;
                border: 2px dashed black !important;
                border-radius: 12px !important;
                color: black !important;
            }
        
            /* TEXT INSIDE DROPZONE */
            [data-testid="stFileUploaderDropzone"] * {
                color: black !important;
            }
        
            /* =========================
               UPLOAD BUTTON
            ========================= */
            [data-testid="stFileUploaderDropzone"] button {
                background-color: #0057b8 !important;
                color: white !important;
                border: none !important;
                border-radius: 10px !important;
                font-weight: bold !important;
                padding: 10px 18px !important;
            }
        
            /* BUTTON HOVER */
            [data-testid="stFileUploaderDropzone"] button:hover {
                background-color: #004494 !important;
                color: white !important;
            }
        
            /* =========================
               VIDEO SIZE
            ========================= */
            [data-testid="stVideo"] {
                max-width: 320px;
            }
        
            /* VIDEO PLAYER */
            [data-testid="stVideo"] video {
                max-width: 320px !important;
                max-height: 500px !important;
                border-radius: 12px !important;
            }
        
            </style>
            """, unsafe_allow_html=True)
        
            # =========================
            # VIDEO UPLOADER
            # =========================
            uploaded_video = st.file_uploader(
                "Upload Video",
                type=["mp4", "mov"],
                help="Upload a video file for analysis"
            )
        
            # =========================
            # PROCESS VIDEO
            # =========================
            if uploaded_video is not None:
        
                st.success("✅ Video uploaded successfully!")
        
                # =========================
                # CREATE TEMP FILE
                # =========================
                temp_video = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp4"
                )
        
                temp_video.write(uploaded_video.read())
        
                video_path = temp_video.name
        
                temp_video.close()
        
                # =========================
                # PLAY VIDEO
                # =========================
                st.video(video_path)
        
                # =========================
                # VIDEO INFO
                # =========================
                file_size = uploaded_video.size / (1024 * 1024)
        
                st.markdown("### 📊 Video Info")
        
                st.write(f"**File Name:** {uploaded_video.name}")
        
                st.write(f"**Size:** {file_size:.2f} MB")
    
                
                # =========================
                # ANALYZE BUTTON
                # =========================
                if st.button ("Analyze the Video"):
                    st.write("UNDER DEVELOPMENT")
                    
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
    st.write("At Genesis Digital we specialize in sourcing and curating high-quality digital content to help businesses enhance their online presence. With a focus on video acquisition, metadata documentation, and quality assurance, we deliver engaging, scalable, and compliant solutions tailored to meet client needs. Backed by a skilled team and innovative strategies, we are committed to driving digital impact and delivering excellence with every project")

    # ======================================
    # THIN BLUE LINE
    # ======================================
    st.markdown("""
    <div style="
        width:100%;
        height:2px;
        background-color:#0057b8;
        margin-top:25px;
        margin-bottom:25px;
    "></div>
    """, unsafe_allow_html=True)

# ======================================
# OUR TEAM SLIDER CSS
# ======================================
    st.markdown("""
    <style>
    
    /* TEAM SECTION */
    .team-slider-container {
    
        width: 100%;
    
        overflow: hidden;
    
        position: relative;
    
        margin-top: 20px;
    
        margin-bottom: 40px;
    }
    
    /* SLIDING ROW */
    .team-slider {
    
        display: flex;
    
        gap: 30px;
    
        width: max-content;
    
        animation: slideTeam 10s linear infinite;
    }
    
    /* INDIVIDUAL CARD */
    .team-card {
    
        background: rgba(255,255,255,0.9);
    
        border-radius: 14px;
    
        padding: 18px;
    
        min-width: 220px;
    
        text-align: center;
    
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }
    
    /* TEAM IMAGE */
    .team-card img {
    
        width: 170px;
    
        height: 170px;
    
        object-fit: cover;
    
        border-radius: 12px;
    
        margin-bottom: 12px;
    }
    
    /* TEAM NAME */
    .team-name {
    
        font-size: 20px;
    
        font-weight: 800;
    
        color: #0057b8;
    
        margin-bottom: 5px;
    }
    
    /* TEAM TITLE */
    .team-role {
    
        font-size: 15px;
    
        color: #555;
    }
    
    /* SLIDE ANIMATION */
    @keyframes slideTeam {
    
        0% {
            transform: translateX(0%);
        }
    
        100% {
            transform: translateX(-50%);
        }
    }
    
    </style>
    """, unsafe_allow_html=True)
# ======================================
# OUR TEAM TITLE
# ======================================
    st.markdown("""
    <div style="
        color:#0057b8;
        font-size:34px;
        font-weight:900;
        margin-bottom:25px;
    ">
        Our Team
    </div>
    """, unsafe_allow_html=True)
    
# ======================================
# TEAM MEMBERS
# ======================================
# ======================================
# TEAM MEMBERS
# ======================================
    team1, team2, team3 = st.columns(3)
    
    with team1:
    
        st.image("aravind.png", width=180)
    
        st.markdown(
            """
            <div style="text-align:center;">
                <div style="
                    color:#0057b8;
                    font-size:18px;
                    font-weight:600;
                ">
                    Aravind Konnte
                    - Chief Executive Officer
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with team2:
    
        st.image("havala.png", width=180)
    
        st.markdown(
            """
            <div style="text-align:center;">
                <div style="
                    color:#0057b8;
                    font-size:18px;
                    font-weight:600;
                ">
                    Dr. Havala Allan
                    - Chief Operations Officer
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with team3:
    
        st.image("ezekiel.png", width=180)
    
        st.markdown(
            """
            <div style="text-align:center;">
                <div style="
                    color:#0057b8;
                    font-size:18px;
                    font-weight:600;
                ">
                    Ezekiel Mose
                    - Head of Analytics
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================
# CONTACT US
#=========================================
    st.title("Contact Us")
    st.write("📧 aravind@genesisdigital.in")
    st.write("📞 +919731016770")

# ======================================
# FOOTER
# ======================================
st.markdown("""
<div class="footer">
    © 2026 Genesis Digital | All Rights Reserved
</div>
""", unsafe_allow_html=True)
