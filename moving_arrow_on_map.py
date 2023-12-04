import plotly.graph_objects as go
import numpy as np

# Define the two points
p0 = np.array([44.7, -68])
p1 = np.array([44.9, -69])

# Calculate the slope (m) and intercept (c) of the line
m = (p1[1] - p0[1]) / (p1[0] - p0[0])
c = p0[1] - m * p0[0]

# Generate x values for the line
x = np.linspace(p0[0], p1[0], num=20)

# Calculate y values using the equation of the line (y = mx + c)
y = m * x + c

xm = np.min(x) - 1
xM = np.max(x) + 1
ym = np.min(y) - 1
yM = np.max(y) + 1

N = 20

xx = np.linspace(p0[0], p1[0], num=N)
yy = m * xx + c

angle_rad = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
angle_deg = np.degrees(angle_rad)
if angle_deg < 0:
    angle_deg -= 135

if angle_deg > 0:
    angle_deg -= 45

fig = go.Figure(
    data=[
        go.Scattermapbox(
            lat=[p0[0], p1[0]],  # Latitude data for the two points
            lon=[p0[1], p1[1]],  # Longitude data for the two points
            mode="markers+lines",  # Display as markers and lines
            marker=dict(size=10, color="blue"),  # Marker properties
            line=dict(width=2, color="blue"),  # Line properties
        ),
        go.Scattermapbox(
            lat=[p0[0], p1[0]],  # Latitude data for the two points
            lon=[p0[1], p1[1]],  # Longitude data for the two points
            mode="markers+lines",  # Display as markers and lines
            marker=dict(size=10, color="blue"),  # Marker properties
            line=dict(width=2, color="blue"),  # Line properties
        ),
    ],
    layout=go.Layout(
        title="Kinematic Generation of a Planar Curve",
        hovermode="closest",
        mapbox_style="carto-positron",
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[None],
                    )
                ],
            )
        ],
        mapbox=dict(
            center=dict(lat=np.mean([p0[0], p1[0]]), lon=np.mean([p0[1], p1[1]])),
            zoom=8,
        ),
        margin=dict(l=0, r=0, t=30, b=0),  # Adjust margins if needed
        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
    ),
    frames=[
        go.Frame(
            data=[
                go.Scattermapbox(
                    lat=[xx[k]],  # Latitude data for the current point
                    lon=[yy[k]],  # Longitude data for the current point
                    mode="markers",
                    marker=dict(size=20, color="red", symbol="arrow", angle=angle_deg),
                )
            ]
        )
        for k in range(N)
    ]
)

fig.show(renderer="browser")
