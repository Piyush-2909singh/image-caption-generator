import streamlit as st
from PIL import Image
import tempfile
from caption_model import generate_caption

st.set_page_config(page_title="🧠 AI Image Caption Generator", layout="centered")
st.title("🧠 AI Image Caption Generator")
st.write("Upload an image and get a smart AI-generated caption.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            image.save(temp_file.name)
            caption = generate_caption(temp_file.name)
            st.success(f"📝 Caption: {caption}")
