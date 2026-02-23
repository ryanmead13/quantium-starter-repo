from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/combined_pink_morsel_sales_data.csv')

app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales Data", style={}),
    html.Div(children='''
        A timeline of sales of the pink morsel pre and post price change.
    '''),
    dcc.Graph(id='sales-graph'),
    html.Div(children=[
        html.H3(children='Region Filter', style={}),
        dcc.RadioItems(['North', 'South', 'East', 'West', 'All'], 'All', id='region-radio',
                   style={'color': 'blue'}, inline=True,
                       inputStyle={'accent-color': 'blue', 'color': 'black'}),],
            ),
], style={'text-align': 'center', 'fontFamily':'sans-serif'})

@callback(Output('sales-graph', 'figure'),
          Input('region-radio', 'value'))
def update_graph(region):
    region = region.lower()
    if region != 'all':
        filtered_df = df[df['region'] == region]
    else:
        filtered_df = df

    fig = px.line(filtered_df,
              x='date',
              y='sales',
              title='Pink Morsel Sales',
              labels={'date': 'Date', 'sales': 'Sales ($)'})
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run(debug=True)