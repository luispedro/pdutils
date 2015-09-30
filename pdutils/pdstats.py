from scipy import stats
def mannwhitneyu(data, groupby):
    '''Mann-Whitney U based on groupby

    Parameters
    ----------
    data : pandas series
    groupby : pandas Series
        This is used to form groups for the comparisons

    Returns
    -------
    u, p: float
        Same return as `scipy.stats.mannwhitneyu`
    '''
    g = data.groupby(groupby)
    g1, g2 = g.groups.values()
    return stats.mannwhitneyu(data.ix[g1], data.ix[g2])
