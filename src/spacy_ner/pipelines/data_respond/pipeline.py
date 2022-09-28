"""
This is a boilerplate pipeline 'data_respond'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import iterate_paragraphs


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=iterate_paragraphs,
                inputs="gpt_responses_ticket_2",
                outputs="json_response",
                name="data_respond_nodes",
            )
        ]
    )
