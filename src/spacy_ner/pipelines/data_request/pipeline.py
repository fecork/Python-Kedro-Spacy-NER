from kedro.config import ConfigLoader, MissingConfigException
from kedro.framework.project import settings

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import iterate_scripts


def load_parameters(**kwargs) -> dict:
    conf_loader = ConfigLoader(conf_source="conf", env="local")

    try:
        return conf_loader.get("parameters*", "parameters*/**", "**/parameters*")
    except MissingConfigException:
        print("No parameters found. Please check your configuration.")
        return settings.get("parameters", {})


def create_pipeline(**kwargs) -> Pipeline:
    parameters = load_parameters()
    dataset = parameters["dataset"]
    return pipeline(
        [
            node(
                func=iterate_scripts,
                inputs=[
                    "scripts_joined_{0}".format(dataset),
                    "scripts_questions_{0}".format(dataset),
                ],
                outputs="gpt_responses_{0}".format(dataset),
                name="create_pipeline_node",
            ),
        ],
    )
