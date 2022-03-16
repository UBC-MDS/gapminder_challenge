import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

df = pd.read_csv('../../data/raw/world-data-gapminder_raw.csv')  # local run
# df = pd.read_csv('data/raw/world-data-gapminder_raw.csv')  # heroku deployment


url = '/dash_app2/'


def add_dash(server):
    """
    It creates a Dash app that plots a line chart of children per woman from gapminder dataset
    with 2 widgets : rangeslider for years and dropdown for filter
    
    :param server: The Flask app object
    :return: A Dash server
    """
    app = Dash(server=server, url_base_pathname=url)

    app.layout = html.Div([
        html.Iframe(
            id='line_children',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        html.Label([
            'Zoom in years: ',
            dcc.RangeSlider(1918, 2018, 10, value=[1918, 2018],  id='year_range_slider',
                            marks={str(year): str(year) for year in range(1918, 2028, 10)}),
        ]),
        html.Label([
            'See breakdown number by: ',
            dcc.Dropdown(options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'Income Group', 'value': 'income_group'},
                {'label': 'Region', 'value': 'region'}
            ],
                value='', id='filter_dropdown')
        ]),
        html.Div(id="data_card_2", **{'data-card_2_data': []})
    ])

    # Set up callbacks/backend
    @app.callback(
        Output('line_children', 'srcDoc'),
        Input('year_range_slider', 'value'),
        Input('filter_dropdown', 'value')
    )
    def update_line(year_range_slider, filter_dropdown):
        """
        The function takes in a year range and filter option and outputs the line chart per children 
        for that year range with the filter
        :param year_range_slider: The year range to plot
        :param filter_dropdown: The filter to plot
        :return: The Altair chart is being returned.
        """
        filter = filter_dropdown
        title_params = alt.TitleParams("Average Number of Children", subtitle=[
                                       "Click on legend entries to mute the corresponding lines"])

        if filter == "all" or filter == '':
            df_by_year = df.groupby(["year"]).mean()
            df_by_year = df_by_year.reset_index()
            chart = alt.Chart(df_by_year.query(f'year>={year_range_slider[0]} and year<={year_range_slider[1]}'),
                              title="Average Number of Children").mark_line().encode(
                y=alt.Y("children_per_woman", title="Children per woman"),
                x=alt.X("year", title="Year"),
                tooltip=['year', 'children_per_woman']).interactive()
        else:
            # group by filter field and then year to get the average
            df_by_year = df.groupby([filter, "year"]).mean()
            df_by_year = df_by_year.reset_index()

            # add interactive click
            click = alt.selection_multi(fields=[filter], bind='legend')
            chart = alt.Chart(df_by_year.query(f'year>={year_range_slider[0]} and year<={year_range_slider[1]}'),
                              title=title_params).mark_line().encode(
                y=alt.Y("children_per_woman", title="Children per woman"),
                x=alt.X("year", title="Year"),
                color=filter,
                opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
                tooltip=['year', 'children_per_woman']).interactive().add_selection(click)

        return chart.to_html()

    @app.callback(
        Output('data_card_2', 'data-card_2_data'),
        Input('filter_dropdown', 'value'))
    def get_data(filter_dropdown="income_group"):
        if filter_dropdown == '':
            filter_dropdown = 'income_group'
        df_by_year = df.groupby([filter_dropdown, "year"]).mean()
        df_viz = df_by_year.reset_index()
        df_viz = df_viz[[filter_dropdown, 'year', 'children_per_woman']]
        df_viz = df_viz.to_json()
        return (df_viz)

    return app.server
