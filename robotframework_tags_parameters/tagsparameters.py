"""
Robotframework Keyword for convert tags to dict
"""
from typing import Dict, List
from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn
from argparse_from_jsonschema import get_parser

from robotframework_tags_parameters.tagsparser import tags_to_arguments

def get_tags() -> List[str]:
    """Get Tags of current test

    Returns:
        List[str]: List of Tags ["tag1", "tag2"]
    """
    print(BuiltIn().get_variables())
    return BuiltIn().get_variables().get('@{TEST_TAGS}')

class NoSchemaException(Exception):
    """ Exception raise when no json schema is specify
    """

@library(scope='GLOBAL')
class TagsParameters: # pylint: disable=too-few-public-methods
    """
    Robotframework library
    """
    def __init__(self, json_schema_path:str=None) -> None:
        self.json_schema_path = None
        self.use_json_schema_path(json_schema_path)

    @keyword
    def use_json_schema_path(self, json_schema_path:str=None) -> None:
        """
        Select json schema path
        """
        self.json_schema_path = json_schema_path

    @keyword
    def convert_tags_to_dict(self, json_schema:str=None) -> Dict:
        """Convert Test Tags to Dict
        Use json schema for specify tags to convert.

        Args:
            json_schema (str, optional): \
                Json schema specify tags to convert. Defaults to None.

        Returns:
            Dict: Value parse from tags
        """
        schema = None
        args = None
        if self.json_schema_path:
            schema = self.json_schema_path
        if json_schema:
            schema = json_schema
        if not schema:
            raise NoSchemaException()
        print(schema)
        args = get_parser(schema)
        print(args)
        print(get_tags())
        print(tags_to_arguments(get_tags()))
        return vars(
            args.parse_known_args(
                tags_to_arguments(get_tags())
            )[0]
        )
