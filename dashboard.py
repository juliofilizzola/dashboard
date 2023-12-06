import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    """
    Loads data from the "./supermarket_sale.csv" file and performs some preprocessing.

    :return: A pandas DataFrame with the loaded data.
    """
    df = pd.read_csv("./supermarket_sale.csv", sep=";", decimal=",")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
    return df


def create_figures(df_filtered):
    """
    :param df_filtered: A DataFrame containing the filtered data to be used for creating the figures.
    :return: Five figures created using Plotly Express and representing different aspects of revenue and ratings for different cities and product types.
    """
    fig_date_revenue = px.bar(df_filtered, x="Date", y="Total", color="City", title="Revenue per Day")
    fig_date_product_type = px.bar(df_filtered, x="Date", y="Product line", color="City",
                                   title="Revenue per Type of Product", orientation="h")
    city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
    fig_city = px.bar(city_total, x="City", y="Total", title="Revenue per Branch")
    fig_payment_type = px.pie(df_filtered, values="Total", names="Payment",
                              title="Revenue per Type of Payment")
    city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
    fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Rating")

    return fig_date_revenue, fig_date_product_type, fig_city, fig_payment_type, fig_rating


def plot_figures(fig_date, fig_date_product_type, fig_city, fig_payment_type, fig_rating):
    """
    Plots a set of figures using Streamlit and Plotly.

    :param fig_date: Figure to plot for date.
    :param fig_date_product_type: Figure to plot for date and product type.
    :param fig_city: Figure to plot for city.
    :param fig_payment_type: Figure to plot for payment type.
    :param fig_rating: Figure to plot for rating.
    :return: None

    """
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    col1.plotly_chart(fig_date, use_container_width=True)
    col2.plotly_chart(fig_date_product_type, use_container_width=True)
    col3.plotly_chart(fig_city, use_container_width=True)
    col4.plotly_chart(fig_payment_type, use_container_width=True)
    col5.plotly_chart(fig_rating, use_container_width=True)


def main():
    """
    Entry point of the program.
    Renders the Streamlit application, loads data, and creates and plots figures based on user inputs.

    :return: None
    """
    st.set_page_config(layout="wide")
    df = load_data()
    month = st.sidebar.selectbox("Month", df["Month"].unique())
    df_filtered = df[df["Month"] == month]
    fig_date, fig_date_product_type, fig_city, fig_payment_type, fig_rating = create_figures(df_filtered)
    plot_figures(fig_date, fig_date_product_type, fig_city, fig_payment_type, fig_rating)


if __name__ == "__main__":
    main()
