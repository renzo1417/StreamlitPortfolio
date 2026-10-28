"""Real local-browser checks for the Streamlit portfolio.

Start the app, then run this file:
python tests/browser_check.py
"""

import argparse
import json
from pathlib import Path
import re

from playwright.sync_api import expect, sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument('--url', default='http://127.0.0.1:8501')
parser.add_argument('--channel', default='msedge')
parser.add_argument('--output', default='test-results')
args = parser.parse_args()
OUTPUT = Path(args.output).resolve()
OUTPUT.mkdir(parents=True, exist_ok=True)
report = {"viewports": [], "checks": []}


def ready(page):
    expect(page.get_by_test_id('stException')).to_have_count(0)
    expect(page.get_by_role('main').get_by_text('Renzo Pogoy · Cebu, Philippines · CSIT 349 · Applied AI', exact=True)).to_be_visible()
    expect(page.get_by_test_id('stApp')).to_have_attribute('data-test-script-state', 'notRunning')


def navigate(page, name, heading):
    expand = page.get_by_role('button', name='Expand sidebar', exact=True)
    if expand.is_visible():
        expand.click()
    page.get_by_role('link', name=name, exact=True).click()
    expect(page.get_by_role('heading', name=heading, exact=True)).to_be_visible()
    if page.viewport_size['width'] < 1000:
        collapse = page.get_by_role('button', name='Collapse sidebar', exact=True)
        if collapse.is_visible():
            collapse.click()
        page.get_by_test_id('stSidebar').evaluate('(e)=>Promise.all(e.getAnimations().map(a=>a.finished.catch(()=>{})))')
    ready(page)


def assert_no_overflow(page):
    page.wait_for_function('document.documentElement.scrollWidth <= innerWidth && document.querySelector("main").scrollWidth <= document.querySelector("main").clientWidth + 1', timeout=5000)
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Document overflows horizontally'
    assert page.get_by_role('main').evaluate('(e)=>e.scrollWidth <= e.clientWidth + 1'), 'Main content overflows horizontally'


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel=args.channel, headless=True)
    context = browser.new_context(viewport={'width': 1366, 'height': 900})
    page = context.new_page()
    page.set_default_timeout(15000)
    try:
        page.goto(args.url)
        expect(page.get_by_role('heading', name='RENZO POGOY', exact=True)).to_be_visible()
        ready(page)
        expect(page.get_by_test_id('stMetric')).to_have_count(4)
        report['checks'].append('Home and hero metrics loaded successfully (4 metrics)')

        # Test Hero navigation buttons
        page.get_by_role('button', name='Explore Projects', exact=True).click()
        expect(page.get_by_role('heading', name='Projects', exact=True)).to_be_visible()
        ready(page)
        for title in ['PADULONG', 'FRAMELY', 'PIP (PROJECT_NOTCH)']:
            expect(page.get_by_text(title, exact=False)).to_be_visible()
        report['checks'].append('Projects rendered with all three software systems')

        navigate(page, 'My Story', 'My Story')
        for section in ['Background', 'Education', 'What I Like Building', 'My Learning Journey']:
            expect(page.get_by_role('heading', name=section, exact=True)).to_be_visible()
        report['checks'].append('My Story rendered with all four biographical sections')

        navigate(page, 'Skills', 'Skills')
        for category in ['Programming Languages', 'Web & Backend', 'Desktop & Creative Tools', 'Data & Storage', 'AI & Native Integrations']:
            expect(page.get_by_text(category, exact=False).first).to_be_visible()
        report['checks'].append('Skills rendered with all 5 engineering domains in Core Competencies table')

        navigate(page, 'Achievements', 'Achievements')
        expect(page.get_by_text('Top 5 Finalist', exact=False)).to_be_visible()
        expect(page.get_by_text('Philippine Startup Challenge XI', exact=False)).to_be_visible()
        report['checks'].append('Achievements rendered competition cards and recognitions')

        # Multi-viewport responsive checks
        for width in [390, 768, 1366]:
            viewport_context = browser.new_context(viewport={'width': width, 'height': 900})
            viewport_page = viewport_context.new_page()
            viewport_page.goto(args.url)
            ready(viewport_page)
            for name, title in [('Home', 'RENZO POGOY'), ('My Story', 'My Story'), ('Skills', 'Skills'), ('Projects', 'Projects'), ('Achievements', 'Achievements')]:
                navigate(viewport_page, name, title)
                viewport_page.wait_for_function('Array.from(document.querySelectorAll("[data-testid=stImage] img")).every(i=>i.complete && i.naturalWidth > 0)')
                assert_no_overflow(viewport_page)
                if name == 'Home':
                    viewport_page.get_by_role('heading', name=title, exact=True).scroll_into_view_if_needed()
                viewport_page.screenshot(path=str(OUTPUT / f'{width}-{name.lower().replace(" ", "-")}.png'))
            report['viewports'].append({'width': width, 'screens': 5, 'overflow': False})
            viewport_context.close()
        report['checks'].append('All five screens verified at 390/768/1366px without horizontal overflow')

        (OUTPUT / 'report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(json.dumps(report, indent=2))
    except Exception:
        page.screenshot(path=str(OUTPUT / 'failure.png'))
        raise
    finally:
        context.close()
        browser.close()
