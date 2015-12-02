import numpy.lib
import numpy as np
import pandas as pd
import pickle

def save_pandas(fname, data):
    '''Save DataFrame or Series

    Parameters
    ----------
    fname : str
        filename to use
    data: Pandas DataFrame or Series
    '''
    with open(fname, 'wb') as fo:
        np.save(fo, data)
    if len(data.shape) == 2:
        meta = data.index,data.columns
    elif len(data.shape) == 1:
        meta = (data.index,)
    else:
        raise ValueError('save_pandas: Cannot save this type')
    s = pickle.dumps(meta, protocol=pickle.HIGHEST_PROTOCOL)
    with open(fname, 'ab') as f:
        f.seek(0, 2)
        f.write(s)

def load_pandas(fname, mmap_mode='r'):
    '''Load DataFrame or Series

    Parameters
    ----------
    fname : str
        filename
    mmap_mode : str, optional
        Same as numpy.load option
    '''
    values = np.load(fname, mmap_mode=mmap_mode)
    with open(fname, 'rb') as f:
        numpy.lib.format.read_magic(f)
        numpy.lib.format.read_array_header_1_0(f)
        f.seek(values.dtype.alignment*values.size, 1)
        meta = pickle.loads(f.read())
    if len(meta) == 2:
        return pd.DataFrame(values, index=meta[0], columns=meta[1])
    elif len(meta) == 1:
        return pd.Series(values, index=meta[0])
