import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from datetime import date
import dash_bootstrap_components as dbc

currentDay = dt.now().day
currentMonth = dt.now().month
currentYear = dt.now().year

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


app.layout = html.Div(style={}, className='parent',children=[
    html.H1(style={'display': 'block', 'textAlign': 'center'},
            children="Stock Visualizing and Forecasting App!", className="header"),
    html.Div(className='container', children=[
        html.Div(style={}, children=[
             html.Div(style={'content': '\A'}, children=[
                 html.P("Enter the stock code: "),
                 dcc.Input(
                     placeholder='e.g AAPL (for apple)',
                     type='text',
                     value=''
                 )
             ], className='stockInput'),
             html.Div(style={'display': 'block'}, children=[
                 # Date range picker input
                 dcc.DatePickerRange(
                     id='date_input',
                     min_date_allowed=date(currentYear, currentMonth, currentDay),
                     max_date_allowed=date(2022, 9, 19),
                     initial_visible_month=date(currentYear, currentMonth, currentDay),
                     end_date=date(currentYear, currentMonth, currentDay)
                 )
                 # html.Div(id='output-container-date-picker-range')
                 # html.Br
             ], className='dateinput'),
             html.Div(children=[
                 # Stock price button
                 html.Div(children=[
                     dbc.Button("Stock Price", color="primary", className="mr-1", id='stockprice'),
                     # Indicators button
                     dbc.Button("Indicator", color="success", className="mr-1", id='indicator')
                     # html.Br()
                 ], className='midnav'),
                 # Numner of days forecast input value
                 html.Div(children=[
                     dcc.Input(
                         placeholder='No. of Days',
                         type='number',
                         value='',
                         id='nodays'
                     ),
                     # FOrecast BUtton
                     dbc.Button("Forecast", color="dark", className="mr-1")
             ], className='bottom_nav')])
        ],
             className="nav"),
        html.Div([
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
            className="content")
    ]),
    html.P(children=[
                "Created by ",
                html.A('Tirth Patel', href='https://www.linkedin.com/in/tirth-patel-412b70192')
            ], className="footer")
])

if __name__ == '__main__':
    app.run_server(debug=True)
