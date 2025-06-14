import streamlit as st
from PIL import Image
from caption_model import generate_caption
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="🧠 AI Image Caption Generator",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- THEME TOGGLE ---
theme = st.sidebar.radio("🌓 Toggle Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: #FAFAFA;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #FAFAFA !important;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body {
            background-color: #FFFFFF;
            color: #262730;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #262730 !important;
        }
        </style>
        """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🧠 AI Image Caption Generator")
st.markdown("### Upload an image or choose a demo, and let AI describe what's in it!")

st.markdown("---")

# --- MAIN LAYOUT ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📤 Upload your image")
    uploaded_file = st.file_uploader("Upload JPG, PNG", type=["jpg", "jpeg", "png"])

    st.subheader("📸 Or select a demo image")
    demo_option = st.selectbox(
        "Choose a demo image:",
        ["None", "Cat", "Beach", "Street"],
        index=0
    )

    # Load demo image
    demo_image = None
    if demo_option != "None":
        demo_path = os.path.join("demo_images", f"{demo_option.lower()}.jpg")
        if os.path.exists(demo_path):
            demo_image = Image.open(demo_path)

    # Prioritize uploaded file
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Your Uploaded Image", use_container_width=True)
    elif demo_image:
        image = demo_image
        st.image(image, caption=f"🖼️ Demo Image: {demo_option}", use_container_width=True)
    else:
        image = None

with col2:
    if image:
        with st.spinner("🧠 Thinking... generating caption..."):
            caption = generate_caption(image)
        st.success("✅ Caption generated successfully!")
        st.markdown(f"### 📝 Caption:\n**{caption}**")

# --- SIDEBAR INFO ---
with st.sidebar:
    st.markdown("## ℹ️ About This App")
    st.info("""
    This web app uses a deep learning model to generate captions for images using AI.

    **Technologies used:**  
    - Streamlit  
    - PyTorch  
    - Transformers  
    - Pillow
    """)
    st.markdown("---")
    st.markdown("👨‍💻 Built by [Piyush Tomar](https://github.com/Piyush-2909singh)")
