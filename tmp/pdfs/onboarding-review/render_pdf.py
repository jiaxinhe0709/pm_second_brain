from pathlib import Path
import sys

import fitz


if len(sys.argv) != 3:
    raise SystemExit("usage: render_pdf.py <input.pdf> <output-prefix>")

input_path = Path(sys.argv[1])
output_prefix = Path(sys.argv[2])
document = fitz.open(input_path)
text_sections: list[str] = []

for index, page in enumerate(document):
    text_sections.append(f"\n\n===== PAGE {index + 1} =====\n\n{page.get_text('text')}")
    pixmap = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
    pixmap.save(f"{output_prefix}-{index + 1:03d}.png")

Path(f"{output_prefix}.txt").write_text("".join(text_sections), encoding="utf-8")
print(f"pages={document.page_count} prefix={output_prefix}")
