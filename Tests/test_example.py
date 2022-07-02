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
class TestDocumentor(unittest.TestCase):
    def test_person(self):
        self.assertEqual(
            PERSON,
            AthenaDocumentor.models.parsed_data.ParsedObject(Person).to_dict()
        )

    def test_random_function(self):
        self.assertEqual(
            RANDOM_FUNCTION,
            AthenaDocumentor.models.parsed_data.ParsedObject(random_function).to_dict()
        )

    def test_strange_object(self):
        with self.assertRaises(TypeError):
            AthenaDocumentor.models.parsed_data.ParsedObject(strange_object)

    def test_output_json(self):
        (
            AthenaDocumentor.models.parser.Parser(root_module=AthenaDocumentor)
                .parse()
                .output_to_json_file(filepath="dump.json")
        )

    def test_output_markdown(self):
        (
            AthenaDocumentor.models.parser.Parser(root_module=AthenaDocumentor)
                .parse()
                .output_to_markdown_file(filepath="D:\Directive Athena\Programs\Veritas\Storage\Documentation\dump.md")
        )

    def test_output_support_code(self):
        self.assertEqual(
            ATHENADOCUMENTOR_MD,
            AthenaDocumentor.models.parser.Parser(root_module=AthenaDocumentor)
                .parse()
                .output_to_markdown_string()
        )