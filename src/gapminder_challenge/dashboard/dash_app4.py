import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

# Read in the raw data and subset the data for analysis
df = pd.read_csv('../../data/raw/world-data-gapminder_raw.csv')
df = df[["country", "year", "population", "region", 'income_group', "income"]]

url = '/dash_app4/'

def add_dash(server):
    """
    It creates a Dash app that plots a scatter plot of income per capita by 
        year from 1901 to 2018
    
    :param server: The Flask app object
    :return: A Dash server
    """
    app = Dash(server=server, url_base_pathname=url)

    app.layout = html.Div([
        html.Iframe(
            id='main_chart',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.RangeSlider(min=1901, max=2018,
                   value=[1901, 2018],
                   id='year_slider',
                   marks={str(year): str(year)
                          for year in range(1901, 2018, 10)}
                   )
        #            ,
        # dcc.Dropdown(df_year.region.unique(),
        #              id='dropdown',
        #              value=['Europe', 'Asia', 'Americas', 'Africa' , 'Oceania'],
        #              multi=True)
    ])

    # Set up callbacks/backend
    @app.callback(
    Output('main_chart', 'srcDoc'),
    Input('year_slider', 'value')
    # ,
    # Input('dropdown', 'value')
    )
    def plot_altair(year_slider):
        """
        The function
        :param 
        :param 
        :return: The Altair chart is being returned.
        """
        df_by_year = df.groupby(["year"]).sum()
        df_by_year["income_per_capita"] = df_by_year["income"] * 1000000 / df_by_year["population"]
        df_by_year = df_by_year.reset_index()
        chart = alt.Chart(df_by_year.query(
            f'year>={year_slider[0]} and year<={year_slider[1]}')
            ).mark_point(opacity=0.5
            ).encode(alt.X('year', title='Year', 
            scale=alt.Scale(domain=[year_slider[0], year_slider[1]])),
                    alt.Y('income_per_capita', title='Income Per Capita'))
        # text = chart.mark_text(
        #     align='left',
        #     baseline='middle',
        #     dx=3  # Nudges text to right so it doesn't appear on top of the bar
        # ).encode(
        #     text='co2_per_capita:Q'
        # )

        return (chart).to_html()

    return app.server