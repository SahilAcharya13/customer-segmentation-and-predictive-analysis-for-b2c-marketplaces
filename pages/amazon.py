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
    if dataset_name == "Amazon":
        return pd.read_csv("amazon_products.csv")
    # Add more datasets as needed
    else:
        return None

def count_category_occurrences(categories,df):
    # Split the input to get individual categories
    categories_list = [cat.strip() for cat in categories.split(",")]
    # Initialize a dictionary to store category counts
    category_counts = {}

    # Count occurrences of each category
    for category in categories_list:
        count = (df['category_name'] == category).sum()
        category_counts[category] = count

    return category_counts

def plot_category_counts(category_counts):
    # Convert dictionary to DataFrame
    df = pd.DataFrame.from_dict(category_counts, orient='index', columns=['Count'])
    # Plot bar graph using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df.index, y=df['Count'], palette='viridis')
    plt.xlabel('Category', color='white')
    plt.ylabel('Count', color='white')
    plt.title('Category Occurrences', color='white')
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(color='white')
    plt.gca().patch.set_alpha(0)
    plt.tight_layout()
    st.pyplot(plt.gcf(), transparent=True)

def display_product_details(title,df):
    # Find the product with the given title
    product = df.loc[df['title'] == title]

    if not product.empty:
        # Display product details
        st.write("**Title:**", title)
        st.image(product['imgUrl'].values[0], caption=title, width=100)
        st.write("**Stars:**", product['stars'].values[0])
        st.write("**Price:**", product['price'].values[0])
        st.write("**Is Best Seller:**", product['isBestSeller'].values[0])
        st.write("**Category:**", product['category_name'].values[0])
        st.write("**Product URL:**", product['productURL'].values[0])
    else:
        st.write("Product not found.")


def display_top_products(category_name, sort_by, df):
    category_data = df[df['category_name'] == category_name]

    if not category_data.empty:
        # Sort the data based on the selected sorting criteria
        sorted_data = category_data.sort_values(by=sort_by, ascending=False).head(5)

        # Display the top five product names
        st.write("**Top 5 Products in", category_name, "sorted by", sort_by, ":**")
        c=1
        for index, row in sorted_data.iterrows():
            st.write(c,") ",row['title'])
            c+=1

        # Create a bar graph based on the selected sorting criteria
        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=sort_by, y='title', data=sorted_data, palette='viridis')
        plt.xlabel(sort_by.capitalize(), color='white')
        plt.ylabel('Product Name', color='white')
        plt.title('Top 5 Products Based on ' + sort_by.capitalize(), color='white')
        plt.xticks(color='white')
        plt.yticks(color='white')
        st.pyplot(plt.gcf(), transparent=True)

def display_best_sellers(category,df):
    # Filter the dataset based on the selected category
    category_data = df[df['category_name'] == category]

    if not category_data.empty:
        # Filter the best sellers
        best_sellers = category_data[category_data['isBestSeller'] == True]

        if not best_sellers.empty:
            # Print the details of the best seller
            st.write("**Best Seller in", category, ":**")
            best_seller = best_sellers.iloc[0]
            st.write("**Title:**", best_seller['title'])
            st.write("**Stars:**", best_seller['stars'])
            st.write("**Price:**", best_seller['price'])
            st.write("**Is Best Seller:**", best_seller['isBestSeller'])
            st.write("**Category Name:**", best_seller['category_name'])

        else:
            st.write("No best seller found in", category)
    else:
        st.write("No data available for", category)



def main():
    st.title("Amazon Dataset Analysis")

    # Dropdown menu to select dataset
    dataset_name = "Amazon"

    # Load the selected dataset
    if (dataset_name == "Amazon"):
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
        st.title("Category Occurrence Analysis")

        # Input field for user to enter categories separated by commas
        categories_input = st.text_input("Enter Categories (separated by commas):")

        if categories_input:
            # Count occurrences of each category
            category_counts = count_category_occurrences(categories_input,df)

            if category_counts:
                st.subheader("Category Occurrences:")
                st.write(pd.Series(category_counts))

                # Plot bar graph using Seaborn
                st.subheader("Bar Graph:")
                plot_category_counts(category_counts)

            else:
                st.write("No matching categories found in the dataset.")
        st.title("Product Details")

        # Input field for user to enter the title of the product
        title_input = st.text_input("Enter the title of the product:")

        if title_input:
            # Display product details upon submission
            display_product_details(title_input,df)

        st.title("Top Products by Category")

        # Input field for user to enter the category name
        category_name = st.text_input("Enter the category name:")

        if category_name:
            # Selection box for user to choose sorting criteria
            sort_by = st.selectbox("Sort by:", ["price", "stars", "boughtInLastMonth"])

            if sort_by:
                # Display top products and bar graph
                display_top_products(category_name, sort_by,df)
        st.title("Best Sellers by Category")

        # Input field for user to enter the category name
        category = st.text_input("Enter the category name:", key="category_input")


        if category:
            # Display best sellers and pie chart
            display_best_sellers(category,df)



if __name__ == "__main__":
    main()