from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.evaluation_pipeline import EvaluationPipeline
from src.textSummarizer.logging import logger

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
    data_validate = DataValidationPipeline()
    data_validate.main()
except Exception as ex:
    raise ex


STAGE_NAME = "data transformation"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    data_transformer = DataTransformationPipeline()
    data_transformer.main()
except Exception as ex:
    raise ex


STAGE_NAME = "model trainer"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
except Exception as ex:
    raise ex

STAGE_NAME = "model evaluation"

try:
    logger.info(f"starting {STAGE_NAME} ------> ")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
except Exception as ex:
    raise ex


