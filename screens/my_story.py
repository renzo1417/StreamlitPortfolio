import streamlit as st

from content import STORY
from ui import academic_identity, heading


def render():
    heading("02", "My Story", "From programming fundamentals to AI engineering and full-stack development.")
    st.caption("Autobiography: academic journey, technical passions, and competitive milestones at Cebu Institute of Technology – University.")
    academic_identity()

    for title, paragraph in STORY.items():
        with st.container(border=True):
            st.header(title)
            st.write(paragraph)
