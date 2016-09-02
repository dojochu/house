import numpy as np
import matplotlib.pyplot as pyp
import pandas as pd

def getName(data, column):
    if (column.isnumeric()):
        return data.icol(column).name
    return column

def frequency(data, column):
    column = getName(data,column)
    return data[column].value_counts()


def stat_by_col(data, column, target, agg_func=[np.size,np.mean,np.std,np.min,np.max,np.var]):
    column = getName(data, column)
    target = getName(data, target)
    stat_compute = data.groupby(column).agg(agg_func)[target]
    return stat_compute

def num_missing_val(data):
    return data.isnull().apply(lambda x : x.value_counts(),0)

def freq_hist(data, column):
    column = getName(data, column)
    freq = frequency(data,column)
    freq.plot.bar()

def barplot_by_col(data,column, target, agg_func=sum):
    column = getName(data, column)
    target = getName(data, target)
    stat = stat_by_col(data, column, target, agg_func)
    stat.plot.bar()

def freq_box(data, column):
    column = getName(data, column)
    freq = frequency(data, column)
    freq.plot.box()

def boxplot(data, column):
    column = getName(data, column)
    data[column].plot.box()

def boxplot_by_col(data, column, target):
    column, target = (getName(data, column),getName(data, target))
    data.boxplot(column=target, by=column, rot = 90)

def scatter_corr_plot(data, y, ncols):
    qcols = data.columns[data.dtypes != 'category']
    fig,axes = pyp.subplots(nrows = np.ceil(len(qcols)/ncols).__int__()+1,ncols = ncols,sharex=False,sharey=True,squeeze=True)
    for i in np.arange(0,len(qcols)):
        data.plot(x=qcols[i], y=y, kind='scatter', ax=axes[np.floor(i/ncols), i % ncols])
