import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = px.data.gapminder()

fig = make_subplots(rows=1, cols=1)
frames = []

# Create frames for each step of the animation
for i, x in enumerate(df.loc[df.continent.isin(["Europe"])].country.unique()[:5]):
    fil = df.loc[(df.country.str.contains(x))]
    frame = go.Frame(
        data=[
            go.Scatter(
                x=fil["year"].iloc[:i+1],
                y=fil["pop"].iloc[:i+1],
                mode="lines+markers",
                marker=dict(
                    symbol="arrow",
                    size=15,
                    angleref="previous",
                ),
                name=x,
            )
        ],
        name=f'frame{i}',
    )
    frames.append(frame)

# Add initial trace without data to set up the layout
fig.add_trace(go.Scatter(), row=1, col=1)

# Add frames to the figure
fig.frames = frames

# Set up animation configuration
fig.update_layout(updatemenus=[{
    "buttons": [
        {
            "args": [None, {"frame": {"duration": 800, "redraw": True}, "fromcurrent": True}],
            "label": "Play",
            "method": "animate",
        },
        {
            "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
            "label": "Pause",
            "method": "animate",
        },
    ],
    "direction": "left",
    "pad": {"r": 10, "t": 87},
    "showactive": False,
    "type": "buttons",
    "x": 0.1,
    "xanchor": "right",
    "y": 0,
    "yanchor": "top"
}])

fig.update_layout(
    title="Population Growth Over Years in European Countries",
    xaxis=dict(title="Year"),
    yaxis=dict(title="Population"),
    updatemenus=[],
)

fig.show(renderer="browser")
