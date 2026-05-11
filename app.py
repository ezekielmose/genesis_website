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
            def load_sheet():
                return pd.read_csv(SHEET_URL, dtype=str)

            def clean_id(value):
                return str(value).strip().lower() if value else ""

            # -----------------------------
            # AUTO FILL SECTION
            # -----------------------------
            st.subheader("⚡ Auto Fill from Item ID")

            item_id = st.text_input(
                "Item ID",
                placeholder="e.g. 846e9ee4-e5e4-434d-b6ac-ef67c301b3e8"
            )

            if st.button("⚡ Auto Fill"):

                if item_id:

                    try:
                        df = load_sheet()

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
        #=====================
        # INSTAGRAM BUTTON
        #===================
            
            if st.button("Instagram Page"):
            
                if hotel_name:
            
                    import requests
                    from bs4 import BeautifulSoup
                    import urllib.parse
            
                    # =========================
                    # BUILD SEARCH QUERY
                    # =========================
                    query = f"{hotel_name} {city} {country}".strip()
            
                    search_url = (
                        "https://www.google.com/search?q="
                        f"site:instagram.com+{urllib.parse.quote(query)}"
                    )
            
                    headers = {
                        "User-Agent": "Mozilla/5.0"
                    }
            
                    response = requests.get(search_url, headers=headers)
                    soup = BeautifulSoup(response.text, "html.parser")
            
                    # =========================
                    # EXTRACT LINKS (IMPROVED)
                    # =========================
                    links = []
            
                    for a in soup.find_all("a", href=True):
                        href = a["href"]
            
                        # Google redirect links
                        if "/url?q=" in href:
                            clean_link = href.split("/url?q=")[1].split("&")[0]
                            clean_link = urllib.parse.unquote(clean_link)
            
                            if "instagram.com" in clean_link:
            
                                # FILTER OUT NON-PROFILES
                                if (
                                    "/p/" not in clean_link and
                                    "/reel/" not in clean_link and
                                    "/explore" not in clean_link and
                                    "/tv/" not in clean_link
                                ):
                                    links.append(clean_link)
            
                        # direct instagram links fallback
                        elif "instagram.com/" in href:
            
                            if (
                                "/p/" not in href and
                                "/reel/" not in href and
                                "/explore" not in href and
                                "/tv/" not in href
                            ):
                                links.append(href)
            
                    # remove duplicates
                    links = list(set(links))
            

                    # =========================
                    # RANKING LOGIC (BETTER)
                    # =========================
                    hotel_words = hotel_name.lower().split()
                    
                    ranked_links = []
                    
                    for link in links:
                    
                        score = 0
                    
                        link_clean = (
                            link.lower()
                            .replace("-", " ")
                            .replace("_", " ")
                        )
                    
                        # exact hotel name boost
                        if hotel_name.lower() in link_clean:
                            score += 20
                    
                        # word-by-word matching
                        for word in hotel_words:
                    
                            if len(word) > 2 and word in link_clean:
                                score += 5
                    
                        # city bonus
                        if city and city.lower() in link_clean:
                            score += 3
                    
                        # country bonus
                        if country and country.lower() in link_clean:
                            score += 2
                    
                        # profile bonus
                        if (
                            "/p/" not in link_clean and
                            "/reel/" not in link_clean and
                            "/tv/" not in link_clean
                        ):
                            score += 5
                    
                        ranked_links.append((score, link))
                    
                    # sort by highest score
                    ranked_links = sorted(
                        ranked_links,
                        key=lambda x: x[0],
                        reverse=True
                    )
                    
                    # =========================
                    # DISPLAY RESULTS
                    # =========================
                    if ranked_links:
                    
                        best_score, best_match = ranked_links[0]
                    
                        st.success("🎯 Instagram Profiles Found")
                    
                        # BEST MATCH BUTTON
                        st.markdown(
                            f"""
                            <a href="{best_match}" target="_blank">
                                <button style="
                                    background-color:#0057b8;
                                    color:white;
                                    font-size:16px;
                                    font-weight:bold;
                                    border:none;
                                    padding:12px 20px;
                                    border-radius:10px;
                                    cursor:pointer;
                                    width:100%;
                                    margin-bottom:15px;
                                ">
                                    Open Best Matching Instagram Profile
                                </button>
                            </a>
                            """,
                            unsafe_allow_html=True
                        )
                    
                        st.write("🔗 Best Match:", best_match)
                    
                        # SHOW TOP MATCHES
                        st.subheader("Other Possible Matches")
                    
                        shown = set()
                    
                        for score, link in ranked_links[:5]:
                    
                            if link not in shown:
                    
                                shown.add(link)
                    
                                st.markdown(
                                    f"""
                                    <a href="{link}" target="_blank">
                                        {link}
                                    </a>
                                    """,
                                    unsafe_allow_html=True
                                )
                    
                    else:
                        st.warning("⚠️ No Instagram profiles found.")

        # ======================================
        # ANALYZE VIDEO SECTION
        # ======================================
        elif st.session_state.get("active_tool") == "video":

            st.subheader("Analyze a Video")

            st.write("Video Analyzer Coming Soon...")
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
