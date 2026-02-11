from src.portfolio_projects.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.portfolio_projects.logger import logger

STAGE_NAME = "Data Ingestion"

if __name__ == '__main__':
    try:
        logger.info(f"\n\n-------------------------Stage {STAGE_NAME} started-------------------------\n\n")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f"\n\n-------------------------Stage {STAGE_NAME} completed-------------------------\n\n")
    except Exception as e:
        logger.error(e)
        raise e
