import sys
from datetime import datetime
from typing import Literal

from brewtils import Plugin, command, parameter

__version__ = "3.0.0.dev0"


class ParametersClient(object):
    """Client that shows different options to declaring parameters"""

    @parameter(key="base64", type="Base64", description="Value For base64",)
    @parameter(key="bytes", type="Bytes", description="Value For bytes",)
    @parameter(key="date_time", type="DateTime", description="Value For date_time",)
    @parameter(key="date", type="Date", description="Value For date_time",)
    @parameter(key="dict", type="Dictionary", description="Value For dict",)
    @parameter(key="bool", type="Boolean", description="Value For bool",)
    @parameter(key="float", type="Float", description="Value For float",)
    @parameter(key="int", type="Integer", description="Value For int",)
    @parameter(key="str", type="String", description="Value For str",)
    @parameter(key="date_time_array", type="DateTime", multi=True, description="Value For date_time_array",)
    @parameter(key="date_array", type="Date", multi=True, description="Value For date_array",)
    @parameter(key="dict_array", type="Dictionary", multi=True, description="Value For dict_array",)
    @parameter(key="bool_array", type="Boolean", multi=True, description="Value For bool_array",)
    @parameter(key="float_array", type="Float", multi=True, description="Value For float_array",)
    @parameter(key="int_array", type="Integer", multi=True, description="Value For int_array",)
    @parameter(key="str_array", type="String", multi=True, description="Value For str_array",) 
    def kitchen_sink(self, base64, bytes, date_time, date, dict, bool, float, int, str, date_time_array, date_array, dict_array, bool_array, float_array, int_array, str_array):
        """Kitchen Sink: Any value"""
        return "done"

    @command()
    def any_default(self, value):
        """Any is the default type for any undeclared variables"""
        return value

    @parameter(key="value", type="String")
    def string_parameter(self, value):
        """Parameter: string value"""
        return value

    @command()
    def string_type_hint(self, value: str):
        """Type Hint: String value"""
        return value

    @command()
    def string_doc_string(self, value):
        """Doc String: String value
        Args:
            value (str): A value of String type
        """
        return value

    if sys.version_info.major == 3 and sys.version_info.minor >= 8:

        @command()
        def string_type_hint_choices(self, value: Literal["value1", "value2"]):
            """Type Hint: String value"""
            return value

    @parameter(key="value", type="Integer")
    def int_parameter(self, value):
        """Parameter: int value"""
        return value

    @command()
    def int_type_hint(self, value: int):
        """Type Hint: int value"""
        return value

    if sys.version_info.major == 3 and sys.version_info.minor >= 8:

        @command()
        def int_type_hint_choices(self, value: Literal[1, 2]):
            """Type Hint: String value"""
            return value

    @command()
    def int_doc_string(self, value):
        """Doc String: int value
        Args:
            value (int): A value of int type
        """
        return value

    @parameter(key="value", type="Float")
    def float_parameter(self, value):
        """Parameter: float value"""
        return value

    @command()
    def float_type_hint(self, value: float):
        """Type Hint: float value"""
        return value

    @command()
    def float_doc_string(self, value):
        """Doc String: float value
        Args:
            value (float): A value of float type
        """
        return value

    @parameter(key="value", type="Boolean")
    def bool_parameter(self, value):
        """Parameter: bool value"""
        return value

    @command()
    def bool_type_hint(self, value: bool):
        """Type Hint: bool value"""
        return value

    @command()
    def bool_doc_string(self, value):
        """Doc String: bool value
        Args:
            value (bool): A value of bool type
        """
        return value

    @parameter(key="value", type="Dictionary")
    def dict_parameter(self, value):
        """Parameter: dict value"""
        return value

    @command()
    def dict_type_hint(self, value: dict):
        """Type Hint: dict value"""
        return value

    @command()
    def dict_output_type_hint(self, value: dict) -> dict:
        """Type Hint: default output to JSON for class type dict"""
        return value

    @command()
    def dict_doc_string(self, value):
        """Doc String: dict value
        Args:
            value (dict): A value of dict type
        """
        return value

    @command()
    def obj_type_hint(self, value: object):
        """Type Hint: object value (same input as dict)"""
        return value

    @command()
    def obj_output_type_hint(self, value: object) -> object:
        """Type Hint: default output to JSON for class type object"""
        return value

    @command()
    def obj_doc_string(self, value):
        """Doc String: object value (same input as dict)
        Args:
            value (object): A value of dict type
        """
        return value

    @parameter(key="value", type="DateTime")
    def date_time_parameter(self, value):
        """Parameter: datetime value"""
        return value

    @command()
    def date_time_type_hint(self, value: datetime):
        """Type Hint: datetime value"""
        return value

    @command()
    def date_time_doc_string(self, value):
        """Doc String: datetime value
        Args:
            value (datetime): A value of datetime type
        """
        return value

    @parameter(key="value", type="Bytes")
    def bytes_parameter(self, value):
        """Parameter: bytes value"""
        return value

    @command()
    def bytes_type_hint(self, value: bytes):
        """Type Hint: bytes value"""
        return value

    @command()
    def bytes_doc_string(self, value):
        """Doc String: bytes value
        Args:
            value (bytes): A value of bytes type
        """
        return value

    @parameter(key="value", type="Base64")
    def base64_parameter(self, value):
        """Parameter: base64 value"""
        return value.read()


def main():
    plugin = Plugin(
        name="parameters",
        version=__version__,
        description="Client that shows different options to declaring parameters",
    )
    plugin.client = ParametersClient()
    plugin.run()


if __name__ == "__main__":
    main()
