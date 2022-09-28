import re
from typing import Dict


def _format_text(text: str) -> str:
    """Preprocesses the data text, clean it.

    Args:
        text: String Raw data.
    Returns:
        Preprocessed data text, without stranger character.
    """

    text = text.replace(str("\\n"), "\n")
    text = text.replace(str("/"), " ")
    text = re.sub(r"[^a-zA-Z0-9\s\n.,;]", "", text)
    return text


def iterate_text_list(dataset: dict) -> Dict:
    """Iterate over the list of text.

    Args:
        dataset: Dict  of text.
    """

    list_format_text = []
    id_file = []

    for partition_id, partition_load_func in dataset.items():
        text = partition_load_func()
        list_format_text.append(_format_text(text))
        id_file.append(partition_id)

    res = dict(zip(id_file, list_format_text))
    return res


def join_text_rules_question(dataset: dict) -> Dict:
    """Join the text of the article and the questions.
    Args:
        dataset: Dict with the text data with differents examples.
        questions: String questions list.
    Returns:
        Join the text of the article and the questions.
    """
    list_joined_text = []
    id_file = []

    for partition_id, partition_load_func in dataset.items():
        rules = partition_load_func()
        list_joined_text.append(rules)
        id_file.append(partition_id)

    res = dict(zip(id_file, list_joined_text))
    return res
