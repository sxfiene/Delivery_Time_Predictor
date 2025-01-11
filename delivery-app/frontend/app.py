import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import requests

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        'fontFamily': 'Arial, sans-serif',
        'margin': '0 auto',
        'maxWidth': '800px',
        'padding': '20px',
        'backgroundColor': '#F9FAFB',
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
        'borderRadius': '10px'
    },
    children=[
        html.H1(
            "Delivery Time Predictor",
            style={
                'textAlign': 'center',
                'color': '#333',
                'marginBottom': '20px',
                'fontSize': '28px',
                'fontWeight': '600'
            }
        ),
        html.Div(
            style={
                'backgroundColor': '#FFFFFF',
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                'marginBottom': '20px'
            },
            children=[
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Distance (km)", style={'fontWeight': '500'}),
                        dcc.Input(
                            id='distance',
                            type='number',
                            min=0,
                            step=0.1,
                            value=6,
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Weather", style={'fontWeight': '500'}),
                        dcc.Dropdown(
                            id='weather',
                            options=[
                                {'label': 'Clear', 'value': 'Clear'},
                                {'label': 'Rainy', 'value': 'Rainy'},
                                {'label': 'Snowy', 'value': 'Snowy'},
                                {'label': 'Foggy', 'value': 'Foggy'},
                                {'label': 'Windy', 'value': 'Windy'},
                            ],
                            value='Clear',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Traffic Level", style={'fontWeight': '500'}),
                        dcc.Dropdown(
                            id='traffic',
                            options=[
                                {'label': 'Low', 'value': 'Low'},
                                {'label': 'Medium', 'value': 'Medium'},
                                {'label': 'High', 'value': 'High'}
                            ],
                            value='Low',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Time of Day", style={'fontWeight': '500'}),
                        dcc.Dropdown(
                            id='time_of_day',
                            options=[
                                {'label': 'Morning', 'value': 'Morning'},
                                {'label': 'Afternoon', 'value': 'Afternoon'},
                                {'label': 'Evening', 'value': 'Evening'},
                                {'label': 'Night', 'value': 'Night'}
                            ],
                            value='Afternoon',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Vehicle Type", style={'fontWeight': '500'}),
                        dcc.Dropdown(
                            id='vehicle',
                            options=[
                                {'label': 'Scooter', 'value': 'Scooter'},
                                {'label': 'Bike', 'value': 'Bike'},
                                {'label': 'Car', 'value': 'Car'}
                            ],
                            value='Scooter',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Preparation Time (min)", style={'fontWeight': '500'}),
                        dcc.Input(
                            id='preparation_time',
                            type='number',
                            min=0,
                            step=1,
                            value=1,
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Div(
                    style={'marginBottom': '15px'},
                    children=[
                        html.Label("Courier Experience (yrs)", style={'fontWeight': '500'}),
                        dcc.Input(
                            id='courier_experience',
                            type='number',
                            min=0,
                            step=0.1,
                            value=1,
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'border': '1px solid #CCC',
                                'borderRadius': '5px',
                                'marginBottom': '10px'
                            }
                        ),
                    ]
                ),
                html.Button(
                    'Predict Delivery Time',
                    id='predict_button',
                    n_clicks=0,
                    style={
                        'width': '100%',
                        'padding': '10px',
                        'backgroundColor': '#007BFF',
                        'color': 'white',
                        'border': 'none',
                        'borderRadius': '5px',
                        'cursor': 'pointer',
                        'fontWeight': '600',
                        'fontSize': '16px'
                    }
                )
            ]
        ),
        dcc.Loading(
            id="loading-spinner",
            type="circle",
            children=[
                html.Div(
                    id='prediction_output',
                    style={
                        'textAlign': 'center',
                        'fontSize': '24px',
                        'color': '#007BFF',
                        'marginTop': '20px',
                        'fontWeight': '500'
                    }
                )
            ]
        )
    ]
)

@app.callback(
    Output('prediction_output', 'children'),
    Input('predict_button', 'n_clicks'),
    State('distance', 'value'),
    State('weather', 'value'),
    State('traffic', 'value'),
    State('time_of_day', 'value'),
    State('vehicle', 'value'),
    State('preparation_time', 'value'),
    State('courier_experience', 'value')
)
def update_output(n_clicks, distance, weather, traffic, time_of_day, vehicle, preparation_time, courier_experience):
    if n_clicks > 0:
        payload = {
            "Distance_km": distance,
            "Weather": weather,
            "Traffic_Level": traffic,
            "Time_of_Day": time_of_day,
            "Vehicle_Type": vehicle,
            "Preparation_Time_min": preparation_time,
            "Courier_Experience_yrs": courier_experience
        }
        
        response = requests.post("http://localhost:8000/predict/", json=payload)
        
        if response.status_code == 200:
            prediction = response.json().get("predicted_delivery_time")
            return f"Predicted Delivery Time: {prediction} minutes"
        else:
            return "Error in prediction"

if __name__ == '__main__':
    app.run_server(debug=True)
