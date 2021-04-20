import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from datetime import date
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server

# REF Plot Figure
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
#
# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )
# dcc.Graph(
#     id='example-graph-2',
#     figure=fig
# )


app.layout = html.Div(style={}, children=[
    html.H1(style={'display': 'block', 'text-align': 'center'}, children="Welcome to the Stock Visualizing and Forecasting App!", className="start"),
    html.Div(style= {'display': 'block'},
        children=[
            html.Div(style= {'content':'\A'},children=[
                html.P("Enter the stock code: "),
                dcc.Input(
                    placeholder='e.g AAPL (for apple)',
                    type='text',
                    value=''
                )
            ]),
            html.Div(style={'display': 'block'}, children=[
                # Date range picker input
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2017, 9, 19),
                    initial_visible_month=date(2017, 8, 5),
                    end_date=date(2017, 8, 25)
                ),
                html.Div(id='output-container-date-picker-range')
                # html.Br
            ]),
            html.Div([
                # Stock price button
                dbc.Button("Stock Price", color="primary", className="mr-1"),
                # Indicators button
                dbc.Button("Indicator", color="success", className="mr-1"),
                html.Br(),
                # Numner of days forecast input value
                dcc.Input(
                    placeholder='No. of Days',
                    type='number',
                    value=''
                ),
                # FOrecast BUtton
                dbc.Button("Submit", color="dark", className="mr-1"),
            ]),
        ],
        className="nav"),
    html.Div(
        [
            html.Div(
                [  # Logo
                    # Company Name
                ],
                className="header"),
            html.Div(  # Description
                id="description", className="decription_ticker"),
            html.Div([
                # Stock price plot
            ], id="graphs-content"),
            html.Div([
                # Indicator plot
            ], id="main-content"),
            html.Div([
                # Forecast plot
            ], id="forecast-content")
        ],
        className="content")])

if __name__ == '__main__':
    app.run_server(debug=True)
