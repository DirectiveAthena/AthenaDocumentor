# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
import AthenaDocumentor.models.parser
import AthenaDocumentor.models.parsed_data

# Custom Packages
from Tests.support_code import Person, PERSON, random_function, RANDOM_FUNCTION, strange_object, ATHENADOCUMENTOR_MD
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestParser(unittest.TestCase):
    def test_output_markdown(self):
        with open("../exports/dump.md", "r") as file:
            self.assertEqual(
                file.read(),
                AthenaDocumentor.models.parser.Parser(root_module=AthenaDocumentor)
                    .parse()
                    .output_to_markdown_string()
            )
    def test_output_json(self):
        with open("../exports/dump.json", "r") as file:
            self.assertEqual(
                file.read(),
                AthenaDocumentor.models.parser.Parser(root_module=AthenaDocumentor)
                    .parse()
                    .output_to_json_string()
            )