import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 1, 100)
y = 0.5 * np.ones(100)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    mode='lines',
    line=dict(color='royalblue', width=3)
))

fig.add_trace(go.Scatter(
    x=[0],
    y=[0.5],
    mode='markers',
    marker=dict(size=10, color='darkred', symbol='arrow-right')
))

frames = [dict(data=[dict(type='scatter',  
                   x=[t],
                   y=[0.5])],
              traces=[1],
              name='frame{}'.format(t))
          for t in np.linspace(0, 1, 100)]

fig.frames = frames 

fig.update(frames=frames)

fig.layout.updatemenus = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 100, "redraw": True},  
                                "fromcurrent": True, 
                                "transition": {"duration": 50}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": True},  
                          }],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 70},
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",  
        "y": 0,
        "yanchor": "top"
    }
]
    
fig.show(renderer="browser")
