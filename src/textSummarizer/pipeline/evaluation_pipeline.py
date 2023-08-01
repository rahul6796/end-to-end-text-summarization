
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_evaluation import ModelEvaluation


class EvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = ModelEvaluation(config=config)
        model_evaluation_config.evaluate()