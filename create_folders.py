
from pathlib import Path
print(Path.home())
base = Path(__file__).parent / "01_vigo_ria"
print(base)

# Creamos un novo directorio con mkdir que está na ruta que garda "base"
# Neste caso será un directorio chamado "01_vigo_ria"
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