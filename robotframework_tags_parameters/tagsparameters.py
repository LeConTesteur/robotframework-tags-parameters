"""
Robotframework Keyword for convert tags to dict
"""
from typing import Dict, List
import json
from robot.api.deco import library
from robot.libraries.BuiltIn import BuiltIn
from argparse_from_jsonschema import get_parser

def get_tags() -> List[str]:
    """Get Tags of current test

    Returns:
        List[str]: List of Tags ["tag1", "tag2"]
    """
    return BuiltIn().get_variables().value('${TAGS_NAME}')

class NoSchemaException(Exception):
    """ Exception raise when no json schema is specify
    """

@library(scope='GLOBAL')
class TagsParameters: # pylint: disable=too-few-public-methods
    """
    Robotframework library
    """
    def __init__(self, tags_descriptor_path=None) -> None:
        self.tags_descriptor_path = tags_descriptor_path


    def convert_tags_to_dict(self, tags_descriptor_path:str=None) -> Dict:
        """Convert Test Tags to Dict
        Use json schema for specify tags to convert.

        Args:
            tags_descriptor_path (str, optional): \
                Json schema specify tags to convert. Defaults to None.

        Returns:
            Dict: Value parse from tags
        """
        if tags_descriptor_path:
            self.tags_descriptor_path = tags_descriptor_path
        if self.tags_descriptor_path is None:
            raise NoSchemaException()
        schema = json.load(self.tags_descriptor_path)
        args = get_parser(schema)
        return args.parse_known_args(get_tags())
