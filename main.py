import series
from dataframe import Dataframe

if __name__ == '__main__':
    # construct the dataframe
    df = Dataframe({
        'SKU': series.StringSeries(['X4E', 'T3B', 'F8D', 'C7X'], 'SKU'),
        'price': series.FloatSeries([7.0, 3.5, 8.0, 6.0], 'price'),
        'sales': series.IntegerSeries([5, 3, 1, 10], 'sales'),
        'taxed': series.BooleanSeries([False, False, True, False], 'taxed')
    })

    # let's find all our tax free products/SKUs where the price
    # + our $5.0 shipping fee is more than $10 and we had more than 3 sales
    result = df[
        (df["price"] + 5.0 > 10.0)
        & (df["sales"] > 3)
        & ~df["taxed"]
        ]["SKU"]

    print(result)

