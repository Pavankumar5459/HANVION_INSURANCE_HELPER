import streamlit as st
import pandas as pd

def show_nhe_dashboard():
    st.title("National Health Expenditure (NHE) Dashboard")
    st.write(
        "This dashboard provides an overview of U.S. national healthcare spending trends. "
        "Real data can be connected once uploaded."
    )

    # --------------------------------------------------
    # SAMPLE DATA (Replace with your uploaded dataset)
    # --------------------------------------------------
    data = {
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Total Spending (Billion $)": [3500, 3600, 4100, 4300, 4500],
        "Hospital Care": [1200, 1230, 1400, 1450, 1500],
        "Physician Services": [750, 770, 820, 850, 880],
        "Prescription Drugs": [350, 365, 390, 410, 430],
        "Medicare": [625, 650, 750, 780, 820],
        "Medicaid": [600, 620, 700, 740, 780],
        "Private Insurance": [1200, 1250, 1350, 1400, 1450],
        "Out-of-Pocket": [350, 360, 380, 400, 420]
    }

    df = pd.DataFrame(data)

    # --------------------------------------------------
    # VIEW FULL DATA
    # --------------------------------------------------
    st.subheader("NHE Summary Table")
    st.dataframe(df, use_container_width=True)

    # --------------------------------------------------
    # CHOOSE METRIC TO PLOT
    # --------------------------------------------------
    st.subheader("Trend Visualization")

    metric = st.selectbox(
        "Select a category to visualize:",
        [
            "Total Spending (Billion $)",
            "Hospital Care",
            "Physician Services",
            "Prescription Drugs",
            "Medicare",
            "Medicaid",
            "Private Insurance",
            "Out-of-Pocket"
        ],
    )

    st.line_chart(
        df.set_index("Year")[metric]
    )

    # --------------------------------------------------
    # SUMMARY INSIGHTS
    # --------------------------------------------------
    st.subheader("Key Insights")

    most_recent = df.iloc[-1]
    previous = df.iloc[-2]

    growth = most_recent["Total Spending (Billion $)"] - previous["Total Spending (Billion $)"]

    st.write(f"• Total national health spending in **{most_recent['Year']}** was **${most_recent['Total Spending (Billion $)']}B**.")
    st.write(f"• This is an increase of **${growth}B** from the previous year.")
    st.write(f"• Hospital care remains the largest spending category at **${most_recent['Hospital Care']}B**.")
    st.write(f"• Medicare and Medicaid continue to rise due to population aging and eligibility expansion.")

    st.markdown("---")
    st.caption("This dashboard uses sample data. Real NHE tables can be uploaded anytime for live analysis.")
