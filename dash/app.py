import dash
import dash_html_components as html
import dash_core_components as dcc

from layouts.gan import ganLayout
from layouts.nlp import nlpLayout

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Tabs(id='tabs', value='speech', children=[
        dcc.Tab(label='Speech', style={'color': 'black'}, value='speech'),
        dcc.Tab(label='GAN', style={'color': 'black'}, value='gan'),
    ]),
    html.Div(id='content')
])

@app.callback(Output('content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'speech':
        return nlpLayout
    elif tab == 'gan':
        return ganLayout

if __name__ == '__main__':
    app.run_server(debug=True)
