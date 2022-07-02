# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
import AthenaDocumentor.models.parser
import AthenaDocumentor.models.parsed.parsed_class
import AthenaDocumentor.models.parsed.parsed_function

# Custom Packages
from Tests.support_code import Person, PERSON, random_function, RANDOM_FUNCTION, strange_object

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestParsedData(unittest.TestCase):
    def test_person(self):
        self.assertEqual(
            PERSON,
            AthenaDocumentor.models.parsed.parsed_class.ParsedClass(Person).to_dict()
        )

    def test_random_function(self):
        self.assertEqual(
            RANDOM_FUNCTION,
            AthenaDocumentor.models.parsed.parsed_function.ParsedFunction(random_function).to_dict()
        )