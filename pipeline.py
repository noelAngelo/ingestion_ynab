import dlt
from loguru import logger
from sources.api.upbank.source import upbank

upbank_pipeline = dlt.pipeline(
    pipeline_name="upbank",
    destination="postgres",
    dataset_name="upbank_data",
)

upbank_load_info = upbank_pipeline.run(upbank())
logger.info(upbank_load_info)
