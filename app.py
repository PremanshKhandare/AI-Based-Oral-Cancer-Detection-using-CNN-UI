import streamlit as st
from PIL import Image

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Early Oral Cancer Detection",
    layout="centered"
)

# ------------------ FIX FOR DEPLOY BAR OVERLAP ------------------
st.markdown("""
<style>
.block-container {
    padding-top: 4.8rem !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ THEME STATE ------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# ------------------ THEME TOGGLE ------------------
col1, col2, col3 = st.columns([6, 2, 2])
with col3:
    dark_mode = st.toggle("🌙 Dark Mode", value=(st.session_state.theme == "dark"))
st.session_state.theme = "dark" if dark_mode else "light"

# ------------------ GLOBAL CSS ------------------
st.markdown("""
<style>

/* -------- BASE -------- */
.block-container {
    max-width: 1200px;
    padding-bottom: 3rem;
}

/* -------- TABS -------- */
.stTabs {
    max-width: 900px;
    margin: auto;
}

.stTabs [data-baseweb="tab"] > div {
    font-size: 1.25rem !important;
    font-weight: 600;
    padding: 0.8rem 1.8rem;
}

.stTabs [aria-selected="true"] > div {
    font-size: 1.35rem !important;
    font-weight: 700;
}

/* -------- CARDS -------- */
.card {
    padding: 2.4rem 2.6rem;
    border-radius: 30px;
    backdrop-filter: blur(16px);
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
    margin-bottom: 3.5rem;
}

.card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 6px;
    background: linear-gradient(180deg, #2563eb, #60a5fa);
}

.card:hover {
    transform: translateY(-8px);
}

/* -------- TEXT -------- */
.card h3 {
    font-size: 1.7rem;
    margin-bottom: 0.8rem;
}

.card h4 {
    font-size: 1.35rem;
    margin-bottom: 0.6rem;
}

.card p, .card li {
    font-size: 1.05rem;
    line-height: 1.8;
}

/* -------- WARNING -------- */
.warning-box {
    max-width: 900px;
    margin: 4rem auto;
    padding: 1.6rem 1.8rem;
    border-radius: 18px;
    border-left: 6px solid #facc15;
}

/* -------- UPLOAD SECTION -------- */
.upload-row {
    display: flex;
    gap: 4rem;
    max-width: 1000px;
    margin: 0 auto 4rem auto;
}

.upload-card {
    flex: 1;
}

/* -------- SECTION ALIGNMENT -------- */
.section-start {
    margin-top: 1.2rem;
}

</style>
""", unsafe_allow_html=True)

# ------------------ THEME CSS ------------------
if st.session_state.theme == "light":
    st.markdown("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, #dbeafe, transparent 40%),
            radial-gradient(circle at bottom right, #e0f2fe, transparent 40%),
            linear-gradient(135deg, #eef2ff, #f8fafc);
    }

    .card {
        background: rgba(255,255,255,0.92);
        box-shadow: 0 28px 60px rgba(0,0,0,0.12);
    }

    .warning-box {
        background: rgba(254,252,232,0.95);
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, #020617, transparent 40%),
            radial-gradient(circle at bottom right, #020617, transparent 40%),
            linear-gradient(135deg, #020617, #0f172a);
        color: #e5e7eb;
    }

    h1, h2, h3, h4, p, li {
        color: #f8fafc !important;
    }

    .card {
        background: rgba(2,6,23,0.9);
        border: 1px solid #1e293b;
        box-shadow: 0 28px 60px rgba(0,0,0,0.45);
    }

    .warning-box {
        background: rgba(113,63,18,0.25);
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------ HERO HEADER ------------------
st.markdown("""
<div style="
    max-width:900px;
    margin: 0 auto 4rem auto;
    padding:2.8rem;
    border-radius:32px;
    background: linear-gradient(135deg, #2563eb, #3b82f6, #60a5fa);
    color:white;
    text-align:center;
    box-shadow:0 30px 70px rgba(37,99,235,0.45);
">
    <h1>🦷 Early Oral Cancer Detection</h1>
    <p style="font-size:1.15rem; opacity:0.95;">
        AI-assisted diagnostic support using Convolutional Neural Networks
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------ TABS ------------------
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📤 Upload Image", "ℹ About"])

# ------------------ HOME ------------------
# ------------------ HOME ------------------
with tab1:
    st.markdown('<div class="section-start">', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>👋 Welcome</h3>
        <p>
        Welcome to the <strong>Early Oral Cancer Detection System</strong>,
        an AI-driven platform designed to assist in the early identification
        of potentially cancerous oral lesions.
        </p>
        <p>
        By combining deep learning with medical imaging, this system aims
        to support early-stage detection and promote awareness of oral health.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🚀 Why Early Detection Matters</h4>
        <p>
        Oral cancer often progresses silently in its initial stages.
        Early detection significantly increases survival rates and
        improves treatment outcomes.
        </p>
        <ul>
            <li>Higher survival rate with early diagnosis</li>
            <li>Less invasive treatment options</li>
            <li>Improved quality of life for patients</li>
            <li>Reduced healthcare costs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🧠 AI-Powered Analysis</h4>
        <p>
        The system leverages <strong>Convolutional Neural Networks (CNNs)</strong>
        to automatically learn and analyze visual patterns from oral cavity images.
        </p>
        <p>
        This allows the model to differentiate between normal and abnormal tissue
        with high accuracy, providing a reliable decision-support tool.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>📌 Key Features</h4>
        <ul>
            <li>User-friendly image upload interface</li>
            <li>Real-time prediction and confidence score</li>
            <li>Visual explanations using Grad-CAM</li>
            <li>Modern, responsive UI design</li>
            <li>Academic and research-oriented implementation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>⚙ How the System Works</h4>
        <ol>
            <li>User uploads an oral cavity image</li>
            <li>Image preprocessing and normalization</li>
            <li>CNN-based feature extraction</li>
            <li>Prediction with confidence score</li>
            <li>Visualization using Grad-CAM</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
        ⚠ <strong>Disclaimer:</strong> This system is intended strictly
        for academic and research purposes and must not be used as a
        substitute for professional medical diagnosis.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ UPLOAD ------------------
# ------------------ UPLOAD ------------------
with tab2:
    st.markdown('<div class="upload-row">', unsafe_allow_html=True)

    st.markdown("""
    <div class="card upload-card">
        <h3>📤 Upload Oral Image</h3>
        <p>
        Upload a clear, well-focused image of the oral cavity
        (JPG, PNG, or JPEG format).
        </p>
        <p>
        For best results, ensure proper lighting and avoid excessive
        shadows or obstructions inside the mouth.
        </p>
    """, unsafe_allow_html=True)

    st.file_uploader(
        "Upload Image",
        type=["jpg", "png", "jpeg"],
        label_visibility="collapsed"
    )

    st.markdown("""
        <p style="font-size:0.95rem; opacity:0.85; margin-top:0.6rem;">
        Supported formats: JPG, PNG, JPEG<br>
        Recommended resolution: ≥ 224 × 224 pixels
        </p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card upload-card">
        <h3>📊 Analysis & Results</h3>
        <p>
        Once an image is uploaded, it will be processed by the
        trained CNN model to analyze visual patterns within the image.
        </p>
        <p>
        The analysis panel will display the model’s prediction along
        with a confidence score to assist interpretation.
        </p>
        <ul>
            <li>Predicted class (Normal / Suspicious)</li>
            <li>Confidence percentage</li>
            <li>Grad-CAM heatmap highlighting important regions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ ABOUT ------------------
with tab3:
    st.markdown('<div class="section-start">', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>ℹ About This Project</h3>
        <p>
        Oral cancer is one of the most common forms of cancer in developing countries,
        and early detection plays a crucial role in improving survival rates.
        Unfortunately, many cases are detected at later stages due to lack of
        awareness and limited access to diagnostic resources.
        </p>
        <p>
        This project aims to provide an <strong>AI-assisted early detection support system</strong>
        that can help identify suspicious oral lesions at an early stage.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🧠 Why Convolutional Neural Networks (CNN)?</h4>
        <p>
        Convolutional Neural Networks (CNNs) are highly effective for image-based
        tasks because they can automatically learn spatial features such as
        edges, textures, and complex patterns directly from images.
        </p>
        <p>
        In medical imaging, CNNs have shown superior performance compared to
        traditional machine learning techniques due to their ability to:
        </p>
        <ul>
            <li>Capture fine-grained visual patterns in medical images</li>
            <li>Learn hierarchical feature representations</li>
            <li>Reduce manual feature engineering</li>
            <li>Generalize well across unseen data</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🔬 Dataset & Model Approach</h4>
        <p>
        The system is trained using publicly available oral cavity image datasets.
        Images are preprocessed and passed through a deep CNN model for feature
        extraction and classification.
        </p>
        <p>
        The trained model predicts whether an uploaded image shows
        <strong>normal tissue</strong> or <strong>potentially cancerous regions</strong>,
        along with a confidence score to assist interpretation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🎯 Project Objectives</h4>
        <ul>
            <li>Support early detection of oral cancer using AI</li>
            <li>Demonstrate practical application of CNNs in healthcare</li>
            <li>Provide an intuitive and accessible user interface</li>
            <li>Promote awareness of oral cancer and its early signs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>⚠ Limitations & Ethical Considerations</h4>
        <p>
        This system is designed strictly for <strong>academic and research purposes</strong>.
        It should not be used as a replacement for professional medical diagnosis.
        </p>
        <p>
        Model predictions depend on dataset quality, image clarity, and training
        distribution, and may not generalize perfectly to all real-world scenarios.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>👨‍💻 Team Members</h4>
        <ul>
            <li>Premansh Khandare</li>
            <li>Anjanikumar Choubey</li>
            <li>Navneet Giri</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ------------------ FOOTER ------------------
st.divider()
st.warning("⚠ For academic and research purposes only.")
