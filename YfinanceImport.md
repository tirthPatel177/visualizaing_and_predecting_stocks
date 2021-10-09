import yfinance as yf

import pandas as pd

import plotly.graph_objs as go

import plotly.express as px

Make callback functions to update the empty divisions (.Div) we created in the basic web layout previously(for company information, stock graph and indicator graph ). Dash's callback functions are called whenever an input component's property changes. List out the Output along with their respective IDs and property of the components you want to change. After that list the Input along with their IDs and property of the components which will be used as a trigger for the change in Output components. You may also enlist State to just use the component values without using them as a trigger. You may refer to the code example below.

@app.callback([
    Output("component-id-1", "property"),
    Output(# Output of component-id-2),
    ],
  [Input(# Input of component-id-2)],
  [State("component-id-4", "property")])
def update_data(arg1, arg2):  # input parameter(s)
    # your function here
    return output1, output2

In the first callback function, use the input field (for stock code) and submit buttons as State and Input components respectively. For the Output component use the first empty Div you had created in Task 2. Use the yfinance library's Ticker function to fetch the company info and return it from the first callback function (you may refer to the code snippet below)

ticker = yf.Ticker(val)
inf = ticker.info
df = pd.DataFrame().from_dict(inf, orient="index").T
return # df's first element of 'longBusinessSummary', df's first element value of 'logo_url', df's first element value of 'shortName'

For making the second callback function, use the date range picker's start date, end date and also the stock price button as Input components. For the Output component use the second empty Div we had created in Task 2. You can download the stock price history with the download function of the yfinance library. We get a DataFrame in return. You can pass that DataFrame to a user defined function (which we will make) that returns the required plot (using plotly library). Finally, that plot can be returned from our callback function as a Dash Core Component Graph. You may refer to the code examples below.

df = yf.download(# input parameter, start_date str, end_date str )
df.reset_index(inplace=True)
fig = get_stock_price_fig(df)
return # plot the graph of fig using DCC function

User defined function for stock price graph generation from a given DataFrame

def get_stock_price_fig(df):
    fig = px.line(df,
                  x= # Date str,
                  y= # list of 'Open' and 'Close',
                  title="Closing and Opening Price vs Date")
    return fig

The third callback will be for generating our indicator graph. You may use estimated moving average (EMA) for it. The callback function for it will be similar to the second one. However, we need to make a new user defined function which will return an EMA plot over time. You can refer to the code given below

def get_more(df):
    df['EWA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    fig = px.scatter(df,
                    x= # Date str,
                    y= # EWA_20 str,
                    title="Exponential Moving Average vs Date")

    fig.update_traces(mode= # appropriate mode)
    
    return fig

Till here we have completed the app.py file, i.e. the web layout and server functions are in place and hence the app is partially functional (prediction feature is yet to be implemented).
