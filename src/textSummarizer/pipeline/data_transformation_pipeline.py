
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation


class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()


