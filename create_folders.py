
from pathlib import Path

project = "02_bernal_heights_contours"
base = Path(__file__).parent / project
print(base)

# Creamos un novo directorio con mkdir que está na ruta que garda "base"
# Neste caso, a carpeta que garda a variable project
base.mkdir(parents=True, exist_ok=True)
subfolders = ["data/raw", "data/processed", "maps", "project", "scripts"]
print(subfolders)

# Unha vez creados os nomes das carpetas, creámolas
print("-" *50)
for folder in subfolders:
    (base/folder).mkdir(parents=True, exist_ok=True)
    if (base/folder).exists():
        print(f"✅ {folder}")
    else:
        print(f"❌ {folder}")
print("-" * 50)
