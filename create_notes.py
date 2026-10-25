from pathlib import Path

base = Path(__file__).parent
folder = base / "notes"
folder.mkdir(exist_ok=True)
print(folder.exists())