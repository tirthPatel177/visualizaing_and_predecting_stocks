import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
from datetime import date
import dash_bootstrap_components as dbc
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


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
        html.Div(children=[
             html.Div(style={'content': '\A'}, children=[
                 html.P(style={'margin-left': '8%', 'margin-right':'8%'} ,children="Enter the stock code: "),
                 html.Div(children=[
                     dcc.Input(
                         placeholder='e.g AAPL (for apple)',
                         type='text',
                         value='',
                         id='stockName'
                     ),
                     dbc.Button("Submit", color="primary", className="mr-1", id='stockNameSubmit', n_clicks=0)
                 ], className='start_nav')
             ], className='start_external'),
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
        html.Div(children=[
            # html.H1("This is for testing sdngsednvd  afnenv esnjesg esgnes segsebs"),
            html.Div(
                [  # Logo
                    html.H2(id='company_name', children=[]),
                    html.Img(id='company_logo', children='')
                    # Company Name
                ],
                className="out-header", id='out-header'),
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
    ]
             ),
    html.P(children=[
                "Created by ",
                html.A('Tirth Patel', href='https://www.linkedin.com/in/tirth-patel-412b70192')
            ], className="footer")
])


@app.callback([
        Output('company_name', 'children'),
        Output('description', 'children'),
        Output('company_logo', 'children')
    ],[
        Input('stockNameSubmit', 'n_clicks'),
        State('stockName', 'value')
    ]
)
def company_info(n_clicks, name):
    ticker = yf.Ticker(name)
    inf = ticker.info
    df = pd.DataFrame().from_dict(inf, orient="index").T
    # print(n_clicks)
    company_name = df['shortName'][0]
    description = df['longBusinessSummary'][0]
    logo = df['logo_url'][0]
    print(logo)
    # return # df's first element of 'longBusinessSummary', df's first element value of 'logo_url', df's first element value of 'shortName'
    return company_name, description, logo

if __name__ == '__main__':
    app.run_server(debug=True)
