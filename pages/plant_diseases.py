from keras.src.legacy.preprocessing.image import ImageDataGenerator
import numpy as np
import streamlit as st
import tensorflow as tf
from keras.preprocessing import image
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
model = tf.keras.models.load_model('plant_disease_model1.h5')

# Define constants
img_height = 224
img_width = 224
batch_size = 32

def load_and_preprocess_image(image_file):
    img = image.load_img(image_file, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.
    return img_array

def predict_disease(image_file):
    img_array = load_and_preprocess_image(image_file)
    predictions = model.predict(img_array)
    return predictions

st.title('Plant Disease Prediction')

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    predictions = predict_disease(uploaded_file)
    # Get the predicted class label

    # Download the dataset from this URL https://www.kaggle.com/datasets/emmarex/plantdisease
    # change this URL 
    train_data_dir = 'D:/Degree/Sem 8/plant_diseases/PlantVillage'

    train_datagen = ImageDataGenerator(
        rescale=1./255
    )

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )
    class_labels = list(train_generator.class_indices.keys())
    predicted_class_idx = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_idx]

    st.write("Predicted class:", predicted_class_label)

