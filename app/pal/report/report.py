"""Instantiate the Report Dash application.
"""

import dash
from dash import dcc
from dash import html
from dash import dash_table

from .data import read_stats
from .layout import html_layout


def init_report(server):
    """Create a Plotly Dash dashboard.

    :param server: Flask server.
    :type server: Flask
    :returns: Dash app server.
    :rtype: Dash
    """

    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix=u"/report/",
        external_stylesheets=[
            u"/static/dist/css/styles.css",
            u"https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            html.Div(
                children=create_data_table(
                    read_stats().dropna(),
                    u"database-table-stats"
                )
            )
        ],
        id=u"dash-container",
    )
    return dash_app.server


def create_data_table(df, id):
    """Create Dash datatable from Pandas DataFrame.

    DEMO
    """

    table = dash_table.DataTable(
        id=id,
        columns=[{u"name": i, u"id": i} for i in df.columns],
        data=df.to_dict(u"records"),
        fixed_rows={'headers': True},
        sort_action=u"native",
        sort_mode=u"native",
        page_size=5,
        style_header={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'minWidth': 95, 'maxWidth': 95, 'width': 95,
        }
    )
    return table
