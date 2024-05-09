import os, sys
import shutil
from EmergencyDetection.logger import logging
from EmergencyDetection.exception import AppException
from EmergencyDetection.entity.config_entity import DataValidationConfig
from EmergencyDetection.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact)



class DataValidation:
    def __init__(self,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config


        except Exception as e:
            raise AppException(e, sys)
        
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            logging.info(f"Entered the validation_all_files_exist method of DataValidation class all files exist: {all_files}")

            for file in all_files:
                logging.info(f"Entered the for loop validation_all_files_exist method of DataValidation class all files exist: {all_files} for file: {file}")
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, "w") as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, "w") as f:
                        f.write(f"Validation status: {validation_status}")
        
            return validation_status

        except Exception as e:
            raise AppException(e, sys)
        

    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                directory = "foo"
                path = os.path.join(os.getcwd(), directory)    
                os.mkdir(path)
                shutil.copytree(self.data_ingestion_artifact.data_zip_file_path, path, dirs_exist_ok=True)

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)