import dash
import dash_core_components as dcc
import dash_html_components as html
import flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__,
                     server=app,
                     url_base_pathname='/',
                     external_stylesheets=external_stylesheets)

dash_app.layout = html.Div([
    html.Div(
        [
            html.H1(
                "Sample Dash",
                style={
                    'text-align':'center',
                }
            ),
        ],
    )
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
