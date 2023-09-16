from unittest import TestCase, main as unit_main
from unittest.mock import patch
from robotframework_tags_parameters.tagsparameters import TagsParameters, NoSchemaException

class Testconvert_tags_to_dict(TestCase):
  
  def setUp(self) -> None:
    self.schema = {
      "property": {
        "foo": {"type": "boolean"},
        "name": {"type": "string"},
        "reset": {"type":"boolean", "default": True, "false-prefix":"no"}
      }
    }
    return super().setUp()

  def no_schema(self):
    with self.assertRaises(NoSchemaException):
      TagsParameters().convert_tags_to_dict()

  def no_tags(self):
    self.assertEqual(TagsParameters(self.schema).convert_tags_to_dict(),{})

  @patch("robotframework_tags_parameters.tagsparameters.get_tags")
  def with_tags(self, mock_get_tags):
    mock_get_tags.return_values = ["foo", "name:test_name", "no-reset"]
    self.assertEqual(
      TagsParameters(self.schema).convert_tags_to_dict(),
      {"foo": True, "name": "test_name", "reset": False}
    )
    self.assertEqual(
      TagsParameters().convert_tags_to_dict(self.schema),
      {"foo": True, "name": "test_name", "reset": False}
    )

if __name__ == '__main__':
  unit_main()