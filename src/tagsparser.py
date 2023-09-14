"""
Transform tag to argument
"""
from typing import List

DEFAULT_CONTEXT_SYMBOL = ':'
DEFAULT_LIST_SEPARATOR = ','


def format_option(option: str) -> str:
    """
    Format option
    """
    return f'--{option}'


def tag_to_arguments(tag: str) -> List[str]:
    """
    Transform tag to a list of argument
    """
    if not tag:
        return []

    if DEFAULT_CONTEXT_SYMBOL not in tag:
        return [format_option(tag)]

    option, arguments = tag.split(DEFAULT_CONTEXT_SYMBOL)
    if not arguments:
        return [format_option(option)]
    return [
        x for args in arguments.split(DEFAULT_LIST_SEPARATOR) for x in [format_option(option), args]
    ]


def tags_to_arguments(tags: List[str]) -> List[str]:
    """
    Transform list of tag to list argument
    """
    return [
        x for tag in tags for x in tag_to_arguments(tag)
    ]
