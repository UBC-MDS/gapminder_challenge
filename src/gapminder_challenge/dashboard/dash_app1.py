import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

# get the csv file in data/raw folder
df = pd.read_csv('../../data/raw/world-data-gapminder_raw.csv')


url_base = '/dash_app1/'


def add_dash(server):
    app = Dash(server=server, url_base_pathname='/dash_app1/')

    app.layout = html.Div([
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(2000, 2018, 1,
                   value=2007,
                   id='my-slider',
                   marks={str(year): str(year) for year in range(2000, 2019)}
                   ),
    ])

    # Set up callbacks/backend
    @app.callback(
        Output('scatter', 'srcDoc'),
        Input('my-slider', 'value'))
    def plot_altair(year):
        chart = alt.Chart(df.query(f'year=={year}')).mark_point(
            filled=True, opacity=0.5).encode(
            alt.X('life_expectancy', scale=alt.Scale(domain=(50, 85))),
            alt.Y('income', scale=alt.Scale(
                type='log', base=10, domain=(1000, 80000))),
            size=alt.Size('population', legend=None),
            tooltip=['country', 'year', 'life_expectancy',
                     'income', 'population'],
            color='region').interactive()
        return chart.to_html()

    return app.server
