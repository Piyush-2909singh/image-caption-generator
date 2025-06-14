import streamlit as st
from PIL import Image
from caption_model import generate_caption  # Make sure this function is implemented

# Set page config
st.set_page_config(
    page_title="🧠 AI Image Caption Generator",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Optional Logo (place a logo.png in your repo or use URL)
# st.image("https://path-to-your-logo.png", width=150)

# Title and subtitle
st.title("🧠 AI Image Caption Generator")
st.markdown("### Upload an image and let AI describe what's in it!")

st.markdown("---")

# Layout with columns
col1, col2 = st.columns([1, 2])

with col1:
    uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)


with col2:
    if uploaded_file:
        with st.spinner("🧠 Thinking... generating caption..."):
            caption = generate_caption(image)
        st.success("✅ Caption generated successfully!")
        st.markdown(f"### 📝 Caption:\n**{caption}**")

# Sidebar with project info
with st.sidebar:
    st.markdown("## ℹ️ About This App")
    st.info("""
    This web app uses a deep learning model to generate captions for any image.

    **Technologies:** Streamlit, PyTorch, Transformers, Pillow.
    """)
    st.markdown("---")
    st.markdown("Built with ❤️ by [Piyush Tomar](https://github.com/Piyush-2909singh)")

