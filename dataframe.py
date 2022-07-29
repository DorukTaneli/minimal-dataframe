from series import BooleanSeries


class Dataframe:

    def __init__(self, dict_series):
        self.dict_series = dict_series

    def __str__(self):
        return str(self.dict_series)

    # when given a string returning the respective Series,
    # or when given a boolean Series returns another DataFrame containing only the rows with True values
    def __getitem__(self, item):
        if isinstance(item, str):
            return self.dict_series[item]
        elif isinstance(item, BooleanSeries):
            bool_series = item
            row_indexes_to_get = []
            for i in range(len(bool_series.data)):
                if bool_series.data[i]:
                    row_indexes_to_get.append(i)
            result = Dataframe({})
            for key in self.dict_series:
                lst = self.dict_series[key].data
                result.dict_series[key] = [lst[j] for j in row_indexes_to_get]
            return result
        else:
            raise RuntimeError('Unexpected type {} in __getitem__'.format(type(item)))

