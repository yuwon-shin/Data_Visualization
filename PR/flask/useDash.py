from flask import Flask
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import os


inbodyDf = pd.read_csv(os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'inbody.csv'))
courseDf = pd.read_csv(os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'courses.csv'))

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.cs']

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.title='[Youwon Shin]'

app.layout = html.Div(className='body',children=[

    html.Div(className='header',children=[
        html.H1(className='h1',children='Welcome to YOUWON\'s WORLD!',style={'color':'white'})
    ]),

    html.Div(className='firstDiv',children=[
        html.Div(className='Intro',children=[
            html.H1(className='h1',children='Youwon Shin',style={'color':'#8977ad'}),html.Br(),
            html.P(className='IntroArticle',children=['Hello, I\'m youwon shin.',html.Br(),'I am currently a M.S. student in ',
            html.B(children='Computer Science major'), ' at KAIST and supervised by Prof.Uchin Lee in ',
            html.A(className='a',children='ICLab@KAIST', href="http://ic.kaist.ac.kr/wiki/wiki.cgi?Main"), '.', html.Br(),
            'I received my B.S. degree in ', html.A(className='a',children='Mechanical and Biomedical Engineering', href="http://mbe.ewha.ac.kr/"),
            ' from Ewha Womans University in 2021.', html.Br(),html.Br(),html.Br(),
            html.B(children='Contact: '),
            html.A(className='email',children='youwon.shin@kaist.ac.kr',href="mailto:youwon.shin@kaist.ac.kr")])
        ]),
        html.Div(className='Img', children=[
            html.Img(className='profimg',src= app.get_asset_url('profile.jpg'), style={'alt':'Profile image'})
        ]) 
    ]),

    html.Div(className='secondDiv',children=[
        html.Div(className='leftDiv',children=[
            html.H2(className='h2',children='My Personality Type'),
            html.Div(className='leftChild',children=[
                html.Img(className='mbtiImg',src=app.get_asset_url('ENFJ.png'), style={'alt':'ENFJ'}),
                html.Span(className='MBTI',children=[
                    html.Br(),
                    html.B('E'), 'xtroverted', html.Br(),
                    'I', html.B('N'), 'tution', html.Br(),
                    html.B('F'), 'eelings', html.Br(),
                    html.B('J'), 'udgment'
                ])
            ])
        ]),
        html.Div(className='rightDiv',children=[
            html.H2(className='h2',children='Inbody Trend'),
            html.Div(className='chartbox',children=[
                dcc.Dropdown(
                id="Value-selector",    
                options=[{
                    'label': i,
                    'value': i
                } for i in inbodyDf['Type'].unique()],
                value="All",
                placeholder="Select Type",
                ),
                dcc.Graph(id='inbody-graph')
            ]),    
        ],
        style={
            'width' : '100%',
            'min-width':'35rem'
        })
    ]),

    html.Div(className='thirdDiv',children=[
        html.Div(className='leftDiv',children=[
            html.H2(className='h2',children='Course Schedule (Fall, 2021)'),
            html.Table(className='table1',children=[
                html.Tbody([
                    html.Tr([
                        html.Th(style={'background-color':"#9283ad", 'width':'80px'}),
                        html.Th('MON', style={'background-color':"#9283ad", 'width':'80px'}),
                        html.Th('TUE', style={'background-color':"#9283ad", 'width':'80px'}),
                        html.Th('WED', style={'background-color':"#9283ad", 'width':'80px'}),
                        html.Th('THU', style={'background-color':"#9283ad", 'width':'80px'}),
                        html.Th('FRI', style={'background-color':"#9283ad", 'width':'80px'})
                    ],style={'height':'35px'}),
                    html.Tr([
                        html.Td('9:00-10:30'),html.Td(),html.Td(),html.Td(),html.Td(),html.Td()
                    ]),
                    html.Tr([
                        html.Td('10:30-12:00'),html.Td(),html.Td(['Data', html.Br(),'Visualization']),html.Td(),html.Td(['Data', html.Br(),'Visualization']),html.Td()
                    ]),
                    html.Tr([
                        html.Td('12:00-13:00'),html.Td('~LUNCH TIME~', colSpan=5,style={'background-color': '#d5c9dd','font-weight':'bold'})
                    ]),
                    html.Tr([
                        html.Td('13:00-14:30'),html.Td(['Advanced', html.Br(), 'Data Mining']),html.Td(),html.Td(['Advanced', html.Br(), 'Data Mining']),html.Td(),html.Td()
                    ]),
                    html.Tr([
                        html.Td('14:30-16:00'),html.Td(),html.Td('HCI'),html.Td(),html.Td('HCI'),html.Td()
                    ])
                ])
            ])
        ]),
        html.Div(className='rightDiv',children=[
            html.H2(className='h2',children='How many courses did I take?'),
            html.Div(className='chartbox',children=[
                dcc.Dropdown(
                id="Year-selector",    
                options=[{
                    'label': i,
                    'value': i
                } for i in courseDf['Year'].unique()],
                value="Year",
                placeholder="Select Year"
                ),
                dcc.Graph(id='course-graph')
            ])
        ],
        style={
            'width' : '100%',
            'min-width':'35rem'
        })
    ]),

    html.Div(className='fourthDiv',children=[
        html.Div(className='DivChild',children=[
            html.H2(className='h2',children=['Visitors for last 7 days']),
            html.Table(className='table2',children=[
                html.Tbody([
                    html.Tr([
                        html.Th('MON', style={'background-color':"#dbd4e7", 'width':'90px'}),
                        html.Th('TUE', style={'background-color':"#dbd4e7", 'width':'90px'}),
                        html.Th('WED', style={'background-color':"#dbd4e7", 'width':'90px'}),
                        html.Th('THU', style={'background-color':"#dbd4e7", 'width':'90px'}),
                        html.Th('FRI', style={'background-color':"#dbd4e7", 'width':'90px'}),
                        html.Th('SAT', style={'background-color':"#dbd4e7", 'width':'90px'}),
                        html.Th('SUN', style={'background-color':"#dbd4e7", 'width':'90px'})
                    ]),
                    html.Tr([
                        html.Td('30', style={'width':"#dbd4e7"}),html.Td('12'),html.Td('23'),html.Td('43'),
                        html.Td('21'),html.Td('11'),html.Td('34')
                    ])
                ])
            ])
        ])
    ]),

    html.Div(className='footer',children=[
        html.B('Interactive Computing Lab, School of Computing,KAIST'),
        html.Br(),
        html.I('291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea')
    ])

])

@app.callback(
    Output(component_id='inbody-graph', component_property='figure'),
    [Input(component_id='Value-selector', component_property='value')]
)
def update_inbody_graph(value):
    days = ['2021-07-27', '2021-08-03', '2021-08-12', '2021-09-07']
    if value == "All":
        df = inbodyDf.copy()
    else:
        df = inbodyDf.loc[inbodyDf['Type']==value]
    line1 = go.Scatter(name='Fat', x=days, y=df.loc[df['Type']=='Fat']['Figure'], mode='lines+markers')
    line2 = go.Scatter(name='Skeletal muscles', x=days, y=df.loc[df['Type']=='Skeletal muscles']['Figure'],mode='lines+markers')
    line3 = go.Scatter(name='BMI', x=days, y=df.loc[df['Type']=='BMI']['Figure'],mode='lines+markers')
    line4 = go.Scatter(name='Fat Pect.', x=days, y=df.loc[df['Type']=='Fat Pect.']['Figure'],mode='lines+markers')

    return {
        'data': [line1,line2,line3,line4],
        'layout':
            go.Layout(
                barmode='stack'
            )
        }

@app.callback(
    Output(component_id='course-graph', component_property='figure'),
    [Input(component_id='Year-selector', component_property='value')]
)
def update_course_graph(value):
    if value == "Year":
        df = courseDf[courseDf['Year']==2021]
    else:
        df = courseDf[courseDf['Year']==value]
    grouped_Df = df.groupby(['Semester','Department']).count()
    grouped_Df = grouped_Df.reset_index()
    semesters = ['Spring', 'Fall']
    
    bar1 = go.Bar(name='School of Computing', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='School of Computing']['Course'])
    bar2 = go.Bar(name='General Required', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='General Required']['Course'])
    bar3 = go.Bar(name='Electrical Engineering', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Electrical Engineering']['Course'])
    bar4 = go.Bar(name='Cyber Security', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Cyber Security']['Course'])
    bar5 = go.Bar(name='Computer Engineering', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Computer Engineering']['Course'])
    bar6 = go.Bar(name='Mech/BioMed Engineering', x=semesters, y=grouped_Df.loc[grouped_Df['Department']=='Mech/BioMed Engineering']['Course'])
    
    return {
        'data': [bar1,bar2,bar3,bar4,bar5,bar6],
        'layout':
            go.Layout(
                barmode='stack'
            )
        }

if __name__ == '__main__':
    app.run_server(debug=True)