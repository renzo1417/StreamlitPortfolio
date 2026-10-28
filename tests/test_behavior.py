"""Run: python -m unittest discover -s tests -v (from app directory)."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

APP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_ROOT))

from PIL import Image
from streamlit.testing.v1 import AppTest

from content import COMPETITIONS, PROFILE, PROJECTS, SKILL_GROUPS


def screen_app(screen):
    code = """
import streamlit as st
from state import initialize
from screens import skills, achievements, my_story, projects, contact
st.set_page_config(layout='wide')
initialize()
screens = {'skills': skills, 'achievements': achievements, 'story': my_story, 'projects': projects, 'contact': contact}
screens[st.session_state.get('test_screen', 'skills')].render()
"""
    app = AppTest.from_string(code, default_timeout=20)
    app.session_state.test_screen = screen
    return app.run()


class PortfolioBehavior(unittest.TestCase):
    def assert_clean(self, app):
        self.assertEqual([item.message for item in app.exception], [])

    def test_assets_and_content(self):
        with Image.open(APP_ROOT / PROFILE['portrait']) as image:
            image.verify()
        self.assertEqual(PROFILE['year'], '3rd Year')
        self.assertEqual(PROFILE['section'], 'F2')
        self.assertEqual(PROFILE['role'], '3rd Year Computer Science Student')
        self.assertEqual(PROFILE['focus'], 'Aspiring AI Engineer & Full-Stack Developer')
        self.assertEqual(PROFILE['github'], '')
        self.assertEqual(PROFILE['linkedin'], '')
        self.assertEqual(len(COMPETITIONS), 4)
        self.assertEqual(len(PROJECTS), 3)
        self.assertGreaterEqual(len(SKILL_GROUPS), 4)

    def test_home_and_sidebar_rendering(self):
        app = AppTest.from_file(str(APP_ROOT / 'app.py'), default_timeout=20).run()
        self.assert_clean(app)
        metric_values = [metric.value for metric in app.metric]
        self.assertIn('3rd Year', metric_values)
        self.assertIn('F2', metric_values)

    def test_projects_rendering(self):
        app = screen_app('projects')
        self.assert_clean(app)
        self.assertEqual(app.title[0].value, 'Projects')
        for project in PROJECTS:
            self.assertTrue(any(project['title'] in subheader.value for subheader in app.subheader))

    def test_achievements_rendering(self):
        app = screen_app('achievements')
        self.assert_clean(app)
        self.assertEqual(app.title[0].value, 'Achievements')

    def test_skills_rendering(self):
        app = screen_app('skills')
        self.assert_clean(app)
        self.assertEqual(app.title[0].value, 'Skills')
        self.assertGreaterEqual(len(app.dataframe), 1)
        self.assertGreaterEqual(len(app.get('vega_lite_chart')), 1)
        df = app.dataframe[0].value
        for category in SKILL_GROUPS.keys():
            self.assertIn(category, df["Domain"].values)

    def test_story_rendering(self):
        app = screen_app('story')
        self.assert_clean(app)
        self.assertEqual(app.title[0].value, 'My Story')

    def test_contact_rendering(self):
        app = screen_app('contact')
        self.assert_clean(app)
        self.assertEqual(app.title[0].value, 'Contact & Feedback')
        self.assertGreaterEqual(len(app.form), 1)

    def test_missing_media_preserves_screen(self):
        with patch('ui.asset_path', return_value=APP_ROOT / 'assets' / 'intentionally-missing-file'):
            app = AppTest.from_file(str(APP_ROOT / 'app.py'), default_timeout=20).run()
            self.assert_clean(app)
            self.assertTrue(any('Image unavailable' in item.value for item in app.markdown))


if __name__ == '__main__':
    unittest.main()
