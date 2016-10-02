from pdutils import pdstats
from scipy import stats
import pandas as pd
import numpy as np

def gen_data():
    data = np.random.rand(100)
    data = np.vstack([np.zeros_like(data), data])
    data[0,50:] = 1
    return pd.DataFrame(data.T, index=['v{}'.format(i) for i in range(data.shape[1])], columns=['ID', 'Val'])


def test_mannwhitneyu():
    data = gen_data()
    r_p = pdstats.mannwhitneyu(data.Val, groupby=data.ID)
    assert stats.mannwhitneyu(data.Val[:50], data.Val[50:], alternative='two-sided') == r_p

def test_kruskal():
    data = gen_data()
    data.ID[:25] = -1
    k = pdstats.kruskal(data.Val, groupby=data.ID)
    assert stats.kruskal(data.Val[:25], data.Val[25:50], data.Val[50:]) == k
