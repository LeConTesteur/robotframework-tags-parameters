import unittest
from unittest.mock import patch
from jsonschema import ValidationError
from robotframework_tags_parameters.tagsparameters import TagsParameters, NoSchemaException

class Testconvert_tags_to_dict(unittest.TestCase):
  
  def setUp(self) -> None:
    self.schema = {
      "type": "object",
      "properties": {
        "foo": {"type": "boolean"},
        "name": {"anyOf": [{"type": "string"},{"type":"null"}]},
        "reset": {"type":"boolean", "default": True, "false-prefix":"no"},
        "number_default": {"type": "integer", "default":"0"},
      }
    }
    return super().setUp()

  def test_no_schema(self):
    with self.assertRaises(NoSchemaException):
      TagsParameters().convert_tags_to_dict()

  @patch("robotframework_tags_parameters.tagsparameters.get_tags")
  def test_no_tags(self, mock_get_tags):
    mock_get_tags.return_value = []
    self.assertEqual(TagsParameters(self.schema).convert_tags_to_dict(),
                     {"foo": False, "name":None,"reset": True, "number_default":0})

  @patch("robotframework_tags_parameters.tagsparameters.get_tags")
  def test_with_tags(self, mock_get_tags):
    mock_get_tags.return_value = ["foo", "name:test_name", "no-reset","number_default:5"]
    self.assertEqual(
      TagsParameters(self.schema).convert_tags_to_dict(),
      {"foo": True, "name": "test_name", "reset": False, "number_default":5}
    )
    self.assertEqual(
      TagsParameters().convert_tags_to_dict(self.schema),
      {"foo": True, "name": "test_name", "reset": False, "number_default":5}
    )

  @patch("robotframework_tags_parameters.tagsparameters.get_tags")
  def test_string_with_maxlength(self, mock_get_tags):
    schema = {
      "type": "object",
      "properties": {
        "name": {"type": "string", "default": "foo", "maxLength":3},
      }
    }
    mock_get_tags.return_value = []
    self.assertEqual(
      TagsParameters(schema).convert_tags_to_dict(),
      {"name": "foo"}
    )
    mock_get_tags.return_value = ['name:BAR']
    self.assertEqual(
      TagsParameters(schema).convert_tags_to_dict(),
      {"name": "BAR"}
    )
    mock_get_tags.return_value = ['name:BAAR']
    with self.assertRaises(ValidationError):
      TagsParameters(schema).convert_tags_to_dict(),





if __name__ == '__main__':
  unittest.main()