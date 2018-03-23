__all__ = ['TRANSFORM']


class TRANSFORM(object):
    __doc__ = '< TypeClass : TRANSFORM > \n Welcome, This file converts all mathematical data from kilogram to ' \
              'gram and vice versa'
    __slots__ = ['__VALUE__']

    def __init__(self, VALUE):
        self.__VALUE__ = VALUE

    def __mul__(self):
        """ KILOGRAM -> GRAM """
        __Value__ = ['Value in kg', 'KG']

        print('{0} -> {1} {2}'.format(__Value__[0], self.__VALUE__ * 10 ** 3, __Value__[1]))

    def __pow__(self):
        """ GRAM -> KILOGRAM """
        __Value__ = ['Value in g', 'G']
        print('{0} -> {1} {2}'.format(__Value__[0], self.__VALUE__ * 10 ** (-3), __Value__[1]))
