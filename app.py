##=============================================
## Master of Computing and Innovation Project
## Student: Ruonan Fu, Tian Qiu, Vandit Gajjar
## Student ID: a1785307, a1777071, a1779153
## Semester: 1
## Year: 2021
## Milestone-1 Codebase
##=============================================

#################################################
####### Drop-down menu for individual generations
#################################################

#Importing utilites
import dash
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

app = dash.Dash(__name__)
server = app.server

#Creating dataframe
df = pd.read_csv("https://github.com/Vanditg/MCI-tmp/blob/main/datasheet_1.csv")


#Extracting different datapoints
SampleNames = df["SampleNames"].tolist()

Gen0 = df["gen0"].tolist()
Gen1 = df["gen1"].tolist()
Gen2 = df["gen2"].tolist()
Gen3 = df["gen3"].tolist()
Gen4 = df["gen4"].tolist()
Gen5 = df["gen5"].tolist()
Gen6 = df["gen6"].tolist()
Gen7 = df["gen7"].tolist()
Gen8 = df["gen8"].tolist()

totalCells = df["TotalCells"].tolist()

timeHrs = df["TimeHrs"].tolist()

#Creating application using Python-dash
#app = dash.Dash(__name__)

#Creating layout
app.layout = html.Div([
    html.H1("Modelling Immune Response in Python"),
    dcc.Dropdown(id='sample-names',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.SampleNames.unique())],
                 value='0.19'
                 ),
    dcc.Graph(id='my-graph', figure={}
              )
])

#Making callbacks
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='sample-names', component_property='value')
)

#Defining function for interaction
def interactive_graphs(sample_names_choice):
    #print(time_hrs_choice)
    dff = df[df.SampleNames == sample_names_choice]

    fig = px.box(data_frame=dff[0:135], x='TimeHrs', y='TotalCells', title="TimeHrs Stamp vs. Total Number of Cells for different SampleNames Chart", points="all")

    #fig.update_yaxes(range=[0, 50000])
    return fig

#Main method
if __name__=='__main__':
    app.run_server(debug=True)
