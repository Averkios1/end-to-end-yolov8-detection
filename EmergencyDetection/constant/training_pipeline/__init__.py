from roboflow import Roboflow

ARTIFACTS_DIR: str = "artifacts"

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

#DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1ECfl3dtYyfivY8kYPq7RHUBTjC-2vf61/view?usp=share_link"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1JWSKGaCTFch4bGpO0xTpHZG4v8LhL3Uk/view?usp=sharing"

'''
rf = Roboflow(api_key="H5PkFgOqeCO4gbl7EHeb")
DATA_DOWNLOAD_URL = rf.workspace("vasalosi-gmail-com").project("forest-detection-9k2e4")
version = DATA_DOWNLOAD_URL.version(1)
dataset = version.download("yolov8")
'''



"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "data.yaml"]



"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16