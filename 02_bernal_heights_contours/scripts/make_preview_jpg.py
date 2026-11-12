# Input: 300 dpi PNG exported from the QGIS layout "bernal_heights_contours_ansi_d" (not in the repo: too large).
# Output: 150 dpi JPG preview (5100 x 3300 px, quality 85) for the README.

from pathlib import Path
from PIL import Image

maps_folder = Path(__file__).parent.parent / "maps"
source = maps_folder / "bernal_heights_contours_ansi_d.png"
target = maps_folder / "bernal_heights_contours_ansi_d.jpg"

image = Image.open(source).convert("RGB")
image = image.resize((5100, 3300), Image.LANCZOS)
image.save(target, quality=85, optimize=True, dpi=(150, 150))
print(f"{target.name} {target.stat().st_size / 1000000:.1f} MB")
