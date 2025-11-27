from dataclasses import dataclass, field

import datetime
from typing import List
import os
import json


def load_dataset_ids():
    json_path = os.path.join(os.path.dirname(__file__), 'dataset_ids.json')
    with open(json_path, 'r') as f:
        return json.load(f)

@dataclass
class Config:
    
    date_min: datetime.date = field(default_factory=lambda: datetime.date(2025, 10, 1))
    date_max: datetime.date = field(default_factory=lambda: datetime.date(2025, 10, 31))
    
    
    dataset_ids: List = field(default_factory=load_dataset_ids)
    

config = Config()