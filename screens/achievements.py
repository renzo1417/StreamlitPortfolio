import streamlit as st

from content import COMPETITIONS
from ui import heading


def render():
    heading("05", "Achievements", "Hackathon competitions, regional recognition, and collaborative technology innovation.")
    st.caption("Documented hackathon milestones and competitive recognitions.")

    for event in COMPETITIONS:
        with st.container(border=True):
            cols = st.columns([3, 1])
            with cols[0]:
                st.subheader(event["recognition"])
                st.write(f"**{event['title']}**")
                st.write(event["details"])
            with cols[1]:
                st.markdown(f"**Year:** `{event['year']}`")
