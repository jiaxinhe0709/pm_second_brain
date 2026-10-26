"""Check the local 040 preview with external HTTP requests blocked."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'work/onboarding-api-reference-review'
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 1000})
    page.set_default_timeout(5000)
    page.route('http://**/*', lambda route: route.abort())
    page.route('https://**/*', lambda route: route.abort())
    page.goto((OUT / 'SPEC-SEI-040.html').as_uri())
    assert page.locator('pre').count() == 11
    for name in ['B2B Router', 'Banqup (Unifiedpost)', 'EDICOM', 'SERES (Docaposte)', 'ZeroComa']:
        assert name in page.locator('pre').first.inner_text()
    assert page.locator('pre').first.evaluate('(e) => getComputedStyle(e).color') == 'rgb(102, 102, 102)'
    assert page.locator('pre span').first.evaluate('(e) => getComputedStyle(e).color') == 'rgb(21, 101, 192)'
    page.locator('h2').first.scroll_into_view_if_needed()
    page.screenshot(path=str(OUT / 'provider-examples.png'))
    page.locator('h3').first.scroll_into_view_if_needed()
    page.screenshot(path=str(OUT / 'private-provider-catalogue.png'))
    companion = next((ROOT / 'work/onboarding-concise-review').glob('SPEC-SEI-039-*.html'))
    navigation = []
    for index in range(1, 6):
        anchor = f'api-{index:02}'
        page.goto(companion.as_uri())
        page.locator(f'a[href$="#{anchor}"]').first.click()
        assert page.url.endswith('SPEC-SEI-040.html#' + anchor)
        assert f'API-{index:02}' in page.locator(f'#{anchor}').locator('xpath=following::h3[1]').inner_text()
        navigation.append('039 → 040#' + anchor)
    page.locator('a').filter(has_text='039 supported change').first.click()
    assert page.url.endswith('#24-supported-change') and 'SPEC-SEI-039-' in page.url
    navigation.append('040 → 039#24-supported-change')
    page.locator('[id="26-existing-api-and-capability-reuse"]').scroll_into_view_if_needed()
    page.screenshot(path=str(OUT / '039-api-cross-links.png'))
    page.goto((OUT / 'SPEC-SEI-040.html').as_uri())
    viewports = []
    for width in [1280, 768]:
        page.set_viewport_size({'width': width, 'height': 1000})
        overflow = page.evaluate('document.documentElement.scrollWidth > innerWidth')
        assert not overflow
        viewports.append({'width': width, 'page_overflow': overflow})
    (OUT / 'browser-validation.json').write_text(json.dumps({
        'result': 'passed', 'json_examples': 11, 'provider_names': 5,
        'existing_colour': 'rgb(102, 102, 102)', 'spain_colour': 'rgb(21, 101, 192)',
        'viewports': viewports, 'paired_navigation': navigation,
        'published': False}, indent=2) + '\n')
    browser.close()
print('Preview checked: 11 JSON blocks, five provider names, grey/blue colours, desktop and narrow layout.')
