# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
import AthenaDocumentor.functions.markdown_string_manipulations as msm
from AthenaDocumentor.models.parsed_data import ParsedObject

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class MarkdownStructure:
    """
    The MarkdownStructure supports the `Parser` in formatting `ParsedObject` objects to the defined format.
    """
    indent:int = 4

    missing_documentation:str = "*<span style=color:red>-!- Missing documentation -!-</span>*"
    default_footer:str = "\n\n---\n\n"

    # ----------------------------------------------------------------------------------------------------------------------
    # - Formatting text snippets -
    # ----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def format_documentation(cls,parsed_object:ParsedObject) -> str:
        if parsed_object.doc is None or not parsed_object.doc:
            return cls.missing_documentation
        return msm.remove_empty_prefix(parsed_object.doc)

    @classmethod
    def format_type(cls, parsed_object:ParsedObject) -> str:
        return parsed_object.type.value
    @classmethod
    def format_module_name(cls, parsed_object:ParsedObject) -> str:
        return f"<small>{parsed_object.parent_module.__name__}.</small>"
    @classmethod
    def format_object_name(cls, parsed_object:ParsedObject) -> str:
        return f"**{parsed_object.name}**"
    @classmethod
    def format_signature(cls, parsed_object:ParsedObject) -> str:
        return str(parsed_object.signature).replace("'", "")

    @classmethod
    def format_header(cls, parsed_object: ParsedObject) -> str:
        type_:str = cls.format_type(parsed_object)
        module_name:str = cls.format_module_name(parsed_object)
        object_name:str = cls.format_object_name(parsed_object)
        signature:str = cls.format_signature(parsed_object)
        return f"{type_} {module_name}{object_name}{signature}"

    @classmethod
    def format_footer(cls, parsed_object: ParsedObject) -> str:
        return cls.default_footer

    # ----------------------------------------------------------------------------------------------------------------------
    # - Full structures -
    # ----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def structure_function(cls, parsed_object:ParsedObject) -> str:
        header = cls.format_header(parsed_object)
        footer = cls.format_footer(parsed_object)
        return f"{header}\n\n{cls.format_documentation(parsed_object)}{footer}"

    @classmethod
    def structure_class(cls,parsed_object: ParsedObject) -> str:
        header = cls.format_header(parsed_object)
        methods:str = msm.remove_empty_prefix(
            "\n\n".join(
                cls.structure_method(method)
                for method in parsed_object.methods
            )
        )
        footer = cls.format_footer(parsed_object)
        return f"{header}\n\n{cls.format_documentation(parsed_object)}\n\n{methods[:-4]}{footer}"

    @classmethod
    def structure_method(cls, parsed_object: ParsedObject) -> str:
        object_name:str = cls.format_object_name(parsed_object)
        signature:str = cls.format_signature(parsed_object)
        documentation = cls.format_documentation(parsed_object).replace("\n\n", "\n")
        return f'$\qquad${object_name}{signature}\n\n<span class="parent_indent">{documentation}</span>'