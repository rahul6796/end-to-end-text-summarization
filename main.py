from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.logging import  logger

STAGE_NAME = "data ingestion"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as ex:
    raise ex

