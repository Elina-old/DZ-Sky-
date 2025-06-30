from string_utils import StringUtils
import pytest

string_funcs = StringUtils()

class TestStringUtils:

    @pytest.mark.parametrize(["input_data", "expected_data"], [("hello", "Hello"), ("w", "W"), ("мышь", "Мышь")])
    def test_capitalize_pozitiv(self, input_data: str, expected_data: str):
        res = string_funcs.capitalize(string=input_data)
        assert res == expected_data

    @pytest.mark.parametrize(["input_data", "expected_data"], [("1hello", "1hello"), ("", ""), ("  ", "  ")])
    def test_capitalize_negativ(self, input_data: str, expected_data: str):
        res = string_funcs.capitalize(string=input_data)
        assert res == expected_data

    @pytest.mark.parametrize(["input_data", "simvol", "expected"], [("hello", "e", True), (" 123", " 1", True), ("RER", "R", True)])
    def test_contens_positiv(self, input_data: str, simvol: str, expected: bool):
        res = string_funcs.contains(string=input_data, symbol=simvol)
        assert res == expected


    @pytest.mark.parametrize(["input_data", "simvol", "expected"], [("hello", "he", "llo"), ("Flai", "F", "lai"), ("Test", "T", "est")])
    def test_delete_symbol_positiv(self, input_data: str, simvol: str, expected: bool):
        res = string_funcs.delete_symbol(string=input_data, symbol=simvol)
        assert  res == expected

    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [("hi my friend", "Hi my friend"),("30 июня 2025", "30 июня 2025"), ("Hey buddy", "Hey buddy")])
    def test_capitalize_positive(self, input_str: str, expected: str ):
        assert string_funcs.capitalize(input_str) == expected
