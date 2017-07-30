import types
import unittest

from item_reader import file_line_stream


class ItemReaderTest(unittest.TestCase):

    def test_reading_line_by_line(self):
        lines = file_line_stream(file_path="./customers.json")
        self.assertTrue(isinstance(lines, types.GeneratorType))
        lines = list(lines)
        self.assertEqual(len(lines), 4)