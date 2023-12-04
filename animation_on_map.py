import plotly.graph_objects as go

import numpy as np

# Generate curve data
# Define the two points
p0 = np.array([44.7, -68])
p1 = np.array([44.9, -69])

# p0 = np.array([0, 0])
# p1 = np.array([1, 1])

# Calculate the slope (m) and intercept (c) of the line
m = (p1[1] - p0[1]) / (p1[0] - p0[0])
c = p0[1] - m * p0[0]

# Generate x values for the line
x = np.linspace(p0[0], p1[0], num=20)

# Calculate y values using the equation of the line (y = mx + c)
y = m * x + c

# Generate curve data
xm = np.min(x) - 1
xM = np.max(x) + 1
ym = np.min(y) - 1
yM = np.max(y) + 1

N = 20
xx = np.linspace(p0[0], p1[0], num=N)
yy = m * x + c


# Calculate the angle of the line (in radians)
angle_rad = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
# angle_rad = np.arctan2(p1, p0)

# Convert angle to degrees
angle_deg = np.degrees(angle_rad)+180+45
# if angle_deg > 90:
#     angle_deg += 90
#
# if angle_deg < 0:
#     angle_deg += 270
print(angle_deg)


# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
        title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=[xx[k]],
            y=[yy[k]],
            mode="markers",
            # marker=dict(symbol="arrow", angleref="previous", color="red", size=10))])
            marker=dict(color="red", size=20, symbol="arrow", angle=angle_deg))])

        for k in range(N)]
)

fig.show(renderer="browser")

