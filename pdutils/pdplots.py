import numpy as np
import pandas as pd
def heatmap(
            frame,
            ax=None,
            cmap=None,
            vmin=None,
            vmax=None,
            interpolation='nearest',
            ):
    from matplotlib import pyplot as plt
    if ax is None:
        ax = plt.gca()
    ax.set_xticks(np.arange(frame.shape[1]))
    ax.set_xticklabels(frame.columns, rotation='vertical')

    ax.set_yticks(np.arange(frame.shape[0]))
    ax.set_yticklabels(frame.index)
    ax.grid(False)
    ax.set_aspect('auto')
    ax.imshow(frame.values, interpolation=interpolation, cmap=cmap, vmin=vmin, vmax=vmax, aspect='auto')
    return ax

def bare_axis(ax):
    ax.grid(False)
    ax.set_yticks([])
    ax.set_xticks([])

def _is_categorical(z):
    if isinstance(z, pd.Categorical):
        return True
    try:
        return isinstance(z.values, pd.Categorical)
    except:
        return False

def scatter_w_color(Xs, Ys, Zs=None, shape=None, factorize=False, cmap=None, sm=None, s=20, ax=None, vmax=None, vmin=None, cont=False, labels=None, colors=None, autolabels=False):
    '''
    Parameters
    ----------
    autolabels : boolean, optional
        If true, sets the axis labels to be ``Xs.name`` and ``Ys.name``, respectively
    '''
    if factorize and labels:
        raise ValueError('Factorize cannot be used with labels')
    from matplotlib import cm
    from matplotlib import colors as matcolors
    if ax is None:
        from matplotlib import pyplot as plt
        ax = plt.gca()
    if autolabels:
        xname = Xs.name
        yname = Ys.name
    Xs = np.asanyarray(Xs)
    Ys = np.asanyarray(Ys)
    if len(Xs) != len(Ys):
        raise ValueError('All args should be of the same length')

    if shape is None:
        ms = np.asanyarray(['o' for _ in Xs])
    else:
        ms = np.asanyarray(shape)
        if len(ms) != len(Xs):
            raise ValueError('Shape array should be of the same size as input data')

    Zs_max = 0
    if Zs is not None:
        if factorize or _is_categorical(Zs):
            Zs,labels = pd.factorize(Zs)
            cont = False
        else:
            Zs = np.asanyarray(Zs)
        Zs_max = Zs.max()
        if len(Xs) != len(Zs):
            raise ValueError('All args should be of the same length')
    elif cont:
        Zs = np.ones_like(Xs)
    if cont:
        if vmin is None:
            vmin = Zs.min()
        if vmax is None:
            vmax = Zs_max

        if sm is None:
            if cmap is None:
                from matplotlib import pyplot
                cmap = pyplot.get_cmap()
            sm = cm.ScalarMappable(matcolors.Normalize(vmin, vmax), cmap)
        elif cmap is not None:
            import warnings
            warnings.warn('scatter_w_color: cmap argument is ignored when sm is used (pass None to cmap to disable warning)')
        cs = sm.to_rgba(Zs)
        for x,y,c,m in zip(Xs, Ys, cs, ms):
            ax.scatter(x, y, c=c, s=s, marker=m)
    else:
        if colors is None and (Zs is not None):
            from brewer2mpl import get_map
            colors = get_map('Set1', 'Qualitative', max(3, Zs_max + 1)).mpl_colors
        c = None
        label = None
        seen_label = set()
        for ci in range(Zs_max + 1):
            if Zs is not None:
                cs = [colors[ci] for _ in range(sum(Zs == ci))]
                sel_xs = Xs[Zs == ci]
                sel_ys = Ys[Zs == ci]
                sel_ms = ms[Zs ==ci]
            else:
                cs = (colors[0] if colors else ['k' for _ in Xs])
                sel_xs = Xs
                sel_ys = Ys
                sel_ms = ms
            if labels is not None:
                label = labels[ci]
            if sel_ms is None:
                ms = None
                ax.scatter(sel_xs, sel_ys, c=c, s=s, marker=sel_ms, label=label)
            elif len(set(sel_ms)) is None:
                ms = sel_ms[0]
                ax.scatter(sel_xs, sel_ys, c=c, s=s, marker=sel_ms, label=label)
            else:
                for x,y,c,m in zip(sel_xs, sel_ys, cs, sel_ms):
                    ax.scatter(x, y, c=c, s=s, marker=m, label=(label if label not in seen_label else None))
                    seen_label.add(label)

    if autolabels:
        ax.set_xlabel(xname)
        ax.set_ylabel(yname)
    return ax

def compareplotu(data, groupby, kind='boxplot', add_p_val_to_plot=True, ax=None):
    '''Compare two groups visually and print out mann-whitney U'''
    from seaborn import apionly as sns
    from .pdstats import mannwhitneyu

    if ax is None:
        from matplotlib import pyplot as plt
        fig,ax = plt.subplots()
    if kind == 'boxplot':
        sns.boxplot(data, groupby=groupby, ax=ax)
    elif kind == 'violinplot':
        sns.violinplot(data, groupby=groupby, ax=ax)
    else:
        raise ValueError("Unknown plot kind '{}'".format(kind))

    u, p = mannwhitneyu(data, groupby=groupby)
    print("Mann-Whitney U: p-value: {}".format(p))
    if add_p_val_to_plot:
        ax.set_title("Mann-Whitney U test p-value: {:.2}".format(p))

    return ax

