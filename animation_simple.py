import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objs as go

# Sample data for points 1, 2, 3, and 4
data1 = {'latitude': [44.7, 44.29706043],
         'longitude': [-68.8, -69.55621676],
         'point': ['Point1', 'Point2']}
data2 = {'latitude': [44.9, 44.09706043],
         'longitude': [-68.6, -67.55621676],
         'point': ['Point3', 'Point4']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Initialize Dash app
app = dash.Dash(__name__)

# Create initial map using Plotly Express
fig = px.scatter_mapbox(df1, lat='latitude', lon='longitude', zoom=6, height=800, width=2000)
fig.update_geos(center=dict(lon=-68.8, lat=44.7))  # Set initial map center
fig.update_layout(mapbox_style="carto-positron")  # Set map style

# Define frames for animation between points 1, 2 and points 3, 4
# frames1 = [{'data': [{'lat': [df1['latitude'][0] + (df1['latitude'][1] - df1['latitude'][0]) * i],
#                       'lon': [df1['longitude'][0] + (df1['longitude'][1] - df1['longitude'][0]) * i]}],
#             'name': f'frame_{i:.2f}'} for i in np.linspace(0, 1, 30)]


frames1 = [{'data': [{'lat': [df1['latitude'][0] + (df1['latitude'][1] - df1['latitude'][0]) * i],
                      'lon': [df1['longitude'][0] + (df1['longitude'][1] - df1['longitude'][0]) * i],
                      'marker': {'color': 'red', 'size': 50, 'symbol': 'circle'}
                      }],
            'name': f'frame_{i:.2f}'} for i in np.linspace(0, 1, 30)]



frames2 = [{'data': [{'lat': [df2['latitude'][0] + (df2['latitude'][1] - df2['latitude'][0]) * i],
                      'lon': [df2['longitude'][0] + (df2['longitude'][1] - df2['longitude'][0]) * i]}],
            'name': f'frame_{i:.2f}'} for i in np.linspace(0, 1, 30)]

# Define line trace between points 1 and 2
line_trace1 = go.Scattermapbox(
    lat=[df1['latitude'][0], df1['latitude'][1]],
    lon=[df1['longitude'][0], df1['longitude'][1]],
    mode='lines+markers',
    line=dict(width=2),
    marker=go.scattermapbox.Marker(size=10),
    text=['Point1', 'Point2']
)
fig.add_trace(line_trace1)

# Define line trace between points 3 and 4
line_trace2 = go.Scattermapbox(
    lat=[df2['latitude'][0], df2['latitude'][1]],
    lon=[df2['longitude'][0], df2['longitude'][1]],
    mode='lines',
    line=dict(width=2),
    marker=go.scattermapbox.Marker(size=10),
    text=['Point3', 'Point4']
)
fig.add_trace(line_trace2)

# Define layout for Dash app
app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=[
            {'label': '2000', 'value': '2000'},
            {'label': '2001', 'value': '2001'}
        ],
        value='2000'
    ),
    dcc.Graph(
        id='map',
        figure=fig
    ),
    dcc.Interval(
        id='interval-component',
        interval=100,
        n_intervals=0
    )
])

# Define callback to update map figure based on dropdown selection and interval
@app.callback(
    Output('map', 'figure'),
    Input('year-dropdown', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_map(selected_year, n):
    if selected_year == '2000':  # For 2000, update map with frames between points 1 and 2
        frame_data = frames1[n % len(frames1)]
        fig['data'][0]['lat'] = frame_data['data'][0]['lat']
        fig['data'][0]['lon'] = frame_data['data'][0]['lon']
        return fig
    elif selected_year == '2001':  # For 2001, update map with frames between points 3 and 4
        frame_data = frames2[n % len(frames2)]
        fig['data'][0]['lat'] = frame_data['data'][0]['lat']
        fig['data'][0]['lon'] = frame_data['data'][0]['lon']
        return fig
    else:
        return go.Figure()  # Return an empty figure if year not selected

if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
