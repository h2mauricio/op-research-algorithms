#get path of current notebook
from pathlib import Path
from loguru import logger

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
SOLVER = "gurobi"

logger.info(f"ROOT_DIR: {ROOT_DIR}")
logger.info(f"DATA_DIR: {DATA_DIR}")