import pandas as pd
import numpy as np

from pathlib import Path
import datetime
import re
import glob
import os
import json
import logging
from tqdm import tqdm

from config import config

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

# Create formatters - simple and clean format
simple_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# File handler without rotation - single file only
file_handler = logging.FileHandler(
    'db_sync.log',
    mode='a',  # append mode
    encoding='utf-8'
)
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(simple_formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(simple_formatter)

# Add handlers to logger
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def read_file_simem(file_path):
    filename = Path(file_path).name
    try:
        df=pd.read_json(file_path)
        
        return df
    except Exception as e:
        logger.error(f"❌ Error en empresas: {Path(file_path).name}: {str(e)}")

        raise
def filter_json_file_paths(dataset_id):
    logger.debug(f"Entering filter_json_file_paths for dataset_id: {dataset_id}")
    file_paths = []
    try:
        glob_pattern = f"data/simem/{dataset_id}/*.json"
        found_files = glob.glob(glob_pattern)
        file_paths.extend(found_files)
        file_paths.sort()
        logger.info(f"Found {len(file_paths)} JSON files for dataset_id '{dataset_id}'.")
        logger.debug(f"Sorted file paths: {file_paths}")
    except Exception as e:
        logger.error(f"Error filtering JSON file paths for dataset_id '{dataset_id}': {e}")
        raise
    logger.debug(f"Exiting filter_json_file_paths for dataset_id: {dataset_id}")
    return file_paths

def create_file(dataset_id):
    file_paths = filter_json_file_paths(dataset_id)
    if file_paths:
        df = pd.concat([read_file_simem(file_path) for file_path in tqdm(file_paths, desc=f"Procesando archivos {dataset_id}")])
        file_name = f"tmp/{dataset_id}.csv"
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        df.to_csv(file_name, index=False)


def create_files():
    for dataset_id in config.dataset_ids:
        create_file(dataset_id)

if __name__ == "__main__":
    create_files()
