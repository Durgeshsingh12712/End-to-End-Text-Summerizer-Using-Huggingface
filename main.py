import sys
from textSummerizer.logging import logger
from textSummerizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from textSummerizer.exception.exception import ConfigurationError

STAGE_NAME = "Data Ingestion Stage: 1"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e