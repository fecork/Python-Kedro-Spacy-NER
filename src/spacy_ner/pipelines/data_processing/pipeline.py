from kedro.config import ConfigLoader, MissingConfigException
from kedro.framework.project import settings

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import iterate_text_list, join_text_rules_question


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
                func=iterate_text_list,
                inputs="scripts_content_{0}".format(dataset),
                outputs="scripts_content_{0}_clean".format(dataset),
                name="format_text_node",
            ),
            node(
                func=join_text_rules_question,
                inputs=[
                    "scripts_content_{0}_clean".format(dataset),
                    "scripts_questions_{0}".format(dataset),
                    "scripts_content_information_{0}".format(dataset),
                    "scripts_structure_answer_{0}".format(dataset),
                ],
                outputs="scripts_joined_{0}".format(dataset),
                name="join_text_node",
            ),
        ],
    )
