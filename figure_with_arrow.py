import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder()

fig = go.Figure()

for x in df.loc[df.continent.isin(["Europe"])].country.unique()[:5]:
    fil = df.loc[(df.country.str.contains(x))]
    fig.add_trace(
        go.Scatter(
            x=fil["year"],
            y=fil["pop"],
            mode="lines+markers",
            marker=dict(
                symbol="arrow",
                size=15,
                angleref="previous",
            ),
            name=x,
        )
    )
fig.show(renderer="browser")