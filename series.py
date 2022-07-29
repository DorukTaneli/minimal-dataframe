def factory(dtype, data, name=None):
    if dtype == str:
        return StringSeries(data, name)
    elif dtype == bool:
        return BooleanSeries(data, name)
    elif dtype == int:
        return IntegerSeries(data, name)
    elif dtype == float:
        return FloatSeries(data, name)
    else:
        raise TypeError('{} type not supported. '
                        'Supported Series Types: str, bool, int, float'.format(dtype))


def expand_single_value_to_series_if_necessary(series, other):
    if not issubclass(type(other), Series):
        return factory(type(other), [other] * len(series.data))
    else:
        return other


class Series:
    def __init__(self, data, name=None):
        self.data = data
        self.name = name

    def __str__(self):
        return '''
        type: {}
        name: {}
        data: {}'''.format(type(self), self.name, str(self.data))

    # fail hard if the Series types or lengths are different
    # otherwise perform an element-wise comparison returning a boolean Series.
    def __eq__(self, other):
        other = expand_single_value_to_series_if_necessary(self, other)

        if type(self) != type(other):
            raise TypeError('Series have different types: {} and {}'.format(type(self), type(other)))
        elif len(self.data) != len(other.data):
            raise RuntimeError('Series have different lengths')
        else:
            element_wise_comparison = []
            for i in range(len(self.data)):
                element_wise_comparison.append(self.data[i] == other.data[i])
            return BooleanSeries(element_wise_comparison, 'comparison result')

    # for testing purposes
    def has_same_data(self, other):
        return self.data == other.data


class BooleanSeries(Series):

    dtype = bool

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, bool) or val is None):
                raise TypeError('{} is not bool or None'.format(val))

        Series.__init__(self, data, name)

    def __invert__(self):
        data = []
        for elem in self.data:
            if elem is None:
                data.append(None)
            else:
                data.append(not elem)
        return BooleanSeries(data, self.name)

    # TODO: Tested, Does not work as expected
    def __and__(self, other):
        other = expand_single_value_to_series_if_necessary(self, other)
        comparison = []
        for i in range(len(self.data)):
            if self.data[i] is None or other.data[i] is None:
                comparison.append(None)
            else:
                comparison.append(self.data[i] and other.data[i])
        return BooleanSeries(comparison, self.name)

    # TODO: implement __or__, __xor__


class StringSeries(Series):

    dtype = str

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, str) or val is None):
                raise TypeError('{} is not str or None'.format(val))

        Series.__init__(self, data, name)


class NumericalSeries(Series):

    def __init__(self, data, name):
        Series.__init__(self, data, name)

    # Element-wise addition, returns None if one of the elements is None
    def __add__(self, other):
        other = expand_single_value_to_series_if_necessary(self, other)
        addition = []
        for i in range(len(self.data)):
            if self.data[i] is None or other.data[i] is None:
                addition.append(None)
            else:
                addition.append(self.data[i] + other.data[i])
        return factory(other.dtype, addition, self.name)

    # Element-wise comparison, returns None if one of the elements compared is None
    def __gt__(self, other):
        other = expand_single_value_to_series_if_necessary(self, other)
        comparison = []
        for i in range(len(self.data)):
            if self.data[i] is None or other.data[i] is None:
                comparison.append(None)
            else:
                comparison.append(self.data[i] > other.data[i])
        return BooleanSeries(comparison, self.name)

    # TODO: implement math operations: __sub__, __mul__, __truediv__
    # TODO: implement inequalities: __ne__, __ge__, __lt__, __le__


class IntegerSeries(NumericalSeries):

    dtype = int

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, int) or val is None):
                raise TypeError('{} is not int or None'.format(val))

        NumericalSeries.__init__(self, data, name)


class FloatSeries(NumericalSeries):

    dtype = float

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, float) or val is None):
                raise TypeError('{} is not float or None'.format(val))

        NumericalSeries.__init__(self, data, name)
