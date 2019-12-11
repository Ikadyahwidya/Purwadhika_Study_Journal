import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Input, Output, State
from sqlalchemy import create_engine

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

engine = create_engine("mysql+mysqlconnector://root:Widya180390@localhost/DB_automotive?host=localhost?port=3306")
conn = engine.connect()
dfAuto=pd.DataFrame(conn.execute('SELECT * FROM auto_imports_ujian').fetchall(),columns=pd.read_csv('auto_imports_ujian.csv').columns)

dropdwn=['All',*[str(i) for i in dfAuto['Fuel-Type'].unique()]]

app.layout = html.Div(children = [
    html.Center(html.H1('Dashboard Specification')),
    html.H1('Ujian Modul 2 Dashboard Auto Imports'),
    html.P('Created by: Ika Dyah Widya Ningrum'),
    dcc.Tabs(value = 'tabs', id = 'tabs-1', children = [
        

        dcc.Tab(label = 'Table', id = 'table', children = [
            html.Center(html.H1('DATAFRAME AUTO IMPORTS')),
            html.Div(className = 'col-6', children=[
                html.P('Fuel-Type'),
                dcc.Dropdown(id= 'table-dropdown', value = 'All',
                    options= [
                        {'label': i, 'value': i} for i in dropdwn
                    ]
                )
            ]),
            html.Div(className = 'col-3', children=[
                html.P('Max Rows:'),
                dcc.Input(
                    id='page-size',
                    type='number',
                    value=10,
                    min=3,max=20,step=1
                )
            ]),
            html.Div(className = 'col-12', children = [
                html.Button(id='Search', n_clicks=0, children='Search',style={
                    'margin-top':'14px',
                    'margin-bottom':'14px'})
            ]),
            html.Div(id='div-table',className = 'col-12', children = [
                dash_table.DataTable(
                    id= 'dataTable',
                    data= dfAuto.to_dict('records'),
                    columns= [{'id': i, 'name': i} for i in dfAuto.columns],
                    page_action= 'native',
                    page_current= 0,
                    page_size = 10,
                    style_table={'overflowX': 'scroll'}
                )
            ])
        ]), 
        
        dcc.Tab(label = 'Bar Chart', id = 'bar', children = [
            html.Div(className = 'col-12', children = [
                html.Div(className = 'row', children = [
                    html.Div(className = 'col-4',children= [
                        html.P(f'Y1'),
                        dcc.Dropdown(id= f'y-axis-1', value = f'Wheel-Base',
                            options= [
                                {'label': i, 'value': i} for i in dfAuto.select_dtypes('number').columns
                            ]
                        )
                    ]),
                    html.Div(className = 'col-4',children= [
                        html.P(f'Y2'),
                        dcc.Dropdown(id= f'y-axis-2', value = f'Height',
                            options= [
                                {'label': i, 'value': i} for i in dfAuto.select_dtypes('number').columns
                            ]
                        )
                    ]),
                    html.Div(className = 'col-4',children= [
                        html.P(f'X'),
                        dcc.Dropdown(id= f'y-axis-3', value = f'Drive-Wheels',
                            options= [
                                {'label': i, 'value': i} for i in ['Drive-Wheels','Engine-Location','Engine-Type']
                            ]
                        )
                    ])
                ]),
                html.Div(children= [dcc.Graph(
                    id = 'contoh-graph-bar',
                    figure={'data' : [{
                        'x': dfAuto['Drive-Wheels'],
                        'y': dfAuto['Wheel-Base'],
                        'type': 'bar',
                        'name': 'Wheel-Base'
                    },{
                        'x': dfAuto['Drive-Wheels'],
                        'y': dfAuto['Height'],
                        'type': 'bar',
                        'name': 'Height'
                    }],
                        'layout': {'title': 'Bar Chart'}
                    }
                )])
            ])
        ]),
    
        dcc.Tab(label = 'Scatter Chart', id = 'scatter', children = [
        html.Div(children = dcc.Graph(
            id = 'graph-scatter',
            figure = {'data':[go.Scatter(
                x= dfAuto[dfAuto['Drive-Wheels']==i]['Horsepower'],
                y= dfAuto[dfAuto['Drive-Wheels']==i]['Price'],
                text= dfAuto[dfAuto['Drive-Wheels']==i]['Make'],
                mode='markers',
                name= f'{i}'    
            ) for i in dfAuto['Drive-Wheels'].unique()
            ],
                'layout':go.Layout(
                    xaxis= {'title':'Horsepower'},
                    yaxis = {'title' : 'Price'},
                    hovermode = 'closest'
                )
            }
        ),className = 'col-12')
    ]),

    dcc.Tab(label = 'Pie Chart', id = 'tab-dua', children = [
        html.Div(className = 'col-4',children= [
            html.P('Select value'),
            dcc.Dropdown(id= f'pie-dropdown', value = 'Length',
                options= [
                    {'label': i, 'value': i} for i in dfAuto.select_dtypes('number').columns
                ]
            )
        ]),
        html.Div(className = 'col-12', children = dcc.Graph(
            id = 'pie-chart',
            figure= {'data' : [go.Pie(
                labels=list(i for i in dfAuto['Fuel-System'].unique()),
                values=list(dfAuto.groupby('Fuel-System').mean()['Length'])
            )
            ], 'layout': {'title': 'Mean Pie Chart'},}
        ))
    ])
    
    ],
        content_style = {
            'fontFamily': 'Arial',
            'borderBottom': '1px solid #d6d6d6',
            'borderRight': '1px solid #d6d6d6',
            'borderLeft': '1px solid #d6d6d6',
            'padding': '44px'
        },
        className = 'row'
    )
], 
    style={
        'maxwidth': '1200px', 'margin': '0 auto'
    }
)

@app.callback(
    Output(component_id= 'contoh-graph-bar', component_property= 'figure'),
    [Input(component_id=f'y-axis-{i}', component_property='value') for i in range(1,4)]
)
def create_graph_bar(y1,y2,x):
    figure={'data' : [{
        'x': dfAuto[x],
        'y': dfAuto[y1],
        'type': 'bar',
        'name': y1
    },{
        'x': dfAuto[x],
        'y': dfAuto[y2],
        'type': 'bar',
        'name': y2
    }]
        
    }
    return figure

@app.callback(
    Output(component_id= 'pie-chart', component_property= 'figure'),
    [Input(component_id=f'pie-dropdown', component_property='value')]
)
def create_pie_chart(pie):
    figure= {'data' : [go.Pie(
            labels=list(i for i in dfAuto['Fuel-System'].unique()),
            values=list(dfAuto.groupby('Fuel-System').mean()[pie])
        )
        ], 'layout': {'title': 'Mean Pie Chart'}
    }
    return figure

@app.callback(
    Output(component_id= 'dataTable', component_property= 'data'),
    [Input(component_id='Search', component_property='n_clicks')],
    [State(component_id='table-dropdown',component_property='value')]
)

def update_data(n_clicks,fuel_type):
    if fuel_type == 'All':
        df = dfAuto.to_dict('records')
    else:
        df = dfAuto[dfAuto['Fuel-Type']==fuel_type].to_dict('records')
    return df

@app.callback(
    Output(component_id= 'dataTable', component_property= 'page_size'),
    [Input(component_id='Search', component_property='n_clicks')],
    [State(component_id='page-size',component_property='value')]
)

def update_data(n_clicks,size):
    return size

if __name__ == '__main__':
    app.run_server(debug=True)
