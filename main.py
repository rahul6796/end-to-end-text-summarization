from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline
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
