"""Renomea o recorte de EMODnet seguindo a convención zona_fonte_SRC.

Uso (desde a carpeta 01_vigo_ria):
    python3 scripts/renomear_raw.py
"""
from pathlib import Path

# Carpeta do proxecto = a carpeta pai da carpeta onde está este script
proxecto = Path(__file__).resolve().parent.parent
carpeta = proxecto / "data" / "raw"

vello = "vigo_ria_raw.tif"
novo = "vigo_ria_emodnet_4326.tif"

for sufixo in ["", ".aux.xml"]:
    orixe = carpeta / (vello + sufixo)
    destino = carpeta / (novo + sufixo)
    if orixe.exists():
        orixe.rename(destino)
        print(f"Renomeado: {orixe.name} -> {destino.name}")
    else:
        print(f"Non existe (nada que facer): {orixe.name}")
