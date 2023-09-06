from typing import Any, List

DEFAULT_CONTEXT_SYMBOL = ':'
DEFAULT_LIST_SEPARATOR = ','


def format_option(option):
    return '--{}'.format(option)


def tag_to_arguments(tag: str) -> List[str]:
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
    return [
        x for tag in tags for x in tag_to_arguments(tag)
    ]
