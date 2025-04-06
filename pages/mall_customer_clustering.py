import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np

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

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Fit KMeans clustering model
X = df[['Annual Income (k$)', 'Spending Score (1-100)']].values
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)


# Function to plot clusters and centroids
def plot_clusters_with_centroids():
    df['Cluster'] = kmeans.labels_
    centroids = pd.DataFrame(kmeans.cluster_centers_, columns=['Annual Income (k$)', 'Spending Score (1-100)'])
    centroids['Cluster'] = ['Centroid'] * len(centroids)
    combined_df = pd.concat([df, centroids])
    fig = px.scatter(combined_df, x='Annual Income (k$)', y='Spending Score (1-100)', color='Cluster',
                     title="Income Wise Spending Clusters with Centroids")
    st.plotly_chart(fig)


# Function to assign cluster to new data
def assign_cluster(new_data):
    cluster = kmeans.predict(new_data)
    return cluster[0]


# Function to print cluster meaning


# Main function to run Streamlit app
def main():
        st.title("Mall Customer Data Cluster")

    # Navigation sidebar

        st.write("### Cluster Assignment")
        annual_income = st.number_input("Enter Annual Income (k$):", min_value=0)
        spending_score = st.number_input("Enter Spending Score (1-100):", min_value=0, max_value=100)

        new_data = np.array([[annual_income, spending_score]])
        cluster = assign_cluster(new_data)

        st.write(f"You belong to Cluster {cluster}")
        plot_clusters_with_centroids()

if __name__ == "__main__":
    main()
