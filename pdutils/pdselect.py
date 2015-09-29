def pdselect(dataframe, **conditions):
    '''Select rows from a dataframe according to conditions

    Example::

        pdselect(data, a=2, b__lt=3)

    will select all rows where 'a' is 2 and 'b' is less than 3
    '''
    import pandas as pd
    if type(dataframe) == pd.Series:
        dataframe = pd.DataFrame({'value': dataframe})
    for cond,value in conditions.items():
        if cond in dataframe.columns:
            cond = dataframe[cond] == value
        elif cond.endswith('__gt'):
            cond = cond[:-len('__gt')]
            cond = dataframe[cond] > value
        elif cond.endswith('__ge'):
            cond = cond[:-len('__ge')]
            cond = dataframe[cond] >= value
        elif cond.endswith('__gte'):
            cond = cond[:-len('__gte')]
            cond = dataframe[cond] >= value
        elif cond.endswith('__lt'):
            cond = cond[:-len('__lt')]
            cond = dataframe[cond] < value
        elif cond.endswith('__le'):
            cond = cond[:-len('__le')]
            cond = dataframe[cond] <= value
        elif cond.endswith('__lte'):
            cond = cond[:-len('__lte')]
            cond = dataframe[cond] <= value
        else:
            raise ValueError("Cannot process condition '{}'".format(cond))
        dataframe = dataframe[cond]
    return dataframe
