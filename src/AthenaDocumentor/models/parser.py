# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import copy
import json
import inspect

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed_data import ParsedObject

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, eq=False)
class Parser:
    """
    Object to control the correct handling of parsing through a Python package

    Parameters:
        - root_module: Define the base package it must parse through
    """
    root_module:Any

    # non init
    parsed_items:dict[str:list[ParsedObject]]=field(init=False, default_factory=dict)
    handled_components:set=field(init=False, default_factory=set)

    def parse(self) -> Parser:
        """
        Main method of the Parser object.
        Running this will start the pared and populate the 'parsed_items' slot of the Parser object

        Returns:
            self : Done for chaining methods
        """
        self._parse_recursive(self.root_module)
        return self

    def _parse_recursive(self, module_to_parse:Any):
        for component in dir(module_to_parse): #type:str
            if component in self.handled_components:
                continue
            # store component string to skip the same name in the future
            self.handled_components.add(component)

            # skip special dunder components in a module
            if component.startswith("__"):
                continue

            # get that actual attribute object
            #   This is needed for the actual storage of component information
            if inspect.ismodule(attr := getattr(module_to_parse, component)):
                self._parse_recursive(attr)

            elif inspect.isclass(attr) or inspect.isfunction(attr) or inspect.ismethod(attr):
                if not (parsed_attr := ParsedObject(attr)).module_name.startswith(self.root_module.__name__):
                    continue
                # make sure the module name is in the dictionary else it will fail
                elif parsed_attr.module_name not in self.parsed_items:
                    self.parsed_items[parsed_attr.module_name] = []
                self.parsed_items[parsed_attr.module_name].append(parsed_attr)


    def output_to_dict(self, *, flat:bool=False) -> dict[str:list[dict]]:
        """
        Output the 'parsed_items' dictionary as is, or with custom parameters.

        Parameters:
            - flat: Outputs the dictionary in base types only (string, integers, booleans, etc...)

        Returns:
            dict
        """
        if not flat:
            return copy.deepcopy(self.parsed_items)
        # else:
        return {
            k: [v_.to_dict() for v_ in v]
            for k,v in self.parsed_items.items()
        }

    def output_to_json_file(self, filepath:str):
        """
        Output the 'parsed_items' dictionary to a json file.
        This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`

        Parameters:
            - filepath: Defines the output file location
        """
        with open(filepath, "w+") as file:
            file.write(
                json.dumps(
                    self.output_to_dict(flat=True),
                    indent=4
                )
            )
