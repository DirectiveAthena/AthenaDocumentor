# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed.parsed import Parsed
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(init=False, eq=False)
class ParsedModule(Parsed):
    """
    A dataclass for storage of module object components.
    Does not hold the documentation by itself, as this can often lead to memory overloads with large documentation strings

    Parameters:
    - obj: the module in question which must be stored
    - parent_module: the module where the class in located in. This is a `types.ModuleType`
    """
    @property
    def type(self):
        return Types.module