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
                if st.button("Analyze Video"):
                
                    import cv2
                    import numpy as np
                    import os
                
                    st.info("🔍 Starting video analysis pipeline...")
                
                    # =========================
                    # OPEN VIDEO
                    # =========================
                    cap = cv2.VideoCapture(video_path)
                
                    if not cap.isOpened():
                
                        st.error("❌ Could not open video.")
                
                    else:
                
                        # =========================
                        # VIDEO METADATA
                        # =========================
                        fps = cap.get(cv2.CAP_PROP_FPS)
                
                        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                
                        duration = total_frames / fps if fps > 0 else 0
                
                        st.markdown("## 📊 Video Metadata")
                
                        st.write(f"**FPS:** {fps:.2f}")
                
                        st.write(f"**Total Frames:** {total_frames}")
                
                        st.write(f"**Duration:** {duration:.2f} seconds")
                
                        # =========================
                        # FRAME EXTRACTION SETTINGS
                        # =========================
                        frame_interval_seconds = 2
                
                        frame_interval = int(fps * frame_interval_seconds)
                
                        extracted_frames = []
                
                        frame_count = 0
                
                        saved_count = 0
                

                        # =========================
                        # ANALYSIS FLAGS
                        # =========================
                        blurry_frames = 0
                        
                        dark_frames = 0
                        
                        static_frames = 0
                        
                        text_overlay_frames = 0
                        
                        previous_gray = None
                        
                        # =========================
                        # IMPORT OCR
                        # =========================

                        
                        # =========================
                        # CREATE FRAME DIRECTORY
                        # =========================
                        frame_dir = "extracted_frames"
                        
                        os.makedirs(frame_dir, exist_ok=True)
                        
                        # =========================
                        # FRAME EXTRACTION LOOP
                        # =========================
                        progress_bar = st.progress(0)
                        
                        while cap.isOpened():
                        
                            success, frame = cap.read()
                        
                            if not success:
                                break
                        
                            # =========================
                            # EXTRACT FRAME
                            # =========================
                            if frame_count % frame_interval == 0:
                        
                                frame_path = os.path.join(
                                    frame_dir,
                                    f"frame_{saved_count}.jpg"
                                )
                        
                                cv2.imwrite(frame_path, frame)
                        
                                extracted_frames.append(frame_path)
                        
                                # =========================
                                # BASIC ANALYSIS
                                # =========================
                                gray = cv2.cvtColor(
                                    frame,
                                    cv2.COLOR_BGR2GRAY
                                )
                        
                                # -------------------------
                                # BLUR DETECTION
                                # -------------------------
                                blur_score = cv2.Laplacian(
                                    gray,
                                    cv2.CV_64F
                                ).var()
                        
                                if blur_score < 120:
                                    blurry_frames += 1
                        
                                # -------------------------
                                # DARK FRAME DETECTION
                                # -------------------------
                                brightness = np.mean(gray)
                        
                                if brightness < 40:
                                    dark_frames += 1
                        
                                # -------------------------
                                # STATIC IMAGE DETECTION
                                # -------------------------
                                if previous_gray is not None:
                        
                                    difference = cv2.absdiff(
                                        previous_gray,
                                        gray
                                    )
                        
                                    motion_score = np.mean(difference)
                        
                                    # Much stricter
                                    if motion_score < 8:
                                        static_frames += 1
                        
                                previous_gray = gray
                        
                                # -------------------------
                                # TEXT OVERLAY DETECTION
                                # -------------------------

                        
                            # =========================
                            # UPDATE PROGRESS
                            # =========================
                            progress = min(
                                frame_count / total_frames,
                                1.0
                            )
                        
                            progress_bar.progress(progress)
                        
                        cap.release()
                        
                        # =========================
                        # EXTRACTION RESULTS
                        # =========================
                        st.success("✅ Frame extraction completed!")
                        
                        st.markdown("## 🖼 Extracted Frames")
                        
                        st.write(f"Frames Extracted: {len(extracted_frames)}")
                        
                        # =========================
                        # DISPLAY SAMPLE FRAMES
                        # =========================
                        preview_frames = extracted_frames[:4]
                        
                        cols = st.columns(len(preview_frames))
                        
                        for idx, frame_path in enumerate(preview_frames):
                        
                            cols[idx].image(
                                frame_path,
                                caption=f"Frame {idx + 1}",
                                use_container_width=True
                            )
                        
                        # =========================
                        # ANALYSIS RESULTS
                        # =========================
                        st.markdown("## 🤖 Video Quality Analysis")
                        
                        rejection_reasons = []
                        
                        # -------------------------
                        # BLUR CHECK
                        # -------------------------
                        if blurry_frames > 2:
                        
                            rejection_reasons.append(
                                "Video contains blurry scenes."
                            )
                        
                        # -------------------------
                        # DARK VIDEO CHECK
                        # -------------------------
                        if dark_frames > 2:
                        
                            rejection_reasons.append(
                                "Video is too dark in several scenes."
                            )
                        
                        # -------------------------
                        # STATIC IMAGE CHECK
                        # -------------------------
                        if static_frames > 2:
                        
                            rejection_reasons.append(
                                "Video contains static image scenes or slideshow-like sections."
                            )
                        
                        # -------------------------
                        # TEXT OVERLAY CHECK
                        # -------------------------
                        if text_overlay_frames > 1:
                        
                            rejection_reasons.append(
                                "Video contains text overlays or captions."
                            )
                
                        # =========================
                        # FUTURE AI MODULES
                        # =========================
                        st.markdown("## 🚀 Upcoming AI Analysis Modules")
                
                        st.markdown("""
                        Future pipeline stages can detect:
                
                        - Hotel room reveals
                        - Lobby walk-ins
                        - Pool scenes
                        - Dining experiences
                        - Spa scenes
                        - Scenic hotel views
                        - Fast-forward videos
                        - Slow motion
                        - Watermarks
                        - Text overlays
                        - Logos
                        - AI-generated visuals
                        - Poor camera movement
                        - Shaky footage
                        - Duplicate content
                        """)
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
