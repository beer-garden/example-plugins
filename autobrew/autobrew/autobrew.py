import sys
from datetime import datetime
from typing import Literal


class AutoBrewClient(object):
    """Auto Brew Client that shows different options to declaring parameters"""

    __version__ = "3.0.0.dev0"

    def any_default(self, value):
        """Any is the default type for any undeclared variables"""
        return value

    def string_type_hint(self, value: str):
        """Type Hint: String value"""
        return value

    def string_doc_string(self, value):
        """Doc String: String value
        Args:
            value (str): A value of String type
        """
        return value

    if sys.version_info.major == 3 and sys.version_info.minor >= 8:

        def string_type_hint_choices(self, value: Literal["value1", "value2"]):
            """Type Hint: String value"""
            return value

    def int_type_hint(self, value: int):
        """Type Hint: int value"""
        return value

    if sys.version_info.major == 3 and sys.version_info.minor >= 8:

        def int_type_hint_choices(self, value: Literal[1, 2]):
            """Type Hint: String value"""
            return value

    def int_doc_string(self, value):
        """Doc String: int value
        Args:
            value (int): A value of int type
        """
        return value

    def float_type_hint(self, value: float):
        """Type Hint: float value"""
        return value

    def float_doc_string(self, value):
        """Doc String: float value
        Args:
            value (float): A value of float type
        """
        return value

    def bool_type_hint(self, value: bool):
        """Type Hint: bool value"""
        return value

    def bool_doc_string(self, value):
        """Doc String: bool value
        Args:
            value (bool): A value of bool type
        """
        return value

    def dict_type_hint(self, value: dict):
        """Type Hint: dict value"""
        return value

    def dict_output_type_hint(self, value: dict) -> dict:
        """Type Hint: default output to JSON for class type dict"""
        return value

    def dict_doc_string(self, value):
        """Doc String: dict value
        Args:
            value (dict): A value of dict type
        """
        return value

    def obj_type_hint(self, value: object):
        """Type Hint: object value (same input as dict)"""
        return value

    def obj_output_type_hint(self, value: object) -> object:
        """Type Hint: default output to JSON for class type object"""
        return value

    def obj_doc_string(self, value):
        """Doc String: object value (same input as dict)
        Args:
            value (object): A value of dict type
        """
        return value

    def date_time_type_hint(self, value: datetime):
        """Type Hint: datetime value"""
        return value

    def date_time_doc_string(self, value):
        """Doc String: datetime value
        Args:
            value (datetime): A value of datetime type
        """
        return value

    def bytes_type_hint(self, value: bytes):
        """Type Hint: bytes value"""
        return value

    def bytes_doc_string(self, value):
        """Doc String: bytes value
        Args:
            value (bytes): A value of bytes type
        """
        return value
