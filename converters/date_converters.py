import re
from converters.converter_base import ConverterBase

__all__ = ['MMDDYYYYToISODate', 'YYYYMMDDToISODate', 'YYMMDDToISODate']

VALID_SEPARATORS = '[-/]'

class MMDDYYYYToISODate(ConverterBase):
    """Convert mmddyyyy format to standard ISO date format."""
    TYPE = 'Date'
    NAME = 'mmddyyyy_to_iso_date'
    REGISTER = True

    def __init__(self):
        self.pattern = re.compile('^([0-9]{2})%s{0,1}([0-9]{2})%s{0,1}([0-9]{4})$' % (
                VALID_SEPARATORS, VALID_SEPARATORS)
        )

    def convert(self, value):
        match = self.pattern.match(value)
        return '%04d-%02d-%02d' % (
            int(match.group(3)), int(match.group(1)), int(match.group(2))
        )


class YYYYMMDDToISODate(ConverterBase):
    """Convert yyyymmdd format to standard ISO date format."""
    TYPE = 'Date'
    NAME = 'yyyymmdd_to_iso_date'
    REGISTER = True

    def __init__(self):
        self.pattern = re.compile('^([0-9]{4})%s{0,1}([0-9]{2})%s{0,1}([0-9]{2})$' % (
                VALID_SEPARATORS, VALID_SEPARATORS)
        )

    def convert(self, value):
        match = self.pattern.match(value)
        return '%04d-%02d-%02d' % (
            int(match.group(1)), int(match.group(2)), int(match.group(3))
        )


class YYMMDDToISODate(ConverterBase):
    """Convert yymmdd format to standard ISO date format."""
    TYPE = 'Date'
    NAME = 'yymmdd_to_iso_date'
    REGISTER = True

    def __init__(self):
        self.pattern = re.compile('^([0-9]{2})%s{0,1}([0-9]{2})%s{0,1}([0-9]{2})$' % (
                VALID_SEPARATORS, VALID_SEPARATORS)
        )

    def convert(self, value):
        match = self.pattern.match(value)
        return '%04d-%02d-%02d' % (
            int('20' + match.group(1)), int(match.group(2)), int(match.group(3))
        )
