import os, sys
import yaml
from EmergencyDetection.utils.main_utils import read_yaml_file
from EmergencyDetection.logger import logging
from EmergencyDetection.exception import AppException
from EmergencyDetection.entity.config_entity import ModelTrainerConfig
from EmergencyDetection.entity.artifacts_entity import ModelTrainerArtifact
from EmergencyDetection.entity.config_entity import DataIngestionConfig
from EmergencyDetection.entity.artifacts_entity import DataIngestionArtifact
from ultralytics import YOLO

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config
      
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            #logging.info("Unzipping data")
            #os.system("unzip data.zip")
            #os.system("rm data.zip")

            #with open("data.yaml", 'r') as stream:
            #    num_classes = str(yaml.safe_load(stream)['nc'])

            #model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            #print(model_config_file_name)

            #config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            #config['nc'] = int(num_classes)


            #with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
            #    yaml.dump(config, f)


            #os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            logging.info(f"Current working directory is {os.getcwd()}")
            logging.info(f"Current working directory is {self.model_trainer_config.model_trainer_dir}")
            os.system(f"yolo task=detect mode=train model={self.model_trainer_config.weight_name} data=data.yaml imgsz=640 epochs={self.model_trainer_config.no_epochs} plots=True")
            os.system(f"cp runs/detect/train/weights/best.pt {os.getcwd()}")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp runs/detect/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}")
           
            os.system("rm -rf runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf valid")
            os.system("rm -rf data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path= self.model_trainer_config.model_trainer_dir,
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise AppException(e, sys)