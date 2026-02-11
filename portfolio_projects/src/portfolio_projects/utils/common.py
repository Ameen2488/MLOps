import os
from box.exceptions import BoxValueError
import yaml
import unittest
if not hasattr(unittest.TestCase, 'assertRaisesRegexp'):
    unittest.TestCase.assertRaisesRegexp = unittest.TestCase.assertRaisesRegex
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from portfolio_projects.logger import logger
import json
import joblib
import base64
import numpy as np
import cv2

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
        except FileExistsError:
            if os.path.isfile(path):
                os.remove(path)
                os.makedirs(path, exist_ok=True)
                if verbose:
                    logger.info(f"deleted existing file and created directory at: {path}")
            else:
                raise

@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        raise e

@ensure_annotations
def save_joblib(path: Path, data: Any):
    try:
        joblib.dump(data, path)
    except Exception as e:
        raise e

@ensure_annotations
def load_joblib(path: Path) -> Any:
    try:
        return joblib.load(path)
    except Exception as e:
        raise e

@ensure_annotations
def save_base64(path: Path, data: Any):
    try:
        with open(path, "wb") as file:
            file.write(base64.b64encode(data))
    except Exception as e:
        raise e

@ensure_annotations
def load_base64(path: Path) -> Any:
    try:
        with open(path, "rb") as file:
            return base64.b64decode(file.read())
    except Exception as e:
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"{size_in_kb} KB"
    except Exception as e:
        raise e    

def decode_image(image_path: Path) -> np.ndarray:
    try:
        with open(image_path, "rb") as file:
            image = base64.b64decode(file.read())
            image = np.frombuffer(image, dtype=np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            return image
    except Exception as e:
        raise e

def encode_image(image_path: Path) -> str:
    try:
        with open(image_path, "rb") as file:
            image = base64.b64encode(file.read())
            return image.decode("utf-8")
    except Exception as e:
        raise e


