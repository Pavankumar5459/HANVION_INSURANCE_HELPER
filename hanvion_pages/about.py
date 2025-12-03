import streamlit as st

def show_about():
    st.markdown("## About Hanvion Health")

    st.write(
        """
        Hanvion Health is an intelligent platform designed to help patients, 
        families, and providers understand U.S. health insurance with clarity 
        and confidence.

        Our mission is to simplify:

        - Insurance eligibility  
        - Health plan selection  
        - Expected cost estimation  
        - National healthcare spending insights  

        Hanvion pairs data, clear explanations, and AI assistance to make 
        healthcare planning easier and more transparent.
        """
    )

    st.markdown("### Vision")
    st.write(
        """
        To become a trusted decision-support platform that improves how individuals 
        understand, choose, and use health insurance.
        """
    )

    st.markdown("### Who This Platform Helps")
    st.write(
        """
        - Patients learning about insurance  
        - Providers helping patients estimate costs  
        - Students studying U.S. healthcare  
        - Startups building eligibility or pricing tools  
        """
    )
