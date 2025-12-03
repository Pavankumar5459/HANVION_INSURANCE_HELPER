import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import zipfile
import os


# ----------------------------------------------------
# Utility: Safe File Loaders
# ----------------------------------------------------
def load_excel(path, sheet_name=None):
    try:
        return pd.read_excel(path, sheet_name=sheet_name)
    except Exception:
        st.error(f"Could not load file: {path}")
        return None


def load_zip_csv(zip_path, filename_contains):
    try:
        with zipfile.ZipFile(zip_path) as z:
            match = [f for f in z.namelist() if filename_contains.lower() in f.lower()]
            if match:
                return pd.read_csv(z.open(match[0]))
            else:
                st.error(f"No file in ZIP contains: {filename_contains}")
                return None
    except Exception:
        st.error(f"Could not read zip file: {zip_path}")
        return None


# ----------------------------------------------------
# NHE Dashboard
# ----------------------------------------------------
def show_nhe_dashboard():
    st.title("National Health Expenditure Dashboard")

    st.write(
        "National spending data from CMS NHE tables. This dashboard provides insight into "
        "healthcare cost trends across services, payers, and states."
    )

    # Paths
    provider_path = "data/Provider_all_tables.xlsx"
    residence_path = "data/Residence_all_tables.xlsx"
    proj_zip = "data/nhe-projections-tables-1-18.zip"
    nhe_zip = "data/nhe23-tables.zip"

    st.subheader("1. Total National Health Expenditure Trend")

    # Load from NHE ZIP
    df_total = load_zip_csv(nhe_zip, "nhe-tab")
    if df_total is not None:
        # Attempt to find year + total spending columns
        year_col = [c for c in df_total.columns if "Year" in c or "year" in c.lower()]
        value_col = [c for c in df_total.columns if "Total" in c or "total" in c.lower()]

        if year_col and value_col:
            df_plot = df_total[[year_col[0], value_col[0]]].rename(
                columns={year_col[0]: "Year", value_col[0]: "Total Spending"}
            )

            fig = px.line(df_plot, x="Year", y="Total Spending",
                          title="Total National Health Expenditures Over Time",
                          markers=True)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Could not find Year/Total columns in the NHE dataset.")

    st.subheader("2. Private Insurance vs Out-of-Pocket Trend")

    if df_total is not None:
        priv = [c for c in df_total.columns if "Private" in c]
        oop = [c for c in df_total.columns if "Out-of-pocket" in c or "OOP" in c]

        if priv and oop:
            df_plot = df_total[[year_col[0], priv[0], oop[0]]].rename(
                columns={year_col[0]: "Year", priv[0]: "Private Insurance", oop[0]: "Out-of-pocket"}
            )
            fig = px.line(df_plot, x="Year", y=["Private Insurance", "Out-of-pocket"],
                          title="Private Insurance vs Out-of-pocket Spending")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Private/OOP columns not found.")

    st.subheader("3. Provider Spending (Hospitals, Physicians, etc.)")

    df_provider = load_excel(provider_path)
    if df_provider is not None:
        # Try to pick first sheet if needed
        if isinstance(df_provider, dict):
            df_provider = list(df_provider.values())[0]

        # Auto-detect provider categories
        year_col = [c for c in df_provider.columns if "Year" in c or "YEAR" in c]
        cat_cols = [c for c in df_provider.columns if c not in year_col]

        if year_col:
            df_long = df_provider.melt(id_vars=year_col[0], value_vars=cat_cols,
                                       var_name="Category", value_name="Spending")

            fig = px.line(df_long, x=year_col[0], y="Spending", color="Category",
                          title="Provider-Type Spending Trends")
            st.plotly_chart(fig, use_container_width=True)

    st.subheader("4. State-Level Spending Map")

    df_state = load_excel(residence_path)
    if df_state is not None:

        # Find state + spending column heuristically
        state_col = [c for c in df_state.columns if "State" in c or "state" in c.lower()]
        spend_col = [c for c in df_state.columns if "Total" in c or "Spending" in c]

        if state_col and spend_col:
            df_map = df_state[[state_col[0], spend_col[0]]].rename(
                columns={state_col[0]: "State", spend_col[0]: "Spending"}
            )

            fig = px.choropleth(
                df_map,
                locations="State",
                locationmode="USA-states",
                color="Spending",
                color_continuous_scale="Blues",
                scope="usa",
                title="Health Spending by State"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Could not find State/Spending columns in dataset.")

    st.subheader("5. Projections (2023–2035)")

    df_proj = load_zip_csv(proj_zip, "proj")
    if df_proj is not None:
        # Try to detect projection years and columns
        year_candidates = [c for c in df_proj.columns if "Year" in c or "year" in c.lower()]
        value_candidates = [c for c in df_proj.columns if "Total" in c or "Expenditure" in c or "Spending" in c]

        if year_candidates and value_candidates:
            df_p = df_proj[[year_candidates[0], value_candidates[0]]].rename(
                columns={year_candidates[0]: "Year", value_candidates[0]: "Projected Spending"}
            )

            fig = px.line(df_p, x="Year", y="Projected Spending",
                          title="Projected National Health Expenditure (2023–2035)",
                          markers=True)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Projection columns not found.")

