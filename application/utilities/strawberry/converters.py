from strawberry.schema.name_converter import NameConverter


class PythonConverter(NameConverter):
    """
    This converter handles the python conversion of when we have reserved words
    we add an underscore in the end of the name Ex: input_
    """

    def apply_naming_config(self, name: str) -> str:
        if name.endswith("_"):
            name = name[:-1]
        return super().apply_naming_config(name)
