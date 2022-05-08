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

import imp
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.tools as tls
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def plotSeasonalDecompose(
    x,
    model='additive',
    filt=None,
    period=None,
    two_sided=True,
    extrapolate_trend=0,
    title="Seasonal Decomposition"):


    result = seasonal_decompose(
            x, model=model, filt=filt, period=period,
            two_sided=two_sided, extrapolate_trend=extrapolate_trend)
    fig = make_subplots(
            rows=4, cols=1,
            subplot_titles=["Observed", "Trend", "Seasonal", "Residuals"])
    fig.add_trace(
            go.Scatter(x=result.seasonal.index, y=result.observed, mode='lines'),
                row=1, col=1,
            )

    fig.add_trace(
            go.Scatter(x=result.trend.index, y=result.trend, mode='lines'),
                row=2, col=1,
            )

    fig.add_trace(
            go.Scatter(x=result.seasonal.index, y=result.seasonal, mode='lines'),
                row=3, col=1,
            )

    fig.add_trace(
            go.Scatter(x=result.resid.index, y=result.resid, mode='lines'),
                row=4, col=1,
            )

    return fig

"""
This is a function to create a triangle correlation heatmap from a dataframe
"""
# import modules
import matplotlib.pyplot as plt
#import pandas as pd
import seaborn as sns
import numpy as np

def makeCorrPlot(df):
    # import file with data
    data = df
    # creating mask
    mask = np.triu(np.ones_like(data.corr()))
    # plotting a triangle correlation heatmap
    dataplot = sns.heatmap(data.corr(), cmap="YlGnBu", annot=True, mask=mask)    
    # displaying heatmap
    plt.show()