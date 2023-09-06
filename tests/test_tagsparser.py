import unittest
from tagsparser import tag_to_arguments, tags_to_arguments

class Testtag_to_arguments(unittest.TestCase):
  def test_no_tag(self):
    self.assertEqual(tag_to_arguments(""),[])
  
  def test_simple_tag(self):
    self.assertEqual(tag_to_arguments("test"),["--test"])

  def test_simple_tag_with_assignment(self):
    self.assertEqual(tag_to_arguments("test=foo"),["--test=foo"])

  def test_tag_with_option_without_arguments(self):
    self.assertEqual(tag_to_arguments("test:"),["--test"])

  def test_tag_with_option_with_argument_with_assignment(self):
    self.assertEqual(tag_to_arguments("test:foo=bar"),["--test", "foo=bar"])

  def test_tag_with_option_with_list_arguments(self):
    self.assertEqual(tag_to_arguments("test:a,b,c"),["--test", "a", "--test", "b", "--test", "c"])

class Testtags_to_arguments(unittest.TestCase):
  def test_no_tag(self):
    self.assertEqual(tags_to_arguments([]),[])
  
  def test_simple_tag(self):
    self.assertEqual(tags_to_arguments(["test"]),["--test"])

  def test_two_simple_tags_and_tag_with_option_with_list_arguments(self):
    self.assertEqual(tags_to_arguments(["test0", "test1", "test2:a,b,c"]),["--test0", "--test1", "--test2", "a", "--test2", "b", "--test2", "c"])


if __name__ == '__main__':
  unittest.main()