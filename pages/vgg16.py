import streamlit as st
from keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np
import plotly.graph_objects as go

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


# Load VGG16 model
model = VGG16(weights='imagenet')

st.title('Image Classification with VGG16')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Load and preprocess image
    img = image.load_img(uploaded_file, color_mode='rgb', target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Make predictions
    features = model.predict(x)
    predictions = decode_predictions(features)

    # Extract labels and probabilities
    labels = [pred[1] for pred in predictions[0]]
    probs = [pred[2] for pred in predictions[0]]

    # Create bar graph
    fig = go.Figure([go.Bar(x=labels, y=probs)])
    fig.update_layout(title='Top 5 Predictions',
                      xaxis_title='Class',
                      yaxis_title='Probability',
                      yaxis=dict(range=[0, 1]))

    # Display bar graph
    st.plotly_chart(fig)
