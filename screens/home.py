from html import escape

import pandas as pd
import streamlit as st

from content import COMPETITIONS, DOMAIN_SUMMARIES, PROFILE, PROJECTS
from ui import academic_identity, image


def render():
    with st.container(key="home-hero"):
        text, portrait = st.columns([1.7, 1], gap="large", vertical_alignment="center")
        with text:
            st.markdown(f'<p class="eyebrow">BASED IN {escape(PROFILE["location"].upper())}</p>', unsafe_allow_html=True)
            st.markdown(f'<h1 class="hero-name">{escape(PROFILE["name"].upper())}</h1>', unsafe_allow_html=True)
            st.subheader(PROFILE["role"])
            st.write(f"**{PROFILE['focus']}**")
            st.write(PROFILE["intro"])
            academic_identity()
            with st.container(horizontal=True):
                if st.button("Explore Projects", type="primary"):
                    st.switch_page(st.session_state.navigation_pages["projects"])
                if st.button("Read My Story"):
                    st.switch_page(st.session_state.navigation_pages["story"])
                if st.button("Skills"):
                    st.switch_page(st.session_state.navigation_pages["skills"])
                if st.button("Achievements"):
                    st.switch_page(st.session_state.navigation_pages["achievements"])
                if st.button("Contact"):
                    st.switch_page(st.session_state.navigation_pages["contact"])
        with portrait:
            with st.container(key="home-portrait"):
                image(PROFILE["portrait"], "Renzo Pogoy · Computer Science student")

    st.divider()
    metrics = [
        ("Academic Level", PROFILE["year"]),
        ("Class Section", PROFILE["section"]),
        ("Featured Projects", f"{len(PROJECTS)} Systems"),
        ("Competitions & Hackathons", f"{len(COMPETITIONS)} Recognized"),
    ]
    for column, (label, value) in zip(st.columns(4), metrics):
        column.metric(label, value)

    st.divider()
    st.markdown('<p class="eyebrow">FEATURED PROJECTS</p>', unsafe_allow_html=True)
    st.header("Built for Everyday & Creative Needs")
    st.write("Metro Cebu transit guidance, in-browser studio mockups, and ambient desktop companions.")

    cols = st.columns(3, gap="medium")
    for col, project in zip(cols, PROJECTS):
        with col:
            with st.container(border=True):
                image(project["image"], f"{project['title']} preview")
                st.caption(project["platform_label"])
                st.subheader(project["title"])
                st.write(project["summary"])
                st.caption(f"**Tech:** {', '.join(project['tools'][:3])}")

    if st.button("View project details and technical architecture ↗"):
        st.switch_page(st.session_state.navigation_pages["projects"])

    st.divider()
    st.markdown('<p class="eyebrow">CORE COMPETENCIES</p>', unsafe_allow_html=True)
    st.header("Technical Stack & Tools")
    st.write("Overview of engineering domains and primary technologies used across systems:")

    home_skills_df = pd.DataFrame(
        [
            {
                "Domain": row["Domain"],
                "Tools & Frameworks": row["Tools & Frameworks"],
            }
            for row in DOMAIN_SUMMARIES
        ]
    )
    st.dataframe(
        home_skills_df,
        hide_index=True,
        width="stretch",
        column_config={
            "Domain": st.column_config.TextColumn(
                "Engineering Domain",
                width="medium",
            ),
            "Tools & Frameworks": st.column_config.ListColumn(
                "Core Technologies",
                width="large",
            ),
        },
    )

    if st.button("View full skills and engineering scope ↗"):
        st.switch_page(st.session_state.navigation_pages["skills"])

    st.divider()
    st.markdown('<p class="eyebrow">HIGHLIGHTED ACHIEVEMENTS</p>', unsafe_allow_html=True)
    st.header("Recognition & Competitive Milestones")
    st.write("Key hackathon accomplishments and regional competition qualifications.")

    for event in COMPETITIONS[:2]:
        with st.container(border=True):
            st.caption(f"Year {event['year']}")
            st.subheader(event["recognition"])
            st.write(f"**{event['title']}**")
            st.write(event["details"])

    if st.button("View all achievements and details ↗"):
        st.switch_page(st.session_state.navigation_pages["achievements"])
