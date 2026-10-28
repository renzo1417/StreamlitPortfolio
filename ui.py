"""Shared native controls and content presentation."""

from html import escape
from pathlib import Path

import streamlit as st

from content import PROFILE

APP_ROOT = Path(__file__).resolve().parent


def asset_path(relative):
    return APP_ROOT / relative


def image(relative, caption):
    path = asset_path(relative)
    if path.is_file():
        st.image(str(path), caption=caption, alt=caption, width="stretch")
    else:
        st.markdown(f'<div class="media-placeholder">Image unavailable: {escape(caption)}</div>', unsafe_allow_html=True)


def heading(number, title, description):
    st.markdown(f'<p class="eyebrow">{escape(PROFILE["name"].upper())} / {number}</p>', unsafe_allow_html=True)
    st.title(title)
    st.write(description)


def academic_identity():
    st.write(f"**{PROFILE['program']}** · {PROFILE['institution']}")
    st.caption(f"Year: {PROFILE['year']}  ·  Section: {PROFILE['section']}")


def footer():
    st.divider()
    st.caption(f"{PROFILE['name']} · Section {PROFILE['section']} · {PROFILE['institution']} · {PROFILE['course']}")
