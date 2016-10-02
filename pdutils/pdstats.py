from scipy import stats
def mannwhitneyu(data, groupby, reindex=False, alternative='two-sided'):
    '''Mann-Whitney U based on groupby

    Parameters
    ----------
    data : pandas series
    groupby : pandas Series
        This is used to form groups for the comparisons

    reindex : bool, optional
        If true, then the `groupby` argument is first *reindexed* to match
        `data`.

    Returns
    -------
    u, p: float
        Same return as `scipy.stats.mannwhitneyu`
    '''
    if reindex:
        groupby = groupby.reindex(index=data.index)
    g = data.groupby(groupby)
    g1, g2 = g.groups.values()
    return stats.mannwhitneyu(data.ix[g1], data.ix[g2], alternative=alternative)

def kruskal(data, groupby, reindex=False):
    '''Kruskal based on groupby

    Parameters
    ----------
    data : pandas series
    groupby : pandas Series
        This is used to form groups for the comparisons

    reindex : bool, optional
        If true, then the `groupby` argument is first *reindexed* to match
        `data`.

    Returns
    -------
    u, p: float
        Same return as `scipy.stats.kruskal`
    '''
    if reindex:
        groupby = groupby.reindex(index=data.index)
    g = data.groupby(groupby)
    return stats.kruskal(*[data.ix[g] for g in g.groups.values()])
