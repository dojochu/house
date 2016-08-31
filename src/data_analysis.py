

def frequency(data, column):
    if (column.isnumeric()):
        column = data.icol(column).name
    return data[column].value_counts()


def stat_by_col(data, column, target):
    if (column.isnumeric()):
        column = data.icol(column).name
    if (target.isnumeric()):
        target = data.icol(target).name
    stat_compute = data.groupby(column).describe()[target]

    return