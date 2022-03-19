import pandas as pd
from dash import Dash, html, dcc, Input, Output
import altair as alt

# Read in the raw data and subset the data for analysis
# df = pd.read_csv('../../data/raw/combined-data-for-GDP-per-cap.csv')  # local run
# heroku deployment
df = pd.read_csv('data/raw/combined-data-for-GDP-per-cap.csv')
df = df.rename(columns={"GDP total": "income"})

# Define constant values
YEAR_MIN = 1960
YEAR_MAX = 2018
YEAR_INTERVAL = 10
REGIONS = df["region"].unique()
COUNTRIES = df["country"].unique()
url = '/dash_app4/'


def add_dash(server):
    """
    It creates a Dash app that plots a scatter plot of income per capita by 
        year for the chosen countries, regions, and income groups.
    
    :param server: The Flask app object
    :return: A Dash server
    """
    app = Dash(server=server, url_base_pathname=url)

    app.layout = html.Div([
        html.Iframe(
            id='main_chart',
            style={'border-width': '0', 'width': '550px', 'height': '400px', 'display': 'block',
                   'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Label([
            'Zoom in Years: ',
            dcc.RangeSlider(min=YEAR_MIN, max=YEAR_MAX, step = 1,
                            value=[YEAR_MIN, YEAR_MAX],
                            id='year_slider',
                            marks={str(year): str(year)
                            for year in range(YEAR_MIN, YEAR_MAX, YEAR_INTERVAL)},
                            tooltip={"placement": "bottom", "always_visible": True}
            )
        ]),
        html.Label([
            'Filter by Geographic Region: ',
            dcc.Dropdown(id="region_dropdown",
                         value="",
                         options=REGIONS,
                         multi=True)
        ]),
        html.Div(id="data_card_4", **{'data-card_4_data': []})
    ])

    # Set up callbacks/backend
    @app.callback(
        Output('main_chart', 'srcDoc'),
        Input('year_slider', 'value'),
        Input('region_dropdown', 'value')
    )
    def plot_altair(year_slider, region_dropdown):
        """
        The function
        :param year_slider: The year range to plot
        :param region_selector: Regions to filter by
        :param inc_group_dropdown: Income groups to filter by
        :return: The Altair chart is being returned.
        """
        if region_dropdown == "":
            df_by_year = df.groupby(["year"]).sum()
            df_by_year["income_per_capita"] = round(
                df_by_year["income"] / df_by_year["population"], 1)
            df_by_year = df_by_year.reset_index()
            chart = alt.Chart(df_by_year.query(
                f'year>={year_slider[0]} and year<={year_slider[1]}'),
                title="Income Per Capita Has Been Rising"

                ).mark_line(point=alt.OverlayMarkDef(color="blue", opacity=0.3)
                ).encode(
                    alt.X('year', title='Year', scale=alt.Scale(domain=[year_slider[0], year_slider[1]], round=True)),
                    alt.Y('income_per_capita', title='Income Per Capita (in 2017 US$)'),
                    strokeWidth=alt.value(3),
                    tooltip = ["year", "income_per_capita"]).interactive()
        else:
            df_subset_region = df[df.region.isin(region_dropdown)]
            df_by_year = df_subset_region.groupby(["region", "year"]).sum()
            df_by_year["income_per_capita"] = round(
                df_by_year["income"] / df_by_year["population"], 1)
            df_by_year = df_by_year.reset_index()
            chart = alt.Chart(df_by_year.query(
                f'year>={year_slider[0]} and year<={year_slider[1]}'),
                title="Income Per Capita Has Been Rising"
                ).mark_line(point=alt.OverlayMarkDef(color="blue", opacity=0.5)
                ).encode(
                    alt.X('year', title='Year', scale=alt.Scale(domain=[year_slider[0], year_slider[1]], round=True)),
                    alt.Y('income_per_capita', title='Income Per Capita (in 2017 US$)'),
                    alt.Color("region", title = "Region"),
                    strokeWidth=alt.value(3),
                    tooltip = ["year", "income_per_capita"])


        return (chart).to_html()

    @app.callback(
        Output('data_card_4', 'data-card_4_data'),
        Input('region_dropdown', 'value'))
    def get_data(regions=["Western Europe", "Southern  Asia", "Northern America"]):
        if regions == "":
            regions = ["Europe", "Asia", "Americas", "Africa", "Oceania"]
        # df_subset_region = df[df.region.isin(regions)]
        df_subset_region = df.query(f'region=={regions}')
        df_by_year = df_subset_region.groupby(["region", "year"]).sum()
        df_by_year["income_per_capita"] = round(
            df_by_year["income"] / df_by_year["population"], 1)
        df_by_year = df_by_year.reset_index()
        df_viz = df_by_year[['region', 'year', 'income_per_capita']]
        df_viz = df_viz.to_json()
        return (df_viz)

    return app.server
