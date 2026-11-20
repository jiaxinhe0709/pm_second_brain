#!/usr/bin/env python3
"""Render canonical topic question tables into the existing review HTML."""

import argparse
import html
from pathlib import Path
import posixpath
import re
from urllib.parse import quote, unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "work/spain-solution-review-questions.html"
TOPICS = {
    "onboarding": {
        "source": "specs/onboarding-and-connectivity/NOTE-SEI-001-onboarding-questions-and-decisions.md",
        "id": "NOTE-SEI-001", "prefix": "onb", "parents": "Q06, Q08 and Q31",
        "command": "python3 tools/render_onboarding_question_log.py",
    },
    "sending": {
        "source": "specs/invoice-sending/NOTE-SEI-002-sending-questions-and-decisions.md",
        "id": "NOTE-SEI-002", "prefix": "snd", "parents": "Q06, Q20 and Q30",
        "command": "python3 tools/render_question_logs.py",
    },
    "receiving": {
        "source": "specs/invoice-receiving/NOTE-SEI-003-receiving-questions-and-decisions.md",
        "id": "NOTE-SEI-003", "prefix": "rcv", "parents": "Q14 and Q16",
        "command": "python3 tools/render_question_logs.py",
    },
}
HEADERS = [
    "ID and area", "Current understanding", "Question or decision needed", "State",
    "Decision or evidence", "Suggested owner and next action", "Affected specs or diagrams",
]
STATES = {
    "Open": "open", "Proposed answer": "proposed", "Partly answered": "partial",
    "Decision recorded": "answered",
}


def relative_url(url, source):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        if parts.scheme not in {"http", "https"}:
            raise ValueError(f"Unsupported link: {url}")
        return url
    destination = (source.parent / unquote(parts.path)).resolve() if parts.path else source
    if not destination.is_relative_to(ROOT) or not destination.is_file():
        raise ValueError(f"Missing or out-of-repository link: {url}")
    path = posixpath.relpath(destination.as_posix(), TARGET.parent.as_posix())
    return urlunsplit(("", "", quote(path, safe="/"), parts.query, parts.fragment))


def inline(text, source):
    """Support the table's plain text, code and Markdown links without raw HTML."""
    result = []
    cursor = 0
    for match in re.finditer(r"`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)", text):
        result.append(html.escape(text[cursor:match.start()]))
        code, label, url = match.groups()
        if code is not None:
            result.append(f"<code>{html.escape(code)}</code>")
        else:
            result.append(f'<a href="{html.escape(relative_url(url, source), quote=True)}">{html.escape(label)}</a>')
        cursor = match.end()
    result.append(html.escape(text[cursor:]))
    return "".join(result)


def read_rows(topic):
    table_start = f"<!-- {topic}-log-table:start -->"
    table_end = f"<!-- {topic}-log-table:end -->"
    source = (ROOT / TOPICS[topic]["source"]).read_text(encoding="utf-8")
    if source.count(table_start) != 1 or source.count(table_end) != 1:
        raise ValueError("Expected one marked topic table")
    lines = source.split(table_start, 1)[1].split(table_end, 1)[0].strip().splitlines()
    cells = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(cells) < 3 or cells[0] != HEADERS or any(not re.fullmatch(r":?-{3,}:?", c) for c in cells[1]):
        raise ValueError("Unexpected topic table headers or separator")
    rows = cells[2:]
    seen = set()
    for row in rows:
        if len(row) != len(HEADERS):
            raise ValueError(f"Expected {len(HEADERS)} cells: {row}")
        match = re.fullmatch(r'<a id="(q\d+-\d+)"></a>(Q\d+\.\d+) — (.+)', row[0])
        if not match:
            raise ValueError(f"Missing stable question anchor: {row[0]}")
        anchor, question_id, _ = match.groups()
        if anchor != question_id.lower().replace(".", "-") or anchor in seen:
            raise ValueError(f"Duplicate or mismatched question ID: {row[0]}")
        seen.add(anchor)
        if row[3] not in STATES:
            raise ValueError(f"Unknown question state: {row[3]}")
    return rows


def render(topic, rows):
    config = TOPICS[topic]
    source = ROOT / config["source"]
    source_link = html.escape(relative_url("", source), quote=True)
    result = [
        f"<!-- {topic}-topic-log:start -->",
        f'<section id="{topic}-topic-log" aria-labelledby="{topic}-topic-heading">',
        f'<h2 id="{topic}-topic-heading">{topic.capitalize()} question and decision log</h2>',
        f'<p>Read the <a href="{source_link}">{topic} source table — {config["id"]}</a>. '
        'This view shows the questions and answers from that table.</p>',
        f'<p>These {len(rows)} entries add detail to {config["parents"]}. They are counted separately '
        'from the original workshop questions. The owner column suggests who to ask. '
        'An agreed decision does not mean the software is built or tested.</p>',
        '<details><summary>How to update this view</summary>'
        f'<p>Edit the source table, then run <code>{config["command"]}</code>.</p></details>',
    ]
    for row in rows:
        anchor, question_id, area = re.fullmatch(
            r'<a id="(q\d+-\d+)"></a>(Q\d+\.\d+) — (.+)', row[0]
        ).groups()
        state = row[3]
        result.extend([
            f'<article id="{config["prefix"]}-{anchor}">',
            f'<h3>{html.escape(question_id)}. {html.escape(area)}</h3>',
            f'<span class="badge {STATES[state]}">{html.escape(state)}</span>',
            f'<p class="question">{inline(row[2], source)}</p>',
            f'<p class="answer"><strong>Current understanding:</strong> {inline(row[1], source)}</p>',
            f'<p class="evidence"><strong>Decision or evidence:</strong> {inline(row[4], source)}</p>',
            f'<p class="followup"><strong>Suggested owner and next action:</strong> {inline(row[5], source)}</p>',
            f'<p class="details"><strong>Affected specs or diagrams:</strong> {inline(row[6], source)}</p>',
            f'<p class="evidence"><a href="{source_link}#{anchor}">Source entry {html.escape(question_id)}</a></p>',
            '</article>',
        ])
    result.extend(['</section>', f'<!-- {topic}-topic-log:end -->'])
    return "\n".join(result)


def main(default_topics=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topics", nargs="*", help="Topics to render; default: all")
    parser.add_argument("--check", action="store_true", help="Fail if a generated section is stale")
    args = parser.parse_args()
    topics = args.topics or default_topics or list(TOPICS)
    unknown = set(topics) - TOPICS.keys()
    if unknown:
        parser.error(f"Unknown topics: {', '.join(sorted(unknown))}")
    content = TARGET.read_text(encoding="utf-8")
    updated = content
    counts = []
    for topic in topics:
        rows = read_rows(topic)
        start = f"<!-- {topic}-topic-log:start -->"
        end = f"<!-- {topic}-topic-log:end -->"
        if updated.count(start) != 1 or updated.count(end) != 1:
            raise ValueError(f"Expected one generated {topic} section in the question HTML")
        before, remaining = updated.split(start, 1)
        _, after = remaining.split(end, 1)
        updated = before + render(topic, rows) + after
        counts.append(f"{topic}: {len(rows)}")
    if args.check:
        if updated != content:
            parser.exit(1, "Topic HTML is stale; run tools/render_question_logs.py\n")
        print("HTML matches canonical entries — " + "; ".join(counts) + ".")
    else:
        if updated != content:
            TARGET.write_text(updated, encoding="utf-8")
        print("Rendered canonical entries — " + "; ".join(counts) + ".")


if __name__ == "__main__":
    main()
