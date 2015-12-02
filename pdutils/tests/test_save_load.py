import numpy as np
import pandas as pd
from pdutils import load_pandas, save_pandas
from os import unlink

def test_save_load():
    X = pd.DataFrame(np.random.random((20,5)), index=["I{}".format(i) for i in range(20)], columns=["C.{}".format(i) for i in range(5)])
    save_pandas('testing.pdy', X)
    X2 = load_pandas('testing.pdy')
    assert np.all(X == X2)
    assert np.all(X.index == X2.index)
    assert np.all(X.columns == X2.columns)
    unlink('testing.pdy')
