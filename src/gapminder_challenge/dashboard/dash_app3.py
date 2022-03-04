import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

df = pd.read_csv('../../data/raw/world-data-gapminder_raw.csv')
url = '/dash_app3/'

def add_dash(server):
    """
    It creates a Dash app that plots a line chart of life expectancy from gapminder dataset
    with 2 widgets : rangeslider for years and dropdown for sub-region filter
    
    :param server: The Flask app object
    :return: A Dash server
    """
    app = Dash(server=server, url_base_pathname=url)

    app.layout = html.Div([
        html.Iframe(
            id='line_life_exp',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            html.Label([
                'Zoom in years: ',
                dcc.RangeSlider(1918, 2018, 10, value=[1918, 2018], id='q3_year_range_slider',
                    marks={str(year): str(year) for year in range(1918, 2028,10)}),
            ]),
            html.Label([
                'Select sub-region to explore: ',
                    dcc.Dropdown(
                        options = [{'label': 'All', 'value': 'All'}] +
                    [{'label': i, 'value': i} for i in df['sub_region'].unique()],
                    value='Sub-Saharan Africa', id='q3_filter_dropdown')
             ])
    ])

    # Set up callbacks/backend
    @app.callback(
        Output('line_life_exp', 'srcDoc'),
        Input('q3_year_range_slider', 'value'),
        Input('q3_filter_dropdown', 'value')
        )
    def update_line(year_range_slider, filter_dropdown):
        """
        The function takes in a year range and filter option and outputs the line chart for life exp 
        for that year range with the sub-region filter
        :param year_range_slider: The year range to plot
        :param filter_dropdown: The filter to plot
        :return: The Altair chart is being returned.
        """
        filter = filter_dropdown
        if filter=="All" or filter=="":
            df_q3 = df.groupby(['sub_region', 'year']).mean()
            df_q3 = df_q3.reset_index()
            chart = alt.Chart(df_q3.query(f'year>={year_range_slider[0]} and year<={year_range_slider[1]}'), 
                title="Average Life Expectancy").mark_line().encode(
                y=alt.Y("life_expectancy", title="Average Life Expectancy (Years)"),
                x=alt.X("year", title="Year"),
               color=alt.Color('sub_region', legend=None),
                tooltip=['year', 'life_expectancy']).interactive()
        else: 
            # only show the line for selected filter region
            df_q3 = df[df['sub_region']==filter]
            df_q3 = df_q3.groupby(['sub_region', 'year']).mean()
            df_q3 = df_q3.reset_index()  

            chart = alt.Chart(df_q3.query(f'year>={year_range_slider[0]} and year<={year_range_slider[1]}'), 
                title="Average Life Expectancy").mark_line().encode(
                y=alt.Y("life_expectancy", title="Average Life Expectancy (Years)"),
                x=alt.X("year", title="Year"),
                color=alt.Color('sub_region', legend=None),
                tooltip=['year', 'life_expectancy']).interactive()
        
        return chart.to_html()

    return app.server
