import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
x = df["Avg Rating"].tolist()
fig = ff.create_distplot([x], ["mobile rating"])
fig.show()