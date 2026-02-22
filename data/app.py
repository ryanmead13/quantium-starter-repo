from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('combined_pink_morsel_sales_data.csv')

fig = px.line(df,
              x='date',
              y='sales',
              title='Pink Morsel Sales',
              labels={'date': 'Date', 'sales': 'Sales ($)'},
              range_x=[df['date'].min(), df['date'].max()],
              range_y=[df['sales'].min() - 250, df['sales'].max() + 250])

app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales Data", style={}),
    html.Div(children='''
        A timeline of sales of the pink morsel pre and post price change.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
], style={'text-align': 'center', 'fontFamily':'sans-serif'})

if __name__ == '__main__':
    app.run(debug=True)