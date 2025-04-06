import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }

        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        footer {visibility: hidden;}
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
""", unsafe_allow_html=True)

# Load the saved model
model = load_model('covid_classification_model.h5')

# Define image dimensions
img_width, img_height = 150, 150

# Define class labels
labels = ['Covid', 'Normal', 'Viral Pneumonia']

# Function to preprocess uploaded image
def preprocess_image(image):
    img = image.resize((img_width, img_height))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array / 255.0

# Function to make predictions
def predict(image):
    img_array = preprocess_image(image)
    predictions = model.predict(img_array)
    predicted_label_index = np.argmax(predictions)
    return labels[predicted_label_index]

# Streamlit app
def main():
    st.title('Chest X-Ray Image Classification')
    st.write('Upload a chest X-ray image and get the prediction')

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Make prediction when button is clicked
        if st.button('Predict'):
            prediction = predict(image)
            st.write('Prediction:', prediction)

if __name__ == '__main__':
    main()
