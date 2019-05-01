from unittest import TestCase
from converters.date_converters import *
from converters.converter_base import ConverterBase

class TestDateConverters(TestCase):

    def test_yyyymmdd(self):
        date_str = '20190101'
        converter = ConverterBase.get_converter('Date', 'yyyymmdd_to_iso_date')
        converted = converter.convert(date_str)
        self.assertEqual(converted, '2019-01-01')

    def test_mmddyyyy(self):
        date_str = '04012019'
        converter = ConverterBase.get_converter('Date', 'mmddyyyy_to_iso_date')
        converted = converter.convert(date_str)
        self.assertEqual(converted, '2019-04-01')


    def test_yymmdd(self):
        date_str = '190401'
        converter = ConverterBase.get_converter('Date', 'yymmdd_to_iso_date')
        converted = converter.convert(date_str)
        self.assertEqual(converted, '2019-04-01')