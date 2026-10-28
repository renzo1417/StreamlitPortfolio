import streamlit as st

from content import PROJECTS
from ui import heading, image


def render():
    heading("04", "Projects", "Three featured software systems spanning Applied AI, in-browser creative tools, and native desktop companions.")
    st.caption("Each project is presented with its architectural approach, problem statement, technical capabilities, and verified outcomes.")

    # Filter by tech stack using st.multiselect (lecture component demonstration)
    all_tools = sorted({tool for project in PROJECTS for tool in project["tools"]})
    selected_tools = st.multiselect(
        "Filter projects by technology stack:",
        options=all_tools,
        placeholder="Choose one or more technologies (e.g. Next.js, Rust, Python)...",
        help="Filter the landscape project cards below by specific frameworks or languages.",
    )

    displayed_projects = [
        project
        for project in PROJECTS
        if not selected_tools or any(tool in project["tools"] for tool in selected_tools)
    ]

    if not displayed_projects:
        st.info("No projects match the selected technology filters. Clear or adjust your filter selection above.")

    for project in displayed_projects:
        with st.container(border=True):
            col_media, col_info = st.columns([1.35, 1.15], gap="large")
            with col_media:
                image(project["image"], f"{project['title']} preview")
                st.caption(f"**Architecture & Implementation:** {project['approach']}")
            with col_info:
                st.caption(f"{project['platform_label']} · {project['status']}")
                st.subheader(project["title"])
                st.write(project["summary"])
                st.markdown(f"**Problem Statement:** {project['problem']}")
                st.markdown("##### Core Capabilities")
                for capability in project["capabilities"]:
                    st.write(f"• {capability}")
                st.markdown(f"**Tech Stack:** `{'` · `'.join(project['tools'])}`")
                st.markdown(f"**My Role:** {project['role']}")
                st.markdown(f"**Outcome & Deliverables:** {project['outcome']}")
