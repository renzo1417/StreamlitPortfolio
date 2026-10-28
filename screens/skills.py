import pandas as pd
import streamlit as st

from content import DOMAIN_SUMMARIES
from ui import heading


def render():
    heading("03", "Skills", "Technical tools, programming languages, and engineering frameworks.")
    st.caption("Consolidated engineering stack and tools utilized across full-stack, AI, and systems engineering projects.")

    st.markdown('<p class="eyebrow">TECHNOLOGY STACK</p>', unsafe_allow_html=True)
    st.header("Core Competencies & Tools")
    st.caption("Overview of technical tools utilized across full-stack, AI, and systems engineering projects:")

    df = pd.DataFrame(DOMAIN_SUMMARIES)[["Domain", "Tools & Frameworks"]]
    st.dataframe(
        df,
        hide_index=True,
        width="stretch",
        column_config={
            "Domain": st.column_config.TextColumn(
                "Engineering Domain",
                width="medium",
                help="High-level engineering domain",
            ),
            "Tools & Frameworks": st.column_config.ListColumn(
                "Core Technologies & Tools",
                width="large",
                help="Primary languages, libraries, and frameworks",
            ),
        },
    )

    with st.expander("📊 View Tool Distribution by Domain"):
        chart_data = pd.DataFrame(
            [
                {
                    "Domain": row["Domain"],
                    "Number of Tools": len(row["Tools & Frameworks"]),
                }
                for row in DOMAIN_SUMMARIES
            ]
        ).set_index("Domain")
        st.bar_chart(chart_data, color="#52633D", horizontal=True)
