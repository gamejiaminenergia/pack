import pandas as pd
import json

from pathlib import Path
import datetime
import glob
import os

from tqdm import tqdm




def check_json_files():
    file_paths = glob.glob('data/simem/*/*')
    error_file_paths = []

    print(f"Total files: {len(file_paths)}")

    for file_path in tqdm(file_paths, desc="Checking files", unit="file", colour="green"):
        try:
            with open(file_path, 'r') as file:
                json.load(file)
        except json.JSONDecodeError:
            error_file_paths.append(file_path)

    print(f"Files with errors: {len(error_file_paths)}")

    for file_path in tqdm(error_file_paths, desc="Error files", unit="file", colour="red"):
        os.remove(file_path)

if __name__ == "__main__":
    check_json_files()