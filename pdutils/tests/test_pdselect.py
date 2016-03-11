import pandas as pd
from pdutils import pdselect
import numpy as np

def test_in_not_in():
    x = pd.DataFrame([[1,2],[2,1],[3,1],[4,3]], columns=['N', 'C'])
    assert np.all(pdselect(x, C__in=[1]) == pdselect(x, C=1))
    assert np.all(pdselect(x, C__in=[2]) == pdselect(x, C=2))
    assert np.all(pdselect(x, C__not_in=[1]) == pdselect(x, C__neq=1))
    c12 = pdselect(x, C__in=[1,2]).C
    assert np.all((c12 == 1) | (c12 == 2))
    cn12 = pdselect(x, C__not_in=[1,2]).C
    assert np.all((cn12 != 1) | (cn12 != 2))

