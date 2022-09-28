import logging
from kedro.config import ConfigLoader, MissingConfigException
from typing import Dict

import spacy


def load_model():
    """
    Funtion for load parameters spacy model.
    """

    try:
        nlp_ner = spacy.load("data/06_models/model-best")
        return nlp_ner
    except MissingConfigException:
        logging.warning("No hay Modelo")


def _ask_openai(text: str) -> str:
    """
    This is a function for  ask question to GPT API by OpenAI.
    """

    nlp_ner = load_model()
    doc = nlp_ner(text)

    logging.warning(doc)

    colors = {
        "CANCELLATION_TIME": "#F67DE3",
        "CHARGE_CANCEL": "#7DF6D9",
        "CHARGE_NOSHOW": "#FFFFFF",
    }

    options = {"colors": colors}

    # doc.to_dict()

    # spacy.displacy.render(doc, style="ent", options=options, jupyter=True)
    doc_dict = doc.to_dict()
    response = doc.ents
    print(response)
    return str(response)


def iterate_scripts(dataset: dict, question: str) -> Dict:
    """Iterate over the list of text.

    Args:
        dataset: Dict of text.
    """

    list_format_text = []
    id_file = []

    for partition_id, partition_load_func in dataset.items():
        text = partition_load_func()
        gpt_res = _ask_openai(text)

        tag = ""
        list_format_text.append(tag + gpt_res)
        id_file.append(partition_id)

    res = dict(zip(id_file, list_format_text))
    return res
