##=============================================
## Master of Computing and Innovation Project
## Student: Ruonan Fu, Tian Qiu, Vandit Gajjar
## Student ID: a1785307, a1777071, a1779153
## Semester: 1
## Year: 2021
## Milestone-1 Codebase
##=============================================

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

#################################################
####### Data Visulisation for all the data-points
#################################################
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

#Creating dataframe
df = pd.read_csv("C:/Users/gajja/Desktop/MCI_Project_Final/DatasetFiles/datasheet_1.csv")

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

#Making Subplots
fig = make_subplots(rows=2, cols=9)

####SampleNames: 0.19, 0.38, 0.75, 1.5, 3
fig.add_trace(go.Box(x=timeHrs[0:15], y=totalCells[0:15]), row=1, col=1)
fig.add_trace(go.Box(x=timeHrs[15:30], y=totalCells[15:30]), row=1, col=2)
fig.add_trace(go.Box(x=timeHrs[30:45], y=totalCells[30:45]), row=1, col=3)
fig.add_trace(go.Box(x=timeHrs[45:60], y=totalCells[45:60]), row=1, col=4)
fig.add_trace(go.Box(x=timeHrs[60:75], y=totalCells[60:75]), row=1, col=5)
fig.add_trace(go.Box(x=timeHrs[75:90], y=totalCells[75:90]), row=1, col=6)
fig.add_trace(go.Box(x=timeHrs[90:105], y=totalCells[90:105]), row=1, col=7)
fig.add_trace(go.Box(x=timeHrs[105:120], y=totalCells[105:120]), row=1, col=8)
fig.add_trace(go.Box(x=timeHrs[120:135], y=totalCells[120:135]), row=1, col=9)

fig.update_layout(font_family="Courier New", font_color="blue", title_font_family="Times New Roman", title_font_color="red", legend_title_font_color="green", height=500, width=2000, title={'text': "Modelling Immune Responses in Python"})
fig.show()

if __name__ == '__main__':
 app.run_server(debug=True)
