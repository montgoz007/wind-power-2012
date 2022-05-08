"""
This is an area to put helper functions so that my notebooks are not as messy
"""

"""
This is a function to create a univariate series from a dataframe with a datetime index
"""

def getSeries(df, var):
    series = df[['date', var]]
    series = series.set_index('date')
    return series

"""
This is a function to use plotly for seasonal decomposition
"""

