import pandas as p
import plotly.figure_factory as ff
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].to_list()],["weight"],show_curve=False)
fig.show()