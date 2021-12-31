import pandas as p
import plotly.figure_factory as ff
import csv
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["Height(Inches)"].to_list()],["height"],show_hist=False)
fig.show()