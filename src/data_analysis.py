import numpy as np
import matplotlib.pyplot as pyp
import pandas as pd
import seaborn as sb

def getName(data, column):
    return data.icol(column).name if column.isnumeric() else column

def frequency(data, column, target = None):
    column = getName(data,column)
    return data[column].value_counts()


def stat_by_col(data, column, target = None, agg_func=[np.size,np.mean,np.std,np.min,np.max,np.var]):
    column, target = (getName(data, column), getName(data, target))
    stat_compute = data.groupby(column).agg(agg_func)[target]
    return stat_compute

def num_missing_val(data):
    return data.isnull().apply(lambda x : x.value_counts(),0)

def freq_hist(data, column, target = None, numbins = 10):
    column = getName(data, column)
    qcols = data.columns[data.dtypes != 'category']
    data[column].plot.hist(bins=numbins)

def hist_by_col(data, column, target, numbins = 10):
    column, target = (getName(data, column), getName(data, target))
    data.hist(column=target, by=column,  bins=numbins)

def barplot_by_col(data,column, target, agg_func=sum, stacked=False):
    column, target = (getName(data, column), getName(data, target))
    stat = stat_by_col(data, column, target, agg_func)
    stat.plot.bar(stacked = stacked)

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

def violin_plot(data, column, target):
    column, target = (getName(data,column),getName(data,target))
    pyp.xticks(rotation=90)
    sb.violinplot(x=column, y = target, data = data, color_palette = 'deep')

def scatter_plot(data, column, target):
    column, target = (getName(data, column), getName(data, target))
    data.plot(x=column, y=target, kind='scatter')

def linear_regression_plot(data, column, target, ci = .90):
    column, target = (getName(data, column), getName(data, target))
    sb.regplot(x = column, y = target, data = data, color = 'darkred', ci = ci)

def corr_heat_map(data):
    corr = data.select_dtypes(include=['float64','int64']).corr()
    pyp.yticks(rotation=90)
    pyp.xticks(rotation=90)
    sb.heatmap(corr, vmax = 1, square = True)

def grid_plot(data, target = 'No Target',nrows = 2, ncols=3, plot_type=sb.countplot, type = 'quant'):
    target = getName(data, target)
    if type == 'quant':
        qcols = data.columns[data.dtypes != 'category']
    else:
        qcols = data.columns[data.dtypes == 'category']
    chart_index = 0
    loop_break = False
    for i in np.arange(0,np.ceil(len(qcols)/(nrows+ncols)).__int__()+1):
        if loop_break:
            break
        #fig,axes = pyp.subplots(nrows = nrows,ncols = ncols,sharex=False,sharey=True,squeeze=True)
        fig, axes = pyp.subplots(nrows=nrows, ncols=ncols)
        for j in np.arange(0, nrows):
            if loop_break:
                break
            for k in np.arange(0, ncols):
                if chart_index >= len(qcols):
                    loop_break=True
                    break
                if target == 'No Target':
                    data[qcols[chart_index]].plot(kind=plot_type, ax=axes[j, k], title=qcols[chart_index])
                else:
                    #data.plot(x=qcols[chart_index], y=target, kind=plot_type, ax=axes[j, k])

                    #plot_type(column = qcols[chart_index], target=target, data = data, ax = axes[j,k])
                    plot_type(column = qcols[chart_index], target=target, data = data)

                chart_index = chart_index + 1


