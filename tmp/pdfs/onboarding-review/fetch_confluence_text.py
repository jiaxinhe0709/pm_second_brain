from pathlib import Path
import sys

from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.update_confluence_pages import confluence_client, load_workspace_env


if len(sys.argv) < 2:
    raise SystemExit("usage: fetch_confluence_text.py <page-id> [<page-id> ...]")

load_workspace_env(Path("tools/update_confluence_pages.py"))
client = confluence_client()
output_dir = Path("tmp/pdfs/onboarding-review")

for page_id in sys.argv[1:]:
    page = client.get_page_by_id(page_id, expand="version,body.storage")
    storage = page["body"]["storage"]["value"]
    soup = BeautifulSoup(storage, "html.parser")
    for element in soup(["style", "script"]):
        element.decompose()
    text = soup.get_text("\n", strip=True)
    (output_dir / f"confluence-{page_id}.html").write_text(storage, encoding="utf-8")
    (output_dir / f"confluence-{page_id}.txt").write_text(text, encoding="utf-8")
    print(f"page={page_id} version={page['version']['number']} title={page['title']} chars={len(text)}")
