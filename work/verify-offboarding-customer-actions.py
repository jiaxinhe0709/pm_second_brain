"""Render and check the static diagram locally, with network requests blocked."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'offboarding-and-switch-customer-actions'
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1280, 'height':1000}, device_scale_factor=1)
    page.route('http://**/*', lambda route: route.abort())
    page.route('https://**/*', lambda route: route.abort())
    page.goto((ROOT / 'work/offboarding-review/customer-actions.html').as_uri())
    svg = page.locator('svg').last
    assert svg.locator('a').count() == 17
    assert page.locator('tbody tr').count() == 10
    overflow = svg.locator('text').evaluate_all('''items => items.filter(t => {
        const b=t.getBBox(); return b.x<0 || b.x+b.width>1600 || b.y<0 || b.y+b.height>2430;
    }).map(t=>t.textContent)''')
    assert not overflow, overflow
    # Each card title/subtitle must fit its own shape, not merely the canvas.
    clipping = svg.locator('a').evaluate_all('''items => items.flatMap(a => {
        const s=a.querySelector('rect,path').getBBox();
        return [...a.querySelectorAll('text')].filter(t=>{
            const b=t.getBBox(); return b.x<s.x || b.x+b.width>s.x+s.width || b.y<s.y || b.y+b.height>s.y+s.height;
        }).map(t=>t.textContent);
    })''')
    assert not clipping, clipping
    # Render the source SVG without the preview's intentional scroll clipping.
    page.set_viewport_size({'width':1640, 'height':1000})
    page.goto((ROOT / f'assets/diagrams/{SLUG}.svg').as_uri())
    page.locator('svg').screenshot(path=str(ROOT / f'assets/diagrams/{SLUG}.png'))
    page.goto((ROOT / 'assets/diagrams/e-invoicing-settings-actions.svg').as_uri())
    settings = page.locator('svg')
    assert settings.locator('a').count() == 8
    assert not settings.locator('a').evaluate_all('''items=>items.flatMap(a=>{
        const s=a.querySelector('rect,path').getBBox();
        return [...a.querySelectorAll('text')].filter(t=>{
            const b=t.getBBox();return b.x<s.x || b.x+b.width>s.x+s.width || b.y<s.y || b.y+b.height>s.y+s.height;
        }).map(t=>t.textContent);
    })''')
    settings.screenshot(path=str(ROOT / 'assets/diagrams/e-invoicing-settings-actions.png'))
    page.goto((ROOT / 'work/offboarding-review/customer-actions.html').as_uri())
    page.set_viewport_size({'width':390, 'height':844})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    assert page.locator('.offboarding-actions').count() == 2
    assert page.locator('.offboarding-actions').evaluate_all('items=>items.every(e=>e.scrollWidth>e.clientWidth)')
    page.screenshot(path=str(ROOT / 'work/offboarding-review/customer-actions-narrow.png'))
    result = {'svg_nodes':17, 'settings_nodes':8, 'customer_scenarios':10, 'text_within_canvas_and_cards':True, 'narrow_scroll':True, 'published':False}
    (ROOT / 'work/offboarding-review/customer-actions-validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
    browser.close()
