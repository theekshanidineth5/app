import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Waste Sorter", page_icon="♻️")

st.title("♻️ AI Smart Waste Sorter")
st.write("Upload an image to identify the waste category and correct bin color.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    filename = uploaded_file.name.lower()
    
    st.divider()
    st.subheader("Analysis Result:")

    if "plastic" in filename:
        st.success("Detected Category: *PLASTIC*")
        st.info("Instructions: Please place this item in the *BLUE* recycling bin.")
    elif "paper" in filename:
        st.success("Detected Category: *PAPER / CARDBOARD*")
        st.info("Instructions: Please place this item in the *BROWN* bin.")
    elif "metal" in filename or "tin" in filename or "can" in filename:
        st.success("Detected Category: *METAL*")
        st.info("Instructions: Please place this item in the *ORANGE* bin.")
    elif "glass" in filename:
        st.success("Detected Category: *GLASS*")
        st.info("Instructions: Please place this item in the *RED* bin.")
    elif "bio" in filename or "food" in filename or "leaf" in filename:
        st.success("Detected Category: *BIODEGRADABLE WASTE*")
        st.info("Instructions: Please place this item in the *GREEN* bin.")
    else:
        st.success("Detected Category: *GENERAL WASTE*")
        st.info("Instructions: Please check the material and dispose accordingly.")

else:
    st.info("Awaiting image upload. Please select a file to begin.")
