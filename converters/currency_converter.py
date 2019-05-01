from converters.converter_base import ConverterBase

__all__ = ['USDToGBP', 'USDToJPY']

class CurrencyConverterBase(ConverterBase):
    TYPE = 'Currency'
    NAME = 'CurrencyConverterBase'
    REGISTER = False


class USDToGBP(CurrencyConverterBase):
    NAME = 'usd_to_gbp'
    REGISTER = True

    def __init__(self):
        self.exchange_rate = 0.76

    def convert(self, value):
        return self.exchange_rate * float(value)

class USDToJPY(CurrencyConverterBase):
    NAME = 'usd_to_jpy'
    REGISTER = True

    def __init__(self):
        self.exchange_rate = 111.09

    def convert(self, value):
        return self.exchange_rate * float(value)