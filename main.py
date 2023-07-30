from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.logging import  logger

STAGE_NAME = "data ingestion"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    raise ex


STAGE_NAME = "data validation"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    data_ingestion = DataValidationPipeline()
    data_ingestion.main()
except Exception as ex:
    raise ex


STAGE_NAME = "data transformation"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    data_ingestion = DataTransformationPipeline()
    data_ingestion.main()
except Exception as ex:
    raise ex
