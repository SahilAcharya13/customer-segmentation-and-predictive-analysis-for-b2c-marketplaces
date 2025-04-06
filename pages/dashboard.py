
import streamlit as st
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

# Function to open Streamlit pages based on box selection
def open_page(page_name):
    if page_name == 'Data Analysis':
        st.write("Data Analysis Page")
    elif page_name == 'Data Base':
        st.write("Data Base Page")
    elif page_name == 'Hotel':
        st.write("Hotel Page")
    elif page_name == 'Amazon':
        st.write("Amazon Page")


box_content = {
    'Data Analysis': {
        'image': 'https://cdn-icons-png.flaticon.com/512/1643/1643996.png',
        'text': 'Data Analysis',
        'link': 'data_analysis'
    },
    'Hotel': {
        'image': 'https://cdn-icons-png.flaticon.com/512/6008/6008287.png',
        'text': 'Hotel',
        'link': 'hotel'
    },
    'Data Base': {
        'image': 'https://cdn-icons-png.flaticon.com/512/9243/9243391.png',
        'text': 'Data Base',
        'link': 'data_base'
    },
    'Amazon': {
        'image': 'https://i.pinimg.com/736x/cc/b1/05/ccb105426093729a420ce61b52728b9c.jpg',
        'text': 'Amazon Data analysis and visualization',
        'link': 'amazon'
    },
    'Machine Learning': {
        'image': 'https://cdn-icons-png.freepik.com/512/8345/8345929.png',
        'text': 'Machine Learning algorithms',
        'link': 'machine_learning'
    },
    'Opencv': {
        'image': 'https://cdn-icons-png.flaticon.com/512/5904/5904483.png',
        'text': 'Opencv',
        'link': 'opencv'
    },
    'Image Processing': {
        'image': 'https://cdn-icons-png.flaticon.com/512/9423/9423110.png',
        'text': 'Image Processing',
        'link': 'image_processing'
    },
    'Sales Prediction': {
        'image': 'https://cdn-icons-png.flaticon.com/512/3252/3252686.png',
        'text': 'Store Sales Data Prediction',
        'link': 'sales_prediction'
    },
    'Sales Data Analysis': {
        'image': 'https://cdn-icons-png.flaticon.com/512/4149/4149657.png',
        'text': 'Store Sales Data Analysis',
        'link': 'Sales_data'
    },
    'GDP prediction': {
        'image': 'https://cdn-icons-png.flaticon.com/512/9307/9307217.png',
        'text': 'Gross domestic product prediction',
        'link': 'gdp_prediction'
    },
    'Google Stock Price Analysis': {
        'image': 'https://cdn-icons-png.flaticon.com/512/2620/2620564.png',
        'text': 'Google Stock Price Analysis',
        'link': 'google_stock_price_analysis'
    },
    'Google Stock Price Prediction': {
        'image': 'https://cdn-icons-png.flaticon.com/512/6410/6410570.png',
        'text': 'Google Stock Price Prediction',
        'link': 'google_stock_price_prediction'
    },
    'Covid': {
        'image': 'https://cdn-icons-png.freepik.com/256/2667/2667512.png',
        'text': 'Covid19 or viral pneumonia Prediction',
        'link': 'covid19'
    },
    'Customer Wise Data Analysis': {
        'image': 'https://cdn-icons-png.freepik.com/512/4143/4143099.png',
        'text': 'Customer Wise Data Analysis',
        'link': 'customer_wise_data_analysis'
    },
    'Region Wise Data Analysis': {
        'image': 'https://cdn-icons-png.freepik.com/512/9098/9098519.png',
        'text': 'Region Wise Data Analysis',
        'link': 'region_wise_data_analysis'
    },
    'Product Wise Data Analysis': {
        'image': 'https://cdn-icons-png.flaticon.com/512/4129/4129528.png',
        'text': 'Product Wise Data Analysis',
        'link': 'product_wise_data_analysis'
    },
    'Mall Customers Analysis': {
        'image': 'https://cdn-icons-png.flaticon.com/512/3225/3225069.png',
        'text': 'Mall Customers Analysis',
        'link': 'mall_customer_analysis'
    },
    'Mall Customers data visualization': {
        'image': 'https://cdn-icons-png.flaticon.com/512/10729/10729340.png',
        'text': 'Mall Customers data visualization',
        'link': 'mall_customer_visualization'
    },
    'Mall Customers Clustering': {
        'image': 'https://cdn-icons-png.freepik.com/512/4862/4862440.png',
        'text': 'Mall Customers Clustering',
        'link': 'mall_customer_clustering'
    },
    'Walmart Sales Prediction': {
        'image': 'https://cdn-icons-png.flaticon.com/256/5977/5977595.png',
        'text': 'Walmart Sales Prediction',
        'link': 'walmart_sales_prediction'
    },
    'Walmart Sales Analysis': {
        'image': 'https://www.freeiconspng.com/thumbs/walmart-logo-png/walmart-logo-png-5.png',
        'text': 'Walmart Sales Visualization',
        'link': 'walmart_visualization'
    },
    'Zomato Data Cleaning': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/75/Zomato_logo.png',
        'text': 'Zomato Data Cleaning',
        'link': 'zomato_data_cleaning'
    },
    'Plant Diseases Prediction': {
        'image': 'https://cdn-icons-png.flaticon.com/512/7963/7963920.png',
        'text': 'Plant Diseases Predictiong',
        'link': 'plant_diseases'
    }
}


# Display the boxes
st.title("Analysis and Visualization:")
col1, col2, col3 = st.columns(3)

with col1:
    for box_name in ['Amazon','Google Stock Price Analysis','Region Wise Data Analysis','Hotel']:
        box_content_info = box_content[box_name]
        box_html = f"""
        <a href="{box_content_info['link']}" style="text-decoration: none; color: white;">
            <div style="padding: 20px;margin: 10px; border: 3px solid #262730; border-radius: 10px; text-align: center; ">
                <img src="{box_content_info['image']}" style="width: 100px; height: 100px; object-fit: cover; background-color: transparent;">
                <div colour:white>{box_content_info['text']} </div>
            </div>
        </a>
        """
        st.write(box_html, unsafe_allow_html=True)

with col2:
    for box_name in ['Sales Data Analysis','Product Wise Data Analysis','Customer Wise Data Analysis','Data Analysis']:
        box_content_info = box_content[box_name]
        box_html = f"""
        <a href="{box_content_info['link']}" style="text-decoration: none; color: white;">
            <div style="padding: 20px;margin: 10px; border: 3px solid #262730; border-radius: 10px; text-align: center; ">
                <img src="{box_content_info['image']}" style="width: 100px; height: 100px; object-fit: cover; background-color: transparent;">
                <div>{box_content_info['text']}</div>
            </div>
        </a>
        """
        st.write(box_html, unsafe_allow_html=True)
with col3:
    for box_name in ['Mall Customers Analysis','Mall Customers data visualization','Walmart Sales Analysis','Zomato Data Cleaning']:
        box_content_info = box_content[box_name]
        box_html = f"""
        <a href="{box_content_info['link']}" style="text-decoration: none; color: white;">
            <div style="padding: 20px;margin: 10px; border: 3px solid #262730; border-radius: 10px; text-align: center; ">
                <img src="{box_content_info['image']}" style="width: 100px; height: 100px; object-fit: cover; background-color: transparent;">
                <div>{box_content_info['text']}</div>
            </div>
        </a>
        """
        st.write(box_html, unsafe_allow_html=True)

st.title("Machine learning Algorithm:")
col1, col2, col3 = st.columns(3)

with col1:
    for box_name in ['Sales Prediction','GDP prediction','Walmart Sales Prediction']:
        box_content_info = box_content[box_name]
        box_html = f"""
        <a href="{box_content_info['link']}" style="text-decoration: none; color: white;">
            <div style="padding: 20px;margin: 10px; border: 3px solid #262730; border-radius: 10px; text-align: center; ">
                <img src="{box_content_info['image']}" style="width: 100px; height: 100px; object-fit: cover; background-color: transparent;">
                <div colour:white>{box_content_info['text']} </div>
            </div>
        </a>
        """
        st.write(box_html, unsafe_allow_html=True)

with col2:
    for box_name in ['Google Stock Price Prediction','Plant Diseases Prediction']:
        box_content_info = box_content[box_name]
        box_html = f"""
        <a href="{box_content_info['link']}" style="text-decoration: none; color: white;">
            <div style="padding: 20px;margin: 10px; border: 3px solid #262730; border-radius: 10px; text-align: center; ">
                <img src="{box_content_info['image']}" style="width: 100px; height: 100px; object-fit: cover; background-color: transparent;">
                <div>{box_content_info['text']}</div>
            </div>
        </a>
        """
        st.write(box_html, unsafe_allow_html=True)
with col3:
    for box_name in ['Mall Customers Clustering','Machine Learning']:
        box_content_info = box_content[box_name]
        box_html = f"""
        <a href="{box_content_info['link']}" style="text-decoration: none; color: white;">
            <div style="padding: 20px;margin: 10px; border: 3px solid #262730; border-radius: 10px; text-align: center; ">
                <img src="{box_content_info['image']}" style="width: 100px; height: 100px; object-fit: cover; background-color: transparent;">
                <div>{box_content_info['text']}</div>
            </div>
        </a>
        """
        st.write(box_html, unsafe_allow_html=True)

