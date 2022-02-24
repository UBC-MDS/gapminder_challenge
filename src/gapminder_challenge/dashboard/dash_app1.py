import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

df = pd.read_csv('../../data/raw/world-data-gapminder_raw.csv')
url = '/dash_app1/'

def add_dash(server):
    """
    It creates a Dash app that plots a bubble plot of life expectancy vs income
        for a given year.
    
    :param server: The Flask app object
    :return: A Dash server
    """
    app = Dash(server=server, url_base_pathname=url)

    app.layout = html.Div([
        html.Iframe(
            id='bubble',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(2000, 2018, 2,
                   value=2008,
                   id='my-slider',
                   marks={str(year): str(year) for year in range(2000, 2019,2)}
                   ),
    ])

    # Set up callbacks/backend
    @app.callback(
        Output('bubble', 'srcDoc'),
        Input('my-slider', 'value'))
    def plot_altair(year):
        """
        The function takes in a year and outputs the Altair chart for that year

        :param year: The year to plot
        :return: The Altair chart is being returned.
        """
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
