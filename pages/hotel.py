import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
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
def load_dataset(dataset_name):
    if dataset_name == "Hotel":
        return pd.read_csv("hotel.csv")
    # Add more datasets as needed
    else:
        return None

def display_top_hotels(df):
    # Assuming 'name' is the column for hotel names and 'reviews' for the review count
    top_hotels = df['name'].value_counts().head(10)
    st.write(top_hotels)
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid", context="talk")
    sns.barplot(x=top_hotels.index, y=top_hotels.values, palette='coolwarm')
    plt.xlabel('Hotel Name', color='white')
    plt.ylabel('Count', color='white')
    plt.title('Top 10 Hotels by Occurrence', color='white')
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(color='white')
    plt.gcf().set_facecolor('none')
    plt.gcf().set_edgecolor('none')
    plt.gca().set_facecolor('none')
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    st.pyplot(plt.gcf(), transparent=True)


def plot_top_hotels(country, data):
    # Filter the dataset for the selected country and where rating is 5 stars
    filtered_data = data[(data['province'] == country) & (data['reviews.rating'] == 5)]

    # Count the occurrence of each hotel name and get the top 10
    top_hotels = filtered_data['name'].value_counts().head(10)

    # Plotting
    plt.figure(figsize=(12, 8))  # Change figure size for vertical layout
    sns.barplot(x=top_hotels.index, y=top_hotels.values, palette='viridis')
    plt.xlabel('Hotel Name', color='white')  # Adjust font color
    plt.ylabel('Number of 5-Star Ratings', color='white')  # Adjust font color
    plt.xticks(rotation=45, ha='right', color='white')  # Rotate x-axis labels for better visibility
    plt.yticks(color='white')  # Adjust font color for y-axis labels
    plt.title(f'Top 10 Hotels in {country} by 5-Star Rating Occurrence', color='white')  # Adjust font color
    plt.gca().patch.set_alpha(0)  # Make background transparent
    st.pyplot(plt.gcf(), transparent=True)

def plot_star_wise_counts(data):
    # Count the occurrence of each star rating
    star_counts = data['reviews.rating'].value_counts().sort_index()
    st.write(star_counts)
    # Plotting
    plt.figure(figsize=(8, 6))
    sns.barplot(x=star_counts.index, y=star_counts.values, palette='viridis')
    plt.xlabel('Star Rating', color='white')
    plt.ylabel('Count', color='white')
    plt.title('Star-wise Counts', color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.gca().patch.set_alpha(0)
    st.pyplot(plt.gcf(), transparent=True)
def get_star_counts(hotel_name,df):
    # Filter the dataset for the given hotel name
    hotel_reviews = df[df['name'] == hotel_name]
    # Count the occurrences of each star rating
    star_counts = hotel_reviews['reviews.rating'].value_counts().sort_index()
    return star_counts

def get_hotel_counts(hotel_names,df):
    # Split the input string into a list of hotel names
    hotel_names_list = [name.strip() for name in hotel_names.split(',')]

    # Count the occurrences of each hotel name
    hotel_counts = {}
    for name in hotel_names_list:
        count = df['name'].str.contains(name, case=False).sum()
        hotel_counts[name] = count
    if hotel_counts:
        st.subheader("Hotel-wise Counts:")
        for name, count in hotel_counts.items():
            st.write(f"{name}: {count}")

        # Plot bar graph using Plotly
        fig = go.Figure(data=[go.Bar(x=list(hotel_counts.keys()), y=list(hotel_counts.values()))])
        fig.update_layout(
            title="Hotel-wise Counts",
            xaxis_title="Hotel Name",
            yaxis_title="Count"
        )
        st.plotly_chart(fig)
    else:
        st.write("No matching hotels found in the dataset.")



def main():
    st.title("Hotel Dataset Analysis")

    # Dropdown menu to select dataset
    dataset_name = "Hotel"

    # Load the selected dataset
    if (dataset_name == "Hotel"):
        df = load_dataset(dataset_name)
        st.write("Preview of Hotel dataset:")
        st.write(df.head(10))
        # Load the dataset
        if 'name' in df.columns:
            u_data = len(df["name"].unique())
        else:
            u_data = len(df["title"].unique())

        total_blank_columns = (df.isnull().sum() == len(df)).sum()
        # Top small boxes
        st.markdown(
            """
            <div style="display: flex;">
                <div style="background-color: #f0ad4e; color: white; padding: 20px; margin: 10px; border-radius: 5px;">
                    <h2>Total Rows</h2>
                    <p style="font-size: 20px;">{}</p>
                </div>
                <div style="background-color: #5bc0de; color: white; padding: 10px; margin: 10px; border-radius: 5px;">
                    <h2>Total Columns</h2>
                    <p style="font-size: 20px;">{}</p>
                </div>
                 <div style="background-color: #d9534f; color: white; padding: 10px; margin: 10px; border-radius: 5px;">
                    <h2>Blank Columns</h2>
                    <p style="font-size: 20px;">{}</p>
                </div>
                <div style="background-color: #5cb85c; color: white; padding: 10px; margin: 10px; border-radius: 5px;">
                    <h2>Unique Values</h2>
                    <p style="font-size: 20px;">{}</p>
                </div>
            </div>
            """.format(
                df.shape[0],
                df.shape[1],
                (df.isnull().sum() == len(df)).sum(),
                u_data
            ),
            unsafe_allow_html=True
        )

    if dataset_name == "Hotel":
        st.subheader("Highest number of occurrence in data set ")
        display_top_hotels(df)
        st.subheader("Top 10 Hotel in the province")

        # Get unique countries
        countries = df['province'].unique()
        selected_country = st.selectbox("Select province", ["Select"] + list(countries))

        if selected_country != "Select":
            st.write(f"Selected province: {selected_country}")
            # Function to display top 10 hotels with 5-star ratings

            plot_top_hotels(selected_country, df)
            st.write("Star-wise Counts:")
            # Function to display star-wise counts
            plot_star_wise_counts(df)
            # Input field for user to enter hotel name
            hotel_name = st.text_input("Enter Hotel Name:")

            if hotel_name:
                # Get star-wise counts for the entered hotel name
                star_counts = get_star_counts(hotel_name, df)

                if not star_counts.empty:
                    st.subheader(f"Star-wise Counts for {hotel_name}:")
                    st.write(star_counts)

                    # Plot bar graph using Plotly
                    fig = go.Figure(data=[go.Bar(x=star_counts.index, y=star_counts.values)])
                    fig.update_layout(
                        title=f"Star-wise Counts for {hotel_name}",
                        xaxis_title="Star Rating",
                        yaxis_title="Count"
                    )
                    st.plotly_chart(fig)
                else:
                    st.write("Hotel not found in the dataset.")
        hotel_names = st.text_input("Enter Hotel Names (separated by commas):")

        if hotel_names:
            # Get hotel-wise counts for the entered hotel names
            get_hotel_counts(hotel_names, df)


if __name__ == "__main__":
    main()