

class BooleanSeries:

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, bool) or val is None):
                raise TypeError('{} is not bool or None'.format(val))

        self.name = name
        self.data = data

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return len(self.data) == len(other.data) and self.data == other.data

    # NOT TESTED
    def __and__(self, other):
        return BooleanSeries(self.data and other.data, self.name)

    # NOT TESTED
    def __or__(self, other):
        return BooleanSeries(self.data and other.data, self.name)

    def __invert__(self):
        data = []
        for elem in self.data:
            if elem is None:
                data.append(None)
            else:
                data.append(not elem)
        return BooleanSeries(data, self.name)


class StringSeries:

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, str) or val is None):
                raise TypeError('{} is not str or None'.format(val))

        self.name = name
        self.data = data

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return len(self.data) == len(other.data) and self.data == other.data


class IntegerSeries:

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, int) or val is None):
                raise TypeError('{} is not int or None'.format(val))

        self.name = name
        self.data = data

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return len(self.data) == len(other.data) and self.data == other.data

    def __gt__(self, target):
        data = []
        for elem in self.data:
            if elem is not None and elem > target:
                data.append(elem)
        return IntegerSeries(data, self.name)

    # TODO: implement __ne__, __ge__, __lt__, __le__


class FloatSeries:

    def __init__(self, data, name=None):
        # check type
        for val in data:
            if not (isinstance(val, float) or val is None):
                raise TypeError('{} is not float or None'.format(val))

        self.name = name
        self.data = data

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return len(self.data) == len(other.data) and self.data == other.data

    def __gt__(self, target):
        data = []
        for elem in self.data:
            if elem is not None and elem > target:
                data.append(elem)
        return FloatSeries(data, self.name)

    # TODO: implement __ne__, __ge__, __lt__, __le__
