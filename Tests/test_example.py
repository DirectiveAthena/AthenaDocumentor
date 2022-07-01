# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
import AthenaDocumentor.functions.parser

# Custom Packages
from Tests.support_code import Person, PERSON, random_function, RANDOM_FUNCTION, strange_object, STRANGE_OBJECT

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestDocumentor(unittest.TestCase):
    def test_person(self):
        self.assertEqual(
            PERSON,
            AthenaDocumentor.functions.parser.parse_single_object(Person).to_dict()
        )

    def test_random_function(self):
        self.assertEqual(
            RANDOM_FUNCTION,
            AthenaDocumentor.functions.parser.parse_single_object(random_function).to_dict()
        )

    def test_strange_object(self):
        with self.assertRaises(TypeError):
            AthenaDocumentor.functions.parser.parse_single_object(strange_object)

    def test_everything(self):
        print(AthenaDocumentor.functions.parser.parse(AthenaDocumentor, to_dict=True))