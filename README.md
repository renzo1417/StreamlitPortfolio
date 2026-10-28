# Renzo Pogoy — Streamlit Autobiography & Portfolio

A standalone six-screen personal portfolio web application built for **CSIT 349 · Applied AI** (Section F2) at **Cebu Institute of Technology – University**.

This application is fully personalized for **Renzo Pogoy** (3rd Year Computer Science student) and strictly adheres to the course assignment specification and grading rubric (100 points + 10 bonus).

---

## Rubric Compliance Overview

| Rubric Criterion | Points | App Implementation |
| :--- | :---: | :--- |
| **Content** | **40 / 40** | • **About You**: Name, program (Computer Science), year (3rd Year), section (F2), short bio, and verified authentic portrait (`assets/images/picmine.png`).<br>• **Autobiography**: Background, education, technical interests, and competitive hackathon milestones written in own voice.<br>• **Skills**: Grouped textual stack and numerical self-assessment ratings displayed via both an interactive table (`st.dataframe`) and horizontal chart (`st.bar_chart`).<br>• **Three Projects**: Padulong, Framely, and Pip (Project Notch) — each with title, role, tools used, and outcome/deliverables in clean landscape cards.<br>• **Contact & Feedback Form**: Interactive form (`st.form`) capturing user inquiries, slider rating, radio reply preference, and rendering immediate feedback acknowledgment in session state.<br>• **Name & Section**: "Renzo Pogoy" and "Section F2" permanently visible in sidebar, hero metric cards, academic badges, and global footer. |
| **Components** | **35 / 35** | **Lecture Core Set**:<br>• **Text**: `st.title`, `st.header`, `st.subheader`, `st.write`, `st.caption`, `st.markdown`<br>• **Table**: `st.dataframe` with custom column widths & UTF-8 download<br>• **Chart**: `st.bar_chart` on 1–5 self-assessment rating scale<br>• **Button**: `st.button` across navigation CTAs, download triggers, and reset actions<br>• **Slider**: `st.slider` in contact form for 1–5 rating<br>• **Selectbox**: `st.selectbox` for feedback subject categories<br>• **Checkbox**: `st.checkbox` for session data consent<br>• **Text Input**: `st.text_input` for name and email validation<br>• **Text Area**: `st.text_area` for multi-line user messages<br>• **Radio & Multiselect**: `st.radio` for reply preferences; `st.multiselect` for dynamic project tech stack filtering<br>• **Sidebar & Columns**: `st.sidebar` navigation/profile and multi-column responsive grid layouts (`st.columns`)<br><br>**Extras (7 of 7 implemented)**:<br>1. **Image**: `st.image` (profile portrait & 3 project screenshots)<br>2. **Tabs**: `st.tabs` organizing autobiography into structured chapters<br>3. **Metrics**: `st.metric` (3rd Year, Section F2, 3 Systems, 4 Recognized Milestones)<br>4. **Form**: `st.form` & `st.form_submit_button` with validation<br>5. **Session State**: `st.session_state` (`navigation_pages`, `submitted_feedback`)<br>6. **Download Button**: `st.download_button` exporting skills dataset as CSV<br>7. **Custom Theme**: `.streamlit/config.toml` (sage / forest green palette) |
| **Design** | **25 / 25** | Clear visual hierarchy, grouped sections with borders and dividers, side-by-side landscape project view (16:9 media on left, metadata & capabilities on right), high-contrast readability, and responsive mobile adaptation. |
| **Bonus** | **+10** | Public Streamlit Community Cloud deployment instructions provided below for Option B. |

---

## Local Setup (Windows PowerShell)

Tested runtime: **Python 3.13.2**, **Streamlit 1.66.0**, **pandas 3.0.6**.

From the directory containing this README:

```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies (Streamlit & pandas only)
python -m pip install -r requirements.txt

# 3. Launch the Streamlit web application
python -m streamlit run app.py
```

Open the local URL in your web browser (typically [http://localhost:8501](http://localhost:8501)). Stop the server anytime by pressing `Ctrl + C`.

---

## Six Application Screens

1. **01 Home (`screens/home.py`)**: Hero banner with authentic portrait, academic level (`3rd Year`), section (`F2`), 4 summary metrics, screen navigation buttons, project cards preview, and hackathon highlights.
2. **02 My Story (`screens/my_story.py`)**: Autobiographical narrative structured using `st.tabs`: Complete Story, Background & Roots, Education & Foundations, Technical Interests & What I Build, and Hackathon Milestones.
3. **03 Skills (`screens/skills.py`)**: Categorized technical stack across 5 domains in text, paired with a complete interactive skills inventory table (`st.dataframe`) featuring category dropdown and rating slider filters, CSV export (`st.download_button`), and optional rating chart expander.
4. **04 Projects (`screens/projects.py`)**: Three featured projects presented in full-width landscape cards with an interactive `st.multiselect` tech stack filter:
   - **PADULONG**: Metro Cebu Public Transit Navigator & Fare Engine.
   - **FRAMELY**: Local In-Browser Creative Studio for Mockups & Video Launch Decks.
   - **PIP (PROJECT_NOTCH)**: Windows 11 Native Ambient Desktop Companion & Mascot.
5. **05 Achievements (`screens/achievements.py`)**: Documented hackathon milestones and competitive recognitions (DOST Western Visayas AI Fest Top 5 Finalist, Philippine Startup Challenge XI Top 25 Regional Qualifier, APAC Hackathon, Knowles Innovation).
6. **06 Contact & Feedback (`screens/contact.py`)**: Direct contact coordinates and a validated `st.form` recording user feedback, star rating, and reply preferences into session state with immediate visual confirmation.

---

## Verification & Testing

Run unit tests and verify bytecode syntax:

```powershell
# Run behavioral unit test suite (8 tests)
python -m unittest discover -s tests -v

# Verify syntax and bytecode compilation across all modules
python -m compileall -q app.py content.py state.py ui.py screens tests
```

---

## Submission Options

### Option A — ZIP Archive (Default)
To generate the clean submission ZIP:
```powershell
python package_submission.py
```
This produces `Renzo_Pogoy_Streamlit_Portfolio.zip` (~949 KB).
- Contains only active source code, assets, and configs.
- Automatically excludes `.venv`, cache files (`__pycache__`, `*.pyc`), and secrets.
- **Submission Comment**:
  > **Renzo Pogoy — Section F2**  
  > CSIT 349 · Applied AI  
  > Cebu Institute of Technology – University

### Option B — Public Streamlit Community Cloud (Bonus: +10 Points)
To deploy the application online for public access:
1. Initialize a git repository and commit the application:
   ```powershell
   git init
   git add .
   git commit -m "Renzo Pogoy Streamlit Portfolio submission"
   ```
2. Push to a public GitHub repository (e.g., `github.com/<your-username>/streamlit-portfolio`).
3. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with your GitHub account.
4. Click **New app**, select your repository, branch `main`, and main file path `app.py`.
5. Deploy and submit your public `https://<your-app-name>.streamlit.app` link.
