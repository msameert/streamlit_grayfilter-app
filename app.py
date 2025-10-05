import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

st.title("Image Gray Filter")
st.write("This program applies gray filter on your image - Upload the image and press the button to see the Magic!!")

img = st.file_uploader("Upload an Image", type=["jpg","png"])
if img is not None:
 pil_img = Image.open(img)
 image_arr = np.array(pil_img)
 if image_arr.ndim == 3:
        gray = np.mean(image_arr[:, :, :3], axis=2)
 else:
        gray = image_arr 
 gray_image = Image.fromarray(gray.astype(np.uint8))

 if st.button("Convert"):
     st.image(gray_image, caption="Grayscale Image")

 buf = io.BytesIO()
 gray_image.save(buf, format="PNG")
 buf.seek(0)

 st.download_button(
      label="Download Image",
      data=buf,
      file_name="gray_image.png",
      mime="image/png"
     )