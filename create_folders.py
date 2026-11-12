from pathlib import Path

project = "02_bernal_heights_contours"
base = Path(__file__).parent / project
print(base)

# Create the project folder inside gis_portfolio.
# Change the value of project above for each new project.
base.mkdir(parents=True, exist_ok=True)
subfolders = ["data/raw", "data/processed", "deliverables", "maps", "project", "scripts"]
print(subfolders)

# Create each subfolder and confirm that it exists.
print("-" * 50)
for folder in subfolders:
    (base/folder).mkdir(parents=True, exist_ok=True)
    if (base/folder).exists():
        print(f"✅ {folder}")
    else:
        print(f"❌ {folder}")
print("-" * 50)
