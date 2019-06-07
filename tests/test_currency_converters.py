from unittest import TestCase
from converters.converter_base import ConverterBase
# Below import is required in order for Python interpretor to load the converter classes
from converters.currency_converter import *

class TestCurrencyConverters(TestCase):
    def test_usd_to_gbp(self):
        usd = 100.0
        converter = ConverterBase.get_converter('Currency', 'usd_to_gbp')
        converted = converter.convert(usd)
        print(f'\n${usd} converts to {converted} GBP')
        self.assertEqual(converted, 76.0)

    def test_usd_to_jpy(self):
        usd = 100.0
        converter = ConverterBase.get_converter('Currency', 'usd_to_jpy')
        converted = converter.convert(usd)
        print(f'${usd} converts to {converted} JPY')
        self.assertEqual(converted, 11109.0)