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
theme = st.sidebar.radio("🌓 Theme", ["Light", "Dark"])

# --- CUSTOM THEME CSS ---
def set_theme(theme):
    if theme == "Dark":
        st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: #FAFAFA;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FAFAFA;
        }
        .stButton>button {
            background-color: #F63366;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp {
            background-color: #FFFFFF;
            color: #262730;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #262730;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

set_theme(theme)

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
    demo_option = st.selectbox("Choose a demo image:", ["None", "Cat", "Mountains", "Street"], index=0)

    demo_image = None
    if demo_option != "None":
        demo_path = os.path.join("demo_images", f"{demo_option.lower()}.jpg")
        if os.path.exists(demo_path):
            demo_image = Image.open(demo_path)

    # Final image selection
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
