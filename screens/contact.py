import streamlit as st

from content import PROFILE
from ui import heading


def render():
    heading("06", "Contact & Feedback", "Get in touch or leave session feedback on this portfolio.")
    st.caption("Demonstrates validated form input, native widgets, and durable session state feedback acknowledgment.")

    col_info, col_form = st.columns([1, 1.4], gap="large")

    with col_info:
        with st.container(border=True):
            st.subheader("Direct Contact")
            st.write(f"**Name:** {PROFILE['name']}")
            st.write(f"**Program:** {PROFILE['program']} student")
            st.write(f"**Year & Section:** {PROFILE['year']} — Section {PROFILE['section']}")
            st.write(f"**Institution:** {PROFILE['institution']}")
            st.write(f"**Location:** {PROFILE['location']}")
            st.write(f"**Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})")
            st.divider()
            st.caption("Feedback submitted through the form stays in your current browser session and demonstrates Streamlit's interactive form controls.")

    with col_form:
        with st.container(border=True):
            st.subheader("Send Feedback or Inquiries")

            with st.form(key="portfolio_feedback_form"):
                name = st.text_input("Your Name (required)", placeholder="e.g. Alex Santos")
                email = st.text_input("Your Email (optional)", placeholder="e.g. alex@example.com")
                subject = st.selectbox(
                    "Subject",
                    [
                        "Portfolio Feedback",
                        "Coursework Evaluation",
                        "Project Inquiry",
                        "Collaboration / Hackathon",
                        "Other",
                    ],
                )
                reply_pref = st.radio(
                    "Preferred reply method",
                    ["Email", "Campus In-Person (CIT-U)", "No reply needed"],
                    horizontal=True,
                )
                rating = st.slider("Portfolio Rating (1 to 5)", min_value=1, max_value=5, value=5, help="1 Needs improvement · 5 Excellent")
                message = st.text_area("Your Message / Feedback (required)", placeholder="Enter your thoughts or feedback about the portfolio...")
                consent = st.checkbox("I understand this feedback is recorded for this active browser session.", value=True)

                submitted = st.form_submit_button("Submit Feedback", type="primary")

            if submitted:
                if not name.strip():
                    st.error("Please enter your name before submitting.")
                elif not message.strip():
                    st.error("Please provide a message or feedback before submitting.")
                else:
                    st.session_state.submitted_feedback = {
                        "name": name.strip(),
                        "email": email.strip(),
                        "subject": subject,
                        "reply_pref": reply_pref,
                        "rating": rating,
                        "message": message.strip(),
                    }

            # Response acknowledgment
            feedback = st.session_state.get("submitted_feedback")
            if feedback:
                st.success(f"Thank you, {feedback['name']}! Your {feedback['subject'].lower()} has been recorded for this session.")
                with st.expander("View Submitted Details", expanded=True):
                    st.write(f"**Sender:** {feedback['name']} ({feedback['email'] or 'No email provided'})")
                    st.write(f"**Subject:** {feedback['subject']}")
                    st.write(f"**Rating Given:** {'⭐' * feedback['rating']} ({feedback['rating']}/5)")
                    st.write(f"**Preferred Reply:** {feedback['reply_pref']}")
                    st.write(f"**Message:** {feedback['message']}")
                    if st.button("Submit another response / Clear"):
                        st.session_state.submitted_feedback = None
                        st.rerun()
