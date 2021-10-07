from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.cs']

server = Flask(__name__) # Dash uses Flask as a server
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash',
            style={'textAlign':'center'}),
    html.Div(children='''
    Dash: A web application framework for Python'''),

    # graph -> dash core component
    dcc.Graph(
        id='city_graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y':[3, 3, 2],'type': 'bar', 'name':'Seoul'},
                {'x': [1, 2, 3], 'y':[2, 3, 5],'type': 'bar', 'name':'Daejeon'},
                {'x': [1, 2, 3], 'y':[1, 2, 4],'type': 'bar', 'name':'Busan'}
             ],
             'layout': {
                'title': 'Korea City'
             }

        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True) # Run flask server