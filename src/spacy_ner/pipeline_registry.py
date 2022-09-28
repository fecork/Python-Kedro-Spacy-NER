"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from spacy_ner.pipelines import data_processing as dp
from spacy_ner.pipelines import data_request as dr


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_request_pipeline = dr.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_request_pipeline,
        "dp": data_processing_pipeline,
        "dr": data_request_pipeline,
    }
