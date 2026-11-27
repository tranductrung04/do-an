from pathlib import Path
from tempfile import NamedTemporaryFile

from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Group, String
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from svglib.svglib import svg2rlg

BASE = Path(__file__).resolve().parent / "figures"
FONT_NAME = "ArialUnicode"
FONT_CANDIDATES = [
    Path("C:/Windows/Fonts/arial.ttf"),
    Path("C:/Windows/Fonts/DejaVuSans.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
]

FIGURES = [
    "chapter1_monolithic_architecture",
    "chapter1_ecommerce_monolith",
    "chapter1_microservices_architecture",
    "chapter1_monolith_vs_microservices",
    "chapter1_ddd_flow",
    "chapter1_aggregate_example",
    "chapter1_context_map_ecommerce",
    "chapter1_healthcare_decomposition",
    "chapter1_service_relationships",
]


def register_unicode_font() -> None:
    for font_path in FONT_CANDIDATES:
        if font_path.exists():
            pdfmetrics.registerFont(TTFont(FONT_NAME, str(font_path)))
            return

    raise RuntimeError("Cannot find a TrueType font with Vietnamese glyphs")


def prepare_svg(svg_path: Path) -> str:
    svg = svg_path.read_text(encoding="utf-8")
    svg = svg.replace("@import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&amp;display=swap');", "")
    svg = svg.replace("text { font-family: 'Kalam', 'Comic Sans MS', cursive; }", f"text {{ font-family: '{FONT_NAME}'; }}")
    svg = svg.replace(
        '<marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6.5" refY="4" orient="auto">',
        '<marker id="arrowhead" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">',
    )
    svg = svg.replace(
        '<path d="M 0 1 L 6.5 4 L 0 7 Q 2.5 4 0 1" fill="#1e293b" />',
        '<path d="M 0 1 L 10 6 L 0 11 Z" fill="#1e293b" />',
    )
    return svg


def apply_unicode_font(node) -> None:
    if isinstance(node, String):
        node.fontName = FONT_NAME
        node._fontname = FONT_NAME

    if isinstance(node, Group):
        for child in node.contents:
            apply_unicode_font(child)


def convert_svg_to_pdf(name: str) -> None:
    svg_path = BASE / f"{name}.svg"
    pdf_path = BASE / f"{name}.pdf"

    with NamedTemporaryFile("w", encoding="utf-8", suffix=".svg", delete=False) as temp_file:
        temp_file.write(prepare_svg(svg_path))
        temp_svg_path = Path(temp_file.name)

    try:
        drawing = svg2rlg(str(temp_svg_path))
    finally:
        temp_svg_path.unlink(missing_ok=True)

    if drawing is None:
        raise RuntimeError(f"Cannot convert {svg_path}")

    apply_unicode_font(drawing)
    renderPDF.drawToFile(drawing, str(pdf_path))
    print(f"{svg_path.name} -> {pdf_path.name}")


def main() -> None:
    register_unicode_font()
    for figure in FIGURES:
        convert_svg_to_pdf(figure)


if __name__ == "__main__":
    main()