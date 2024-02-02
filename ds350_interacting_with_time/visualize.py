# %%
import polars as pl
import pandas as pd
import plotly.express as px

import plotly.graph_objects as gg
from datetime import datetime
from lets_plot import *
LetsPlot.setup_html()

# %%
pdat = pl.read_parquet("stock.parquet")

# %%
# Create a time series chart that shows performance of all 10 stocks.
gg.plot(pdat, aes(x="date", y="adjClose", color='ticker')) + \
    geom_line() + \
    scale_x_datetime() + \
    labs(
        x="Date",
        y="Adjusted Closing Price",
        title="My chart of the top 10 stocks"
)

# %%
# now fix the html size and only show the last year and save the chart

# %%
# plotly candlestick chart
# https://plotly.com/python/candlestick-charts/
