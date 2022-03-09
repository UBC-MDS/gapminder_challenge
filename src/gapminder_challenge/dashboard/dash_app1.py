import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

df = pd.read_csv('../../data/raw/world-data-gapminder_raw.csv')
df_year = df.groupby(['year', 'region']).agg({'co2_per_capita': 'sum'}).reset_index()

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
            id='bar_chart',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(1914, 2014, 1,
                   value=1914,
                   id='slider',
                   marks=None,
                   tooltip={"placement": "bottom", }
                   ),
        dcc.Dropdown(df_year.region.unique(),
                     id='dropdown',
                     value=['Europe', 'Asia', 'Americas', 'Africa' , 'Oceania'],
                     multi=True),
    ])

    # Set up callbacks/backend
    @app.callback(
    Output('bar_chart', 'srcDoc'),
    Input('slider', 'value'),
    Input('dropdown', 'value'))
    def plot_altair(year, regions):
        """
        The function takes in a year, countries and 
        outputs the Altair chart for that year

        :param year: The year to plot
        :param countries: The countries to plot
        :return: The Altair chart is being returned.
        """
        chart = alt.Chart(df_year.query(f'year=={year} and region=={regions}'), title=f'CO2 per Capita in {year}',).mark_bar(
            opacity=0.5).encode(
            alt.X('co2_per_capita', title='CO2 per Capita'),
            alt.Y('region', sort='-x', title='Region'),
            tooltip=['region', 'year', 'co2_per_capita', ],
            color='region').interactive()

        # text = chart.mark_text(
        #     align='left',
        #     baseline='middle',
        #     dx=3  # Nudges text to right so it doesn't appear on top of the bar
        # ).encode(
        #     text='co2_per_capita:Q'
        # )

        return (chart).to_html()

    return app.server
