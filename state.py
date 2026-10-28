"""Session state management for the portfolio application."""

import streamlit as st


def initialize():
    """Initialize durable session state variables if needed."""
    if "navigation_pages" not in st.session_state:
        st.session_state.navigation_pages = {}
    if "submitted_feedback" not in st.session_state:
        st.session_state.submitted_feedback = None
