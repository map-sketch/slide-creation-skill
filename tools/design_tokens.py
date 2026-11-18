"""
Executive Consulting Visual Design Tokens
Shared constants module for PowerPoint presentation generation via python-pptx.
"""

from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# ---------------------------------------------------------------------------
# Hex Color Constants
# ---------------------------------------------------------------------------
PRIMARY_BLACK_HEX = "#000000"
CANVAS_WHITE_HEX = "#FFFFFF"
ACCENT_GREEN_HEX = "#86BC25"
DELOITTE_GREEN_HEX = ACCENT_GREEN_HEX  # Alias for backward compatibility
MID_GREEN_HEX = "#26890D"
COOL_GRAY_11_HEX = "#53565A"
COOL_GRAY_2_HEX = "#D0D0CE"
TINT_HEX = "#F5F6F7"
CHART_TEAL_HEX = "#0097A9"
CHART_BLUE_HEX = "#0076A8"


def hex_to_rgbcolor(hex_str: str) -> RGBColor:
    """Convert hex string (e.g. '#86BC25' or '86BC25') to pptx.dml.color.RGBColor."""
    clean_hex = hex_str.lstrip("#")
    if len(clean_hex) != 6:
        raise ValueError(f"Invalid hex color string: {hex_str}")
    r = int(clean_hex[0:2], 16)
    g = int(clean_hex[2:4], 16)
    b = int(clean_hex[4:6], 16)
    return RGBColor(r, g, b)


# ---------------------------------------------------------------------------
# RGBColor Object Constants
# ---------------------------------------------------------------------------
PRIMARY_BLACK = RGBColor(0x00, 0x00, 0x00)
CANVAS_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT_GREEN = RGBColor(0x86, 0xBC, 0x25)
DELOITTE_GREEN = ACCENT_GREEN  # Alias for backward compatibility
MID_GREEN = RGBColor(0x26, 0x89, 0x0D)
COOL_GRAY_11 = RGBColor(0x53, 0x56, 0x5A)
COOL_GRAY_2 = RGBColor(0xD0, 0xD0, 0xCE)
TINT = RGBColor(0xF5, 0xF6, 0xF7)
CHART_TEAL = RGBColor(0x00, 0x97, 0xA9)
CHART_BLUE = RGBColor(0x00, 0x76, 0xA8)

# Severity Accent Colors for Risk / Status Callouts
STATUS_RED = RGBColor(0xDA, 0x29, 0x1C)
STATUS_AMBER = RGBColor(0xED, 0x8B, 0x00)
STATUS_GREEN = RGBColor(0x26, 0x89, 0x0D)

# ---------------------------------------------------------------------------
# Typography Constants
# ---------------------------------------------------------------------------
FONT_PRIMARY = "Aptos"
FONT_FALLBACK = "Calibri"
FONT_SAFE = "Open Sans"

TITLE_SIZE = Pt(28)
ACTION_TITLE_SIZE = Pt(22)
SUBTITLE_SIZE = Pt(12)
SECTION_HEADING_SIZE = Pt(14)
BODY_SIZE = Pt(11)
BODY_SMALL_SIZE = Pt(10)
FOOTER_SIZE = Pt(8.5)
KPI_SIZE = Pt(36)
KPI_LABEL_SIZE = Pt(10)

# ---------------------------------------------------------------------------
# Slide Canvas & Grid Dimensions (16:9 Widescreen)
# ---------------------------------------------------------------------------
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

MARGIN_LEFT = Inches(0.5)
MARGIN_RIGHT = Inches(0.5)
MARGIN_TOP = Inches(0.9)
MARGIN_BOTTOM = Inches(0.5)

CONTENT_WIDTH = Inches(12.333)   # 13.333 - 1.0
CONTENT_HEIGHT = Inches(6.1)     # 7.5 - 1.4

FOOTER_TOP = Inches(6.9)
FOOTER_HEIGHT = Inches(0.35)
