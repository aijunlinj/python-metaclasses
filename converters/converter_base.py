from collections import defaultdict

class ConverterMeta(type):

    converter_lookup = defaultdict(lambda: {})

    def __new__(typ, name, bases, attr_dict):
        klass = type.__new__(typ, name, bases, attr_dict)
        ConverterMeta.register_converter(klass)
        return klass

    @classmethod
    def register_converter(cls, klass):
        if hasattr(klass, 'REGISTER') and klass.REGISTER==False:
            return

        if not hasattr(klass, 'TYPE') or klass.TYPE is None:
            raise ValueError(f'class {klass.__name__} did not define TYPE attribute')
        if not hasattr(klass, 'NAME') or klass.NAME is None:
            raise ValueError(f'class {klass.__name__} did not define NAME attribute')

        print(f'Registering class {klass.__name__}, TYPE = {klass.TYPE}, NAME = {klass.NAME}')
        # TODO: check TYPE and NAME clashes (i.e. different classes define the same TYPE and NAME
        cls.converter_lookup[klass.TYPE][klass.NAME] = klass()


    @classmethod
    def de_registor_converter(cls, converter_type: str, converter_name):
        try:
            converters = cls.converter_lookup.get(converter_type)
            if converters:
                converters.pop(converter_name)
        except KeyError:
            print(f"Converter of type {converter_type} and name {converter_name} doesn't exist")


    @classmethod
    def get_converter(cls, converter_type, converter_name):
        if not converter_type in cls.converter_lookup:
            raise ValueError(f'Converter of type {converter_type} not found')
        converters = cls.converter_lookup[converter_type]
        if not converter_name in converters:
            raise ValueError(f'Converter name {converter_name} not found')
        return converters[converter_name]


class ConverterBase(metaclass=ConverterMeta):
    TYPE = 'Converter'
    NAME = 'Base'
    REGISTER = False

    def convert(self, value):
        raise NotImplementedError('Sub class must provide implementation for convert')
