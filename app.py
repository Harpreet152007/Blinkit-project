import streamlit as st
import pandas as pd
import plotly.express as px


# Page Configuration
st.set_page_config(
    page_title="Blinkit Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("blinkit_orders.csv")
# Sidebar
st.sidebar.title("Blinkit Dashboard")

page = st.sidebar.radio(
    "Go To",
    ["Home", "Dataset Cleaning", "EDA", "Research Questions", "Conclusion"]
)

# ================= HOME =================

if page == "Home":

    st.title("🛒 Blinkit Sales Analysis Dashboard")

    # ---------------- Project Description ----------------

    st.header("📌 Project Description")

    st.write("""
The Blinkit Sales Analysis Dashboard is developed to analyze Blinkit grocery order data
using Python, Pandas, Plotly, and Streamlit. The project focuses on understanding customer
purchasing behavior, sales performance, payment preferences, delivery performance,
and business trends through interactive visualizations and data analysis.
""")

    # ---------------- Project Overview ----------------

    st.header("📖 Project Overview")

    st.write("""
This project analyzes the Blinkit Orders dataset to extract meaningful business insights.
The dashboard includes:

• Dataset Cleaning

• Exploratory Data Analysis (EDA)

• Research Questions

• Business Insights

• Final Conclusion

The dashboard helps users understand sales patterns, customer behavior,
payment methods, delivery performance, and order trends.
""")

    # ---------------- Objectives ----------------

    st.header("🎯 Project Objectives")

    st.write("""
• Analyze Blinkit order data.

• Understand customer purchasing behavior.

• Identify sales trends.

• Study payment method preferences.

• Analyze weekday, monthly and hourly order trends.

• Evaluate delivery performance.

• Generate business insights for decision-making.
""")

    # ---------------- Key Features ----------------

    st.header("⭐ Key Features")

    st.write("""
✔ User-friendly Dashboard

✔ Dataset Cleaning

✔ Exploratory Data Analysis (EDA)

✔ Interactive Plotly Charts

✔ Research Question Analysis

✔ Conclusion & References
""")

    # ---------------- Dataset Summary ----------------

    st.header("📊 Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Rows", df.shape[0])
        st.metric("Total Columns", df.shape[1])

    with col2:
        st.metric("Missing Values", df.isnull().sum().sum())
        st.metric("Duplicate Rows", df.duplicated().sum())

    # ---------------- Dataset Description ----------------

    st.header("📄 Dataset Description")

    st.write("""
The dataset contains Blinkit grocery order information including customer details,
store information, order amount, payment methods, delivery status,
ratings, order date, and other order-related attributes.

This data is used to perform sales analysis and identify business trends.
""")

    # ---------------- Dataset Features ----------------

    st.header("📝 Dataset Features")

    feature_df = pd.DataFrame({
        "Feature Name": df.columns
    })

    st.dataframe(feature_df, width="stretch")

    # ---------------- Data Types ----------------

    st.header("📂 Data Types")

    datatype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(datatype_df,width="stretch")

    # ---------------- Statistical Summary ----------------

    st.header("📈 Statistical Summary")

    st.dataframe(df.describe(include="all"), width="stretch")

    # ---------------- Key Highlights ----------------

    st.header("✨ Key Highlights")

    st.write("""
✅ Successfully analyzed Blinkit Orders Dataset.

✅ Dataset cleaned by handling duplicates and creating new date-time features.

✅ Customer ordering trends analyzed by Hour, Weekday and Month.

✅ Payment Method analysis performed.

✅ Delivery Status analysis completed.

✅ Total Revenue and Order Trends evaluated.

✅ Interactive visualizations created using Plotly.

✅ Business insights generated for better decision-making.
""")

    st.success("Welcome to the Blinkit Sales Analysis Dashboard!")
# ================= DATASET CLEANING =================
elif page == "Dataset Cleaning":

    st.title("📂 Dataset Cleaning")

    # Load Dataset
    df = pd.read_csv("blinkit_orders.csv")

    # ================= Original Dataset =================

    st.header("1. Original Dataset")
    st.dataframe(df.head(10), width="stretch")

    # ================= Original Shape =================

    st.header("2. Original Shape")

    st.write("Number of Rows :", df.shape[0])
    st.write("Number of Columns :", df.shape[1])

    # ================= Missing Values =================

    st.header("3. Missing Values")

    st.dataframe(
        pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values
        }),
        width="stretch"
    )

    # ================= Duplicate Values =================

    st.header("4. Duplicate Values")

    st.write("Duplicate Rows :", df.duplicated().sum())
    st.write("There is no missing value and duplicated value in dataset")

    # ================= Data Types =================

    st.header("5. Data Types")

    datatype = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(datatype, width="stretch")

    # ================= Data Cleaning =================

    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(df["order_date"])

    # ================= Create New Columns =================

    df["year"] = df["order_date"].dt.year
    df["month_name"] = df["order_date"].dt.month_name()
    df["day"] = df["order_date"].dt.day
    df["date_only"] = df["order_date"].dt.date
    df["hour"] = df["order_date"].dt.hour
    df["minute"] = df["order_date"].dt.minute
    df["weekday"] = df["order_date"].dt.day_name()

    st.header("6. New Columns Created")

    new_columns = pd.DataFrame({
        "New Columns": [
            "year",
            "month_name",
            "day",
            "date_only",
            "hour",
            "minute",
            "weekday"
        ]
    })

    st.dataframe(new_columns, width="stretch")

    # ================= Dataset After Cleaning =================

    st.header("7. Dataset After Cleaning")

    st.dataframe(df.head(10), width="stretch")

    # ================= Shape After Cleaning =================

    st.header("8. Shape After Cleaning")

    st.write("Number of Rows :", df.shape[0])
    st.write("Number of Columns :", df.shape[1])

    st.success("✅ Dataset Cleaning Completed Successfully.")

# ================= EDA =================

elif page == "EDA":

    st.title("📊 EDA")

    st.title("📊 Exploratory Data Analysis (EDA)")
    # Load Dataset
    df = pd.read_csv("blinkit_orders.csv")

# Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

# Create New Columns
    df["year"] = df["order_date"].dt.year
    df["month_name"] = df["order_date"].dt.month_name()
    df["day"] = df["order_date"].dt.day
    df["date_only"] = df["order_date"].dt.date
    df["hour"] = df["order_date"].dt.hour
    df["minute"] = df["order_date"].dt.minute
    df["weekday"] = df["order_date"].dt.day_name()


    # ================= Graph 1 =================

    st.subheader("1. Orders by Hour")
    hour_df = df["hour"].value_counts().sort_index().reset_index()
    hour_df.columns = ["Hour", "Orders"]

    fig = px.line(
        hour_df,
        x="Hour",
        y="Orders",
        markers=True,
        title="Orders by Hour",
        color_discrete_sequence=["#FFD400" ]
    )

    
    st.plotly_chart(fig,use_container_width=True)

    

    st.subheader("📖 Explanation")

    st.write("""
This line graph shows the total number of orders placed during each hour of the day.
It helps identify the busiest and least busy ordering hours.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• The highest number of orders is received around **8 AM** and **1 PM**, indicating peak ordering hours.

• Order volume decreases after peak hours and remains moderate throughout the day.

• Businesses can increase delivery staff and inventory during peak hours to improve customer service.

• Low-demand hours can be used for maintenance, inventory updates, and promotional activities.
""")

    # ================= Graph 2 =================

    st.subheader("2. Monthly Orders")

    month_df = df["month_name"].value_counts().reset_index()
    month_df.columns = ["Month", "Orders"]

    fig = px.bar(
        month_df,
        x="Month",
        y="Orders",
        color="Orders",
        title="Orders by Month",
        
    )
    fig.update_traces(
    marker_color="#FFD400",          
    marker_line_color="#000000",    
    marker_line_width=2
)
    
    st.plotly_chart(fig,use_container_width=True)
    st.subheader("📖 Explanation")

    st.write("""
This bar chart compares the total number of orders placed in each month.
It helps identify monthly sales trends and seasonal demand.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• **May** and **August** recorded the highest number of orders.

• **February** had the lowest number of orders.

• Monthly demand varies, indicating seasonal purchasing patterns.

• Promotional campaigns can be introduced during low-performing months.
""")

    # ================= Graph 3 =================

    st.subheader("3. Payment Method Distribution")

    payment_df = df["payment_method"].value_counts().reset_index()
    payment_df.columns = ["Payment Method", "Orders"]

    fig = px.pie(
        payment_df,
        names="Payment Method",
        values="Orders",
        title="Payment Method Distribution",
        color_discrete_sequence=[
        "#FFD400",   
        "#000000",   
        "#FFEB3B",   
        "#424242"   
    ]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📖 Explanation")

    st.write("""
This pie chart shows the percentage distribution of different payment methods used by customers.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• Payment methods are almost equally preferred by customers.

• Card payments have a slightly higher usage compared to other methods.

• UPI, Wallet, and Cash are also widely used.

• Multiple payment options improve customer convenience.
""")

    # ================= Graph 4 =================

    st.subheader("4. Delivery Status")

    delivery_df = df["delivery_status"].value_counts().reset_index()
    delivery_df.columns = ["Delivery Status", "Orders"]

    fig = px.bar(
        delivery_df,
        x="Delivery Status",
        y="Orders",
        color="Delivery Status",
        title="Delivery Status Distribution",
        color_discrete_sequence=[
        "#FFD400",   
        "#000000",   
        "#FFEB3B"]

    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📖 Explanation")

    st.write("""
This bar chart displays the total number of orders based on delivery status.
It evaluates delivery performance.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• Most orders are delivered **On Time**, indicating efficient delivery operations.

• Slightly Delayed orders are significantly lower.

• Significantly Delayed deliveries are the least frequent.

• Maintaining high on-time delivery improves customer satisfaction.
""")

    # ================= Graph 5 =================

    st.subheader("5. Order Total by Payment Method")

    payment_total = df.groupby("payment_method")["order_total"].sum().reset_index()

    fig = px.bar(
        payment_total,
        x="payment_method",
        y="order_total",
        color="payment_method",
        title="Order Total by Payment Method",
        
    )
    fig.update_traces(
    marker_color="#FFD400",          
    marker_line_color="#000000",    
    marker_line_width=2
)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📖 Explanation")

    st.write("""
This graph compares the total revenue generated through each payment method.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• Card payments generated the highest total revenue.

• Cash and Wallet payments also contributed significantly.

• UPI generated slightly lower revenue compared to other payment methods.

• All payment methods contribute almost equally to overall sales.
""")

    # ================= Graph 6 =================

    st.subheader("6. Orders by Weekday")

    weekday_df = df["weekday"].value_counts().reset_index()
    weekday_df.columns = ["Weekday", "Orders"]

    fig = px.bar(
        weekday_df,
        x="Weekday",
        y="Orders",
        color="Orders",
        title="Orders by Weekday",
          
    )

    fig.update_traces(
    marker_color="#FFD400",          
    marker_line_color="#000000",    
    marker_line_width=2
)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📖 Explanation")

    st.write("""
This chart shows the total number of orders placed on each day of the week.
It helps identify the busiest weekdays.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• Wednesday received the highest number of orders.

• Monday recorded the lowest number of orders.

• Overall order distribution is balanced throughout the week.

• Businesses can schedule staff according to weekday demand.
""")

    # ================= Graph 7 =================

    st.subheader("7. Payment Method by Weekday")

    weekday_payment = df.groupby(
        ["weekday", "payment_method"]
    ).size().reset_index(name="Orders")

    fig = px.bar(
        weekday_payment,
        x="weekday",
        y="Orders",
        color="payment_method",
        barmode="group",
        title="Payment Method by Weekday",
        color_discrete_map={
        "Card": "#FFD400",      
        "Cash": "#000000",      
        "UPI": "#FFC107",       
        "Wallet": "#424242"     
    }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📖 Explanation")

    st.write("""
This grouped bar chart compares payment methods across different weekdays.
It shows customer payment preferences on each day of the week.
""")

    st.subheader("📌 Key Insights")

    st.write("""
• Card, Cash, UPI, and Wallet are consistently used throughout the week.

• Wednesday recorded the highest Cash transactions.

• Wallet payments were relatively higher on Monday and Sunday.

• Customer payment preferences remain fairly balanced across weekdays.
""")
elif page == "Research Questions":

    st.title("❓ Research Questions")



    # Required Columns
    df["order_date"] = pd.to_datetime(df["order_date"])

    df["hours"] = df["order_date"].dt.hour
    df["month name"] = df["order_date"].dt.month_name()
    df["weekday"] = df["order_date"].dt.day_name()

    # =====================================================
    # Research Question 1
    # =====================================================

    st.header("Research Question 1")
    st.subheader("What is the total revenue generated from all Blinkit orders?")

    total_revenue = df["order_total"].sum()

    fig = px.bar(
        x=["Total Revenue"],
        y=[total_revenue],
        text=[total_revenue],
        title="Total Revenue Generated"
    )
    fig.update_traces(
    marker_color="#FFD400",
    marker_line_color="#000000",
    marker_line_width=2
)

    st.plotly_chart(fig, use_container_width=True)

    st.write("### Analysis")
    st.write("""
The graph shows the total revenue generated from all Blinkit orders.
It represents the overall business performance based on order value.
""")

    st.write("### Key Insights")
    st.write("""
• Displays total business revenue.

• Useful for measuring overall sales performance.

• Higher revenue indicates strong customer demand.
""")

    # =====================================================
    # Research Question 2
    # =====================================================

    st.header("Research Question 2")
    st.subheader("Which payment method is used most frequently by customers?")

    payment_orders = df["payment_method"].value_counts().reset_index()
    payment_orders.columns = ["Payment Method", "Orders"]

    fig = px.bar(
        payment_orders,
        x="Payment Method",
        y="Orders",
        color="Orders",
        text="Orders",
        title="Most Frequently Used Payment Method",
    
    )
    fig.update_traces(
    marker_color="#FFD400",      
    marker_line_color="#000000", 
    marker_line_width=2
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("### Analysis")
    st.write("""
This graph compares the total number of orders placed using each payment method.
""")

    st.write("### Key Insights")
    st.write("""
• Highest bar represents the most preferred payment method.

• Lowest bar represents the least preferred payment method.

• Helps understand customer payment preferences.
""")

    # =====================================================
    # Research Question 3
    # =====================================================

    st.header("Research Question 3")
    st.subheader("On which weekday are the maximum orders placed?")

    weekday = (
        df["weekday"]
        .value_counts()
        .reindex([
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ])
        .reset_index()
    )

    weekday.columns = ["Weekday", "Orders"]

    fig = px.bar(
        weekday,
        x="Weekday",
        y="Orders",
        color="Orders",
        text="Orders",
        title="Orders by Weekday",
        
    )
    fig.update_traces(
    marker_color="#FFD400",      
    marker_line_color="#000000",  
    marker_line_width=2,
    textposition="outside"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("### Analysis")
    st.write("""
The graph shows total orders placed on each weekday.
""")

    st.write("### Key Insights")
    st.write("""
• Identifies the busiest weekday.

• Helps plan staffing and inventory.

• Useful for weekly demand analysis.
""")

    # =====================================================
    # Research Question 4
    # =====================================================

    st.header("Research Question 4")
    st.subheader("During which hour are the highest number of orders received?")

    hour_orders = df.groupby("hours").size().reset_index(name="Orders")

    fig = px.line(
        hour_orders,
        x="hours",
        y="Orders",
        markers=True,
        title="Orders by Hour",
        color_discrete_sequence=["#FFD400" ]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("### Analysis")
    st.write("""
The graph shows customer ordering activity during different hours of the day.
""")

    st.write("### Key Insights")
    st.write("""
• Peak hours receive the highest number of orders.

• Low-demand hours have fewer orders.

• Useful for delivery planning.
""")

    # =====================================================
    # Research Question 5
    # =====================================================

    st.header("Research Question 5")
    st.subheader("Which month records the highest number of orders?")

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    month_orders = (
        df["month name"]
        .value_counts()
        .reindex(month_order)
        .reset_index()
    )

    month_orders.columns = ["Month", "Orders"]

    fig = px.bar(
        month_orders,
        x="Month",
        y="Orders",
        color="Orders",
        text="Orders",
        title="Orders by Month",
        
    )
    fig.update_traces(
    marker_color="#FFD400",          
    marker_line_color="#000000",    
    marker_line_width=2
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("### Analysis")
    st.write("""
This graph compares total monthly orders.
""")

    st.write("### Key Insights")
    st.write("""
• Shows highest and lowest order months.

• Useful for seasonal demand forecasting.

• Helps in planning promotional campaigns.
""")

    # =====================================================
    # Research Question 6
    # =====================================================

    st.header("Research Question 6")
    st.subheader("What is the distribution of different delivery statuses?")

    delivery_status = df["delivery_status"].value_counts().reset_index()
    delivery_status.columns = ["Delivery Status", "Orders"]

    fig = px.pie(
        delivery_status,
        names="Delivery Status",
        values="Orders",
        title="Delivery Status Distribution",
        color_discrete_sequence=[
        "#FFD400",   
        "#000000",   
        "#FFEB3B"]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("### Analysis")
    st.write("""
The pie chart shows the percentage of each delivery status.
""")

    st.write("### Key Insights")
    st.write("""
• Delivered orders should have the largest share.

• Cancelled or pending orders indicate areas for improvement.

• Helps evaluate delivery performance.
""")
elif page == "Conclusion":

    st.title("📈 Conclusion")

    st.subheader("Project Conclusion")

    st.write("""
The Blinkit Sales Analysis Dashboard provides valuable insights into customer purchasing
behavior, sales performance, payment preferences, and delivery operations. Through data
cleaning, exploratory data analysis (EDA), and research questions, meaningful business
patterns were identified.

The analysis shows that customer orders vary across different hours, weekdays, and months.
Digital payment methods are widely preferred by customers, while most orders are delivered
successfully. The dashboard helps businesses monitor sales trends, improve operational
efficiency, and make data-driven decisions.

Overall, this project demonstrates how data visualization and analysis can support better
business planning, inventory management, and customer satisfaction.
""")

    st.subheader("Key Findings")

    st.write("""
✅ Total revenue provides an overview of overall business performance.

✅ Peak ordering hours help optimize delivery staff and inventory.

✅ Weekday and monthly trends reveal customer purchasing patterns.

✅ Digital payment methods are the most preferred among customers.

✅ Most orders are successfully delivered, reflecting efficient delivery operations.

✅ Store-wise and payment-wise analysis helps identify high-performing business areas.

✅ Data visualization makes complex business information easier to understand.
""")

    st.subheader("Business Recommendations")

    st.write("""
• Increase inventory during peak ordering hours.

• Provide promotional offers during low-demand periods.

• Encourage digital payments using cashback and discounts.

• Reduce cancelled orders by improving delivery management.

• Focus marketing strategies on high-performing stores.

• Use sales trends for future demand forecasting and inventory planning.
""")

    st.subheader("References")

    st.write("""
1. Blinkit Orders Dataset (Project Dataset)

2. Python Documentation
   https://docs.python.org/3/

3. Pandas Documentation
   https://pandas.pydata.org/docs/

4. NumPy Documentation
   https://numpy.org/doc/

5. Plotly Python Documentation
   https://plotly.com/python/

6. Streamlit Documentation
   https://docs.streamlit.io/

7. Matplotlib Documentation
   https://matplotlib.org/stable/

8. Kaggle
   https://www.kaggle.com/

9. Jupyter Notebook Documentation
   https://jupyter.org/

10. Blinkit Official Website
    https://blinkit.com/
""")

    st.success("✅ Blinkit Sales Analysis Dashboard Completed Successfully.")