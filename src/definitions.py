from pathlib import Path
import os

# Definition du chemin root du repo
REPO_ROOT = Path(os.getcwd()).resolve().parent

# Definition des chemins d'accès utiles
DATA_PATH = REPO_ROOT / "data"
RAW_DATA_PATH = DATA_PATH / "raw"
CLEAN_DATA_PATH = DATA_PATH / "clean"
CHROMEDRIVER_PATH = REPO_ROOT / "chromedriver" / "chromedriver"
MODEL_PATH = REPO_ROOT / "models"

# Definition des points de ravitaillement
RAVITAILLEMENTS = [
    {
        "nom": "SAINT-CHRISTO-EN-JAREZ",
        "distance": 20_000,
    },
    {
        "nom": "SAINTE-CATHERINE",
        "distance": 33_000,
    },
    {
        "nom": "SAINT-GENOU",
        "distance": 48_000,
    },
    {
        "nom": "SOUCIEU-EN-JARREST",
        "distance": 61_000,
    },
    {
        "nom": "CHAPONOST",
        "distance": 68_000,
    },
]