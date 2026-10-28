"""Run from this directory: python -m streamlit run app.py."""

from pathlib import Path

import streamlit as st

from content import PROFILE
from screens import achievements, contact, home, my_story, projects, skills
from state import initialize
from ui import footer

st.set_page_config(page_title="Renzo Pogoy | Portfolio & Story", page_icon="🌿", layout="wide")
st.html(f"<style>{Path(__file__).with_name('styles.css').read_text(encoding='utf-8')}</style>")
initialize()

pages = {
    "home": st.Page(home.render, title="Home", icon=":material/home:", default=True),
    "story": st.Page(my_story.render, title="My Story", icon=":material/auto_stories:", url_path="my-story"),
    "skills": st.Page(skills.render, title="Skills", icon=":material/construction:", url_path="skills"),
    "projects": st.Page(projects.render, title="Projects", icon=":material/grid_view:", url_path="projects"),
    "achievements": st.Page(achievements.render, title="Achievements", icon=":material/emoji_events:", url_path="achievements"),
    "contact": st.Page(contact.render, title="Contact & Feedback", icon=":material/alternate_email:", url_path="contact"),
}
st.session_state.navigation_pages = pages
navigation = st.navigation(list(pages.values()), position="sidebar", expanded=True)

with st.sidebar:
    st.markdown('<p class="sidebar-monogram">RP<span> / PORTFOLIO</span></p>', unsafe_allow_html=True)
    st.subheader(PROFILE["name"])
    st.write(f"{PROFILE['program']} student")
    st.caption(PROFILE["institution"])
    st.write(f"Year: {PROFILE['year']}")
    st.write(f"Section: {PROFILE['section']}")
    st.divider()
    st.caption(PROFILE["course"])

navigation.run()
footer()
