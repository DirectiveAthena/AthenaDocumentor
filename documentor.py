# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaDocumentor

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    parser = AthenaDocumentor.Parser(root_module=AthenaDocumentor).parse()
    # output the entire AthenaDocumentor to JSON
    parser.output_to_json_file("exports/dump.json")
    # output the entire package to the Obsidian documentation
    parser.output_to_markdown_file(
        r"exports\dump.md",
        r"D:\Directive Athena\Programs\Veritas\Storage\Documentation\Content\Programming\AthenaDocumentor\reference.md"
    )

if __name__ == '__main__':
    main()