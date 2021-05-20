##=============================================
## Master of Computing and Innovation Project
## Student: Ruonan Fu, Tian Qiu, Vandit Gajjar
## Student ID: a1785307, a1777071, a1779153
## Semester: 1
## Year: 2021
## Milestone-1 Codebase
##=============================================

#Importing utilites
import statistics

import dash
from plotly.subplots import make_subplots
from statistics import mean
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import io
#################################################
####### TimeHrs vs. TotalCells Chart
#################################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

top_markdown_text = '''
This is my first deployed app
'''

app.layout = html.Div([

    dcc.Markdown(children=top_markdown_text),

])

#Creating dataframe
path_csv='https://github.com/Vanditg/MCI_tmp/blob/main/datasheet_1.csv?raw=true'

df=pd.read_csv(path_csv, error_bad_lines=False)

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

genTitle = ['Gen0', 'Gen1', 'Gen2', 'Gen3', 'Gen4', 'Gen5', 'Gen6', 'Gen7', 'Gen8']
totalCells = df["TotalCells"].tolist()
timeHrs = df["TimeHrs"].tolist()
fig = go.Figure()

#######################################
# Generation 0 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0]],
    y=Gen0[0:3] + Gen0[15:18] + Gen0[30:33] + Gen0[45:48] + Gen0[60:63] + Gen0[75:78] + Gen0[90:93] + Gen0[105:108] + Gen0[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 0 SampleNames 3"
))

#######################################
# Generation 1 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1]],
    y=Gen1[0:3] + Gen1[15:18] + Gen1[30:33] + Gen1[45:48] + Gen1[60:63] + Gen1[75:78] + Gen1[90:93] + Gen1[105:108] + Gen1[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 1 SampleNames 3"
))

#######################################
# Generation 2 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2]],
    y=Gen2[0:3] + Gen2[15:18] + Gen2[30:33] + Gen2[45:48] + Gen2[60:63] + Gen2[75:78] + Gen2[90:93] + Gen2[105:108] + Gen2[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 2 SampleNames 3"
))

#######################################
# Generation 3 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3]],
    y=Gen3[0:3] + Gen3[15:18] + Gen3[30:33] + Gen3[45:48] + Gen3[60:63] + Gen3[75:78] + Gen3[90:93] + Gen3[105:108] + Gen3[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 3 SampleNames 3"
))

#######################################
# Generation 4 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4]],
    y=Gen4[0:3] + Gen4[15:18] + Gen4[30:33] + Gen4[45:48] + Gen4[60:63] + Gen4[75:78] + Gen4[90:93] + Gen4[105:108] + Gen4[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 4 SampleNames 3"
))

#######################################
# Generation 5 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5]],
    y=Gen5[0:3] + Gen5[15:18] + Gen5[30:33] + Gen5[45:48] + Gen5[60:63] + Gen5[75:78] + Gen5[90:93] + Gen5[105:108] + Gen5[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 5 SampleNames 3"
))

#######################################
# Generation 6 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6]],
    y=Gen6[0:3] + Gen6[15:18] + Gen6[30:33] + Gen6[45:48] + Gen6[60:63] + Gen6[75:78] + Gen6[90:93] + Gen6[105:108] + Gen6[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 6 SampleNames 3"
))

#######################################
# Generation 7 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7]],
    y=Gen7[0:3] + Gen7[15:18] + Gen7[30:33] + Gen7[45:48] + Gen7[60:63] + Gen7[75:78] + Gen7[90:93] + Gen7[105:108] + Gen7[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 7 SampleNames 3"
))

#######################################
# Generation 8 SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8]],
    y=Gen8[0:3] + Gen8[15:18] + Gen8[30:33] + Gen8[45:48] + Gen8[60:63] + Gen8[75:78] + Gen8[90:93] + Gen8[105:108] + Gen8[120:123],
    marker=dict(color="blue", size=8),
    mode="markers",
    name="Gen 8 SampleNames 3"
))

#######################################
# Generation 0 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0]],
    y=Gen0[3:6] + Gen0[18:21] + Gen0[33:36] + Gen0[48:51] + Gen0[63:66] + Gen0[78:81] + Gen0[93:96] + Gen0[108:111] + Gen0[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 0 SampleNames 1.5"
))

#######################################
# Generation 1 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1]],
    y=Gen1[3:6] + Gen1[18:21] + Gen1[33:36] + Gen1[48:51] + Gen1[63:66] + Gen1[78:81] + Gen1[93:96] + Gen1[108:111] + Gen1[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 1 SampleNames 1.5"
))

#######################################
# Generation 2 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2]],
    y=Gen2[3:6] + Gen2[18:21] + Gen2[33:36] + Gen2[48:51] + Gen2[63:66] + Gen2[78:81] + Gen2[93:96] + Gen2[108:111] + Gen2[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 2 SampleNames 1.5"
))

#######################################
# Generation 3 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3]],
    y=Gen3[3:6] + Gen3[18:21] + Gen3[33:36] + Gen3[48:51] + Gen3[63:66] + Gen3[78:81] + Gen3[93:96] + Gen3[108:111] + Gen3[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 3 SampleNames 1.5"
))

#######################################
# Generation 4 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4]],
    y=Gen4[3:6] + Gen4[18:21] + Gen4[33:36] + Gen4[48:51] + Gen4[63:66] + Gen4[78:81] + Gen4[93:96] + Gen4[108:111] + Gen4[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 4 SampleNames 1.5"
))

#######################################
# Generation 5 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5]],
    y=Gen5[3:6] + Gen5[18:21] + Gen5[33:36] + Gen5[48:51] + Gen5[63:66] + Gen5[78:81] + Gen5[93:96] + Gen5[108:111] + Gen5[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 5 SampleNames 1.5"
))

#######################################
# Generation 6 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6]],
    y=Gen6[3:6] + Gen6[18:21] + Gen6[33:36] + Gen6[48:51] + Gen6[63:66] + Gen6[78:81] + Gen6[93:96] + Gen6[108:111] + Gen6[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 6 SampleNames 1.5"
))

#######################################
# Generation 7 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7]],
    y=Gen7[3:6] + Gen7[18:21] + Gen7[33:36] + Gen7[48:51] + Gen7[63:66] + Gen7[78:81] + Gen7[93:96] + Gen7[108:111] + Gen7[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 7 SampleNames 1.5"
))

#######################################
# Generation 8 SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8]],
    y=Gen8[3:6] + Gen8[18:21] + Gen8[33:36] + Gen8[48:51] + Gen8[63:66] + Gen8[78:81] + Gen8[93:96] + Gen8[108:111] + Gen8[123:126],
    marker=dict(color="red", size=8),
    mode="markers",
    name="Gen 8 SampleNames 1.5"
))

#######################################
# Generation 0 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0]],
    y=Gen0[6:9] + Gen0[21:24] + Gen0[36:39] + Gen0[51:54] + Gen0[66:69] + Gen0[81:84] + Gen0[96:99] + Gen0[111:114] + Gen0[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 0 SampleNames 0.75"
))

#######################################
# Generation 1 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1]],
    y=Gen1[6:9] + Gen1[21:24] + Gen1[36:39] + Gen1[51:54] + Gen1[66:69] + Gen1[81:84] + Gen1[96:99] + Gen1[111:114] + Gen1[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 1 SampleNames 0.75"
))

#######################################
# Generation 2 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2]],
    y=Gen2[6:9] + Gen2[21:24] + Gen2[36:39] + Gen2[51:54] + Gen2[66:69] + Gen2[81:84] + Gen2[96:99] + Gen2[111:114] + Gen2[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 2 SampleNames 0.75"
))

#######################################
# Generation 3 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3]],
    y=Gen3[6:9] + Gen3[21:24] + Gen3[36:39] + Gen3[51:54] + Gen3[66:69] + Gen3[81:84] + Gen3[96:99] + Gen3[111:114] + Gen3[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 3 SampleNames 0.75"
))

#######################################
# Generation 4 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4]],
    y=Gen4[6:9] + Gen4[21:24] + Gen4[36:39] + Gen4[51:54] + Gen4[66:69] + Gen4[81:84] + Gen4[96:99] + Gen4[111:114] + Gen4[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 4 SampleNames 0.75"
))

#######################################
# Generation 5 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5]],
    y=Gen5[6:9] + Gen5[21:24] + Gen5[36:39] + Gen5[51:54] + Gen5[66:69] + Gen5[81:84] + Gen5[96:99] + Gen5[111:114] + Gen5[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 5 SampleNames 0.75"
))

#######################################
# Generation 6 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6]],
    y=Gen6[6:9] + Gen6[21:24] + Gen6[36:39] + Gen6[51:54] + Gen6[66:69] + Gen6[81:84] + Gen6[96:99] + Gen6[111:114] + Gen6[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 6 SampleNames 0.75"
))

#######################################
# Generation 7 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7]],
    y=Gen7[6:9] + Gen7[21:24] + Gen7[36:39] + Gen7[51:54] + Gen7[66:69] + Gen7[81:84] + Gen7[96:99] + Gen7[111:114] + Gen7[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 7 SampleNames 0.75"
))

#######################################
# Generation 8 SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8]],
    y=Gen8[6:9] + Gen8[21:24] + Gen8[36:39] + Gen8[51:54] + Gen8[66:69] + Gen8[81:84] + Gen8[96:99] + Gen8[111:114] + Gen8[126:129],
    marker=dict(color="green", size=8),
    mode="markers",
    name="Gen 8 SampleNames 0.75"
))

#######################################
# Generation 0 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0]],
    y=Gen0[9:12] + Gen0[24:27] + Gen0[39:42] + Gen0[54:57] + Gen0[69:72] + Gen0[84:87] + Gen0[99:102] + Gen0[114:117] + Gen0[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 0 SampleNames 0.38"
))

#######################################
# Generation 1 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1]],
    y=Gen1[9:12] + Gen1[24:27] + Gen1[39:42] + Gen1[54:57] + Gen1[69:72] + Gen1[84:87] + Gen1[99:102] + Gen1[114:117] + Gen1[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 1 SampleNames 0.38"
))

#######################################
# Generation 2 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2]],
    y=Gen2[9:12] + Gen2[24:27] + Gen2[39:42] + Gen2[54:57] + Gen2[69:72] + Gen2[84:87] + Gen2[99:102] + Gen2[114:117] + Gen2[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 2 SampleNames 0.38"
))

#######################################
# Generation 3 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3]],
    y=Gen3[9:12] + Gen3[24:27] + Gen3[39:42] + Gen3[54:57] + Gen3[69:72] + Gen3[84:87] + Gen3[99:102] + Gen3[114:117] + Gen3[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 3 SampleNames 0.38"
))

#######################################
# Generation 4 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4]],
    y=Gen4[9:12] + Gen4[24:27] + Gen4[39:42] + Gen4[54:57] + Gen4[69:72] + Gen4[84:87] + Gen4[99:102] + Gen4[114:117] + Gen4[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 4 SampleNames 0.38"
))

#######################################
# Generation 5 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5]],
    y=Gen5[9:12] + Gen5[24:27] + Gen5[39:42] + Gen5[54:57] + Gen5[69:72] + Gen5[84:87] + Gen5[99:102] + Gen5[114:117] + Gen5[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 5 SampleNames 0.38"
))

#######################################
# Generation 6 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6]],
    y=Gen6[9:12] + Gen6[24:27] + Gen6[39:42] + Gen6[54:57] + Gen6[69:72] + Gen6[84:87] + Gen6[99:102] + Gen6[114:117] + Gen6[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 6 SampleNames 0.38"
))

#######################################
# Generation 7 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7]],
    y=Gen7[9:12] + Gen7[24:27] + Gen7[39:42] + Gen7[54:57] + Gen7[69:72] + Gen7[84:87] + Gen7[99:102] + Gen7[114:117] + Gen7[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 7 SampleNames 0.38"
))

#######################################
# Generation 8 SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8]],
    y=Gen8[9:12] + Gen8[24:27] + Gen8[39:42] + Gen8[54:57] + Gen8[69:72] + Gen8[84:87] + Gen8[99:102] + Gen8[114:117] + Gen8[129:132],
    marker=dict(color="gold", size=8),
    mode="markers",
    name="Gen 8 SampleNames 0.38"
))

#######################################
# Generation 0 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0],genTitle[0], genTitle[0], genTitle[0]],
    y=Gen0[12:15] + Gen0[27:30] + Gen0[42:45] + Gen0[57:60] + Gen0[72:75] + Gen0[87:90] + Gen0[102:105] + Gen0[117:120] + Gen0[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 0 SampleNames 0.19"
))

#######################################
# Generation 1 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1],genTitle[1], genTitle[1], genTitle[1]],
    y=Gen1[12:15] + Gen1[27:30] + Gen1[42:45] + Gen1[57:60] + Gen1[72:75] + Gen1[87:90] + Gen1[102:105] + Gen1[117:120] + Gen1[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 1 SampleNames 0.19"
))

#######################################
# Generation 2 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2],genTitle[2], genTitle[2], genTitle[2]],
    y=Gen2[12:15] + Gen2[27:30] + Gen2[42:45] + Gen2[57:60] + Gen2[72:75] + Gen2[87:90] + Gen2[102:105] + Gen2[117:120] + Gen2[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 2 SampleNames 0.19"
))

#######################################
# Generation 3 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3],genTitle[3], genTitle[3], genTitle[3]],
    y=Gen3[12:15] + Gen3[27:30] + Gen3[42:45] + Gen3[57:60] + Gen3[72:75] + Gen3[87:90] + Gen3[102:105] + Gen3[117:120] + Gen3[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 3 SampleNames 0.19"
))

#######################################
# Generation 4 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4],genTitle[4], genTitle[4], genTitle[4]],
    y=Gen4[12:15] + Gen4[27:30] + Gen4[42:45] + Gen4[57:60] + Gen4[72:75] + Gen4[87:90] + Gen4[102:105] + Gen4[117:120] + Gen4[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 4 SampleNames 0.19"
))

#######################################
# Generation 5 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5],genTitle[5], genTitle[5], genTitle[5]],
    y=Gen5[12:15] + Gen5[27:30] + Gen5[42:45] + Gen5[57:60] + Gen5[72:75] + Gen5[87:90] + Gen5[102:105] + Gen5[117:120] + Gen5[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 5 SampleNames 0.19"
))

#######################################
# Generation 6 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6],genTitle[6], genTitle[6], genTitle[6]],
    y=Gen6[12:15] + Gen6[27:30] + Gen6[42:45] + Gen6[57:60] + Gen6[72:75] + Gen6[87:90] + Gen6[102:105] + Gen6[117:120] + Gen6[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 6 SampleNames 0.19"
))

#######################################
# Generation 7 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7],genTitle[7], genTitle[7], genTitle[7]],
    y=Gen7[12:15] + Gen7[27:30] + Gen7[42:45] + Gen7[57:60] + Gen7[72:75] + Gen7[87:90] + Gen7[102:105] + Gen7[117:120] + Gen7[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 7 SampleNames 0.19"
))

#######################################
# Generation 8 SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x=[genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8],genTitle[8], genTitle[8], genTitle[8]],
    y=Gen8[12:15] + Gen8[27:30] + Gen8[42:45] + Gen8[57:60] + Gen8[72:75] + Gen8[87:90] + Gen8[102:105] + Gen8[117:120] + Gen8[132:135],
    marker=dict(color="black", size=8),
    mode="markers",
    name="Gen 8 SampleNames 0.19"
))

#######################################
# Mean Point Connect SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[0:3] + Gen0[15:18] + Gen0[30:33] + Gen0[45:48] + Gen0[60:63] + Gen0[75:78] + Gen0[90:93] + Gen0[105:108] + Gen0[120:123]),
         statistics.mean(Gen1[0:3] + Gen1[15:18] + Gen1[30:33] + Gen1[45:48] + Gen1[60:63] + Gen1[75:78] + Gen1[90:93] + Gen1[105:108] + Gen1[120:123]),
         statistics.mean(Gen2[0:3] + Gen2[15:18] + Gen2[30:33] + Gen2[45:48] + Gen2[60:63] + Gen2[75:78] + Gen2[90:93] + Gen2[105:108] + Gen2[120:123]),
         statistics.mean(Gen3[0:3] + Gen3[15:18] + Gen3[30:33] + Gen3[45:48] + Gen3[60:63] + Gen3[75:78] + Gen3[90:93] + Gen3[105:108] + Gen3[120:123]),
         statistics.mean(Gen4[0:3] + Gen4[15:18] + Gen4[30:33] + Gen4[45:48] + Gen4[60:63] + Gen4[75:78] + Gen4[90:93] + Gen4[105:108] + Gen4[120:123]),
         statistics.mean(Gen5[0:3] + Gen5[15:18] + Gen5[30:33] + Gen5[45:48] + Gen5[60:63] + Gen5[75:78] + Gen5[90:93] + Gen5[105:108] + Gen5[120:123]),
         statistics.mean(Gen6[0:3] + Gen6[15:18] + Gen6[30:33] + Gen6[45:48] + Gen6[60:63] + Gen6[75:78] + Gen6[90:93] + Gen6[105:108] + Gen6[120:123]),
         statistics.mean(Gen7[0:3] + Gen7[15:18] + Gen7[30:33] + Gen7[45:48] + Gen7[60:63] + Gen7[75:78] + Gen7[90:93] + Gen7[105:108] + Gen7[120:123]),
         statistics.mean(Gen8[0:3] + Gen8[15:18] + Gen8[30:33] + Gen8[45:48] + Gen8[60:63] + Gen8[75:78] + Gen8[90:93] + Gen8[105:108] + Gen8[120:123])],
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",
    name="Mean Points for SampleNames 3"
))

#######################################
# Mean Point Connect SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[3:6] + Gen0[18:21] + Gen0[33:36] + Gen0[48:51] + Gen0[63:66] + Gen0[78:81] + Gen0[93:96] + Gen0[108:111] + Gen0[123:126]),
         statistics.mean(Gen1[3:6] + Gen1[18:21] + Gen1[33:36] + Gen1[48:51] + Gen1[63:66] + Gen1[78:81] + Gen1[93:96] + Gen1[108:111] + Gen1[123:126]),
         statistics.mean(Gen2[3:6] + Gen2[18:21] + Gen2[33:36] + Gen2[48:51] + Gen2[63:66] + Gen2[78:81] + Gen2[93:96] + Gen2[108:111] + Gen2[123:126]),
         statistics.mean(Gen3[3:6] + Gen3[18:21] + Gen3[33:36] + Gen3[48:51] + Gen3[63:66] + Gen3[78:81] + Gen3[93:96] + Gen3[108:111] + Gen3[123:126]),
         statistics.mean(Gen4[3:6] + Gen4[18:21] + Gen4[33:36] + Gen4[48:51] + Gen4[63:66] + Gen4[78:81] + Gen4[93:96] + Gen4[108:111] + Gen4[123:126]),
         statistics.mean(Gen5[3:6] + Gen5[18:21] + Gen5[33:36] + Gen5[48:51] + Gen5[63:66] + Gen5[78:81] + Gen5[93:96] + Gen5[108:111] + Gen5[123:126]),
         statistics.mean(Gen6[3:6] + Gen6[18:21] + Gen6[33:36] + Gen6[48:51] + Gen6[63:66] + Gen6[78:81] + Gen6[93:96] + Gen6[108:111] + Gen6[123:126]),
         statistics.mean(Gen7[3:6] + Gen7[18:21] + Gen7[33:36] + Gen7[48:51] + Gen7[63:66] + Gen7[78:81] + Gen7[93:96] + Gen7[108:111] + Gen7[123:126]),
         statistics.mean(Gen8[3:6] + Gen8[18:21] + Gen8[33:36] + Gen8[48:51] + Gen8[63:66] + Gen8[78:81] + Gen8[93:96] + Gen8[108:111] + Gen8[123:126])],
    marker=dict(color="red", size=11, symbol="square"),
    mode="lines + markers",
    name="Mean Points for SampleNames 1.5"
))

#######################################
# Mean Point Connect SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[6:9] + Gen0[21:24] + Gen0[36:39] + Gen0[51:54] + Gen0[66:69] + Gen0[81:84] + Gen0[96:99] + Gen0[111:114] + Gen0[126:129]),
         statistics.mean(Gen1[6:9] + Gen1[21:24] + Gen1[36:39] + Gen1[51:54] + Gen1[66:69] + Gen1[81:84] + Gen1[96:99] + Gen1[111:114] + Gen1[126:129]),
         statistics.mean(Gen2[6:9] + Gen2[21:24] + Gen2[36:39] + Gen2[51:54] + Gen2[66:69] + Gen2[81:84] + Gen2[96:99] + Gen2[111:114] + Gen2[126:129]),
         statistics.mean(Gen3[6:9] + Gen3[21:24] + Gen3[36:39] + Gen3[51:54] + Gen3[66:69] + Gen3[81:84] + Gen3[96:99] + Gen3[111:114] + Gen3[126:129]),
         statistics.mean(Gen4[6:9] + Gen4[21:24] + Gen4[36:39] + Gen4[51:54] + Gen4[66:69] + Gen4[81:84] + Gen4[96:99] + Gen4[111:114] + Gen4[126:129]),
         statistics.mean(Gen5[6:9] + Gen5[21:24] + Gen5[36:39] + Gen5[51:54] + Gen5[66:69] + Gen5[81:84] + Gen5[96:99] + Gen5[111:114] + Gen5[126:129]),
         statistics.mean(Gen6[6:9] + Gen6[21:24] + Gen6[36:39] + Gen6[51:54] + Gen6[66:69] + Gen6[81:84] + Gen6[96:99] + Gen6[111:114] + Gen6[126:129]),
         statistics.mean(Gen7[6:9] + Gen7[21:24] + Gen7[36:39] + Gen7[51:54] + Gen7[66:69] + Gen7[81:84] + Gen7[96:99] + Gen7[111:114] + Gen7[126:129]),
         statistics.mean(Gen8[6:9] + Gen8[21:24] + Gen8[36:39] + Gen8[51:54] + Gen8[66:69] + Gen8[81:84] + Gen8[96:99] + Gen8[111:114] + Gen8[126:129])],
    marker=dict(color="green", size=11, symbol="hexagon"),
    mode="lines + markers",
    name="Mean Points for SampleNames 0.75"
))

#######################################
# Mean Point Connect SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[9:12] + Gen0[24:27] + Gen0[39:42] + Gen0[54:57] + Gen0[69:72] + Gen0[84:87] + Gen0[99:102] + Gen0[114:117] + Gen0[129:132]),
         statistics.mean(Gen1[9:12] + Gen1[24:27] + Gen1[39:42] + Gen1[54:57] + Gen1[69:72] + Gen1[84:87] + Gen1[99:102] + Gen1[114:117] + Gen1[129:132]),
         statistics.mean(Gen2[9:12] + Gen2[24:27] + Gen2[39:42] + Gen2[54:57] + Gen2[69:72] + Gen2[84:87] + Gen2[99:102] + Gen2[114:117] + Gen2[129:132]),
         statistics.mean(Gen3[9:12] + Gen3[24:27] + Gen3[39:42] + Gen3[54:57] + Gen3[69:72] + Gen3[84:87] + Gen3[99:102] + Gen3[114:117] + Gen3[129:132]),
         statistics.mean(Gen4[9:12] + Gen4[24:27] + Gen4[39:42] + Gen4[54:57] + Gen4[69:72] + Gen4[84:87] + Gen4[99:102] + Gen4[114:117] + Gen4[129:132]),
         statistics.mean(Gen5[9:12] + Gen5[24:27] + Gen5[39:42] + Gen5[54:57] + Gen5[69:72] + Gen5[84:87] + Gen5[99:102] + Gen5[114:117] + Gen5[129:132]),
         statistics.mean(Gen6[9:12] + Gen6[24:27] + Gen6[39:42] + Gen6[54:57] + Gen6[69:72] + Gen6[84:87] + Gen6[99:102] + Gen6[114:117] + Gen6[129:132]),
         statistics.mean(Gen7[9:12] + Gen7[24:27] + Gen7[39:42] + Gen7[54:57] + Gen7[69:72] + Gen7[84:87] + Gen7[99:102] + Gen7[114:117] + Gen7[129:132]),
         statistics.mean(Gen8[9:12] + Gen8[24:27] + Gen8[39:42] + Gen8[54:57] + Gen8[69:72] + Gen8[84:87] + Gen8[99:102] + Gen8[114:117] + Gen8[129:132])],
    marker=dict(color="gold", size=11, symbol="pentagon"),
    mode="lines + markers",
    name="Mean Points for SampleNames 0.38"
))

#######################################
# Mean Point Connect SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[12:15] + Gen0[27:30] + Gen0[42:45] + Gen0[57:60] + Gen0[72:75] + Gen0[87:90] + Gen0[102:105] + Gen0[117:120] + Gen0[132:135]),
         statistics.mean(Gen1[12:15] + Gen1[27:30] + Gen1[42:45] + Gen1[57:60] + Gen1[72:75] + Gen1[87:90] + Gen1[102:105] + Gen1[117:120] + Gen1[132:135]),
         statistics.mean(Gen2[12:15] + Gen2[27:30] + Gen2[42:45] + Gen2[57:60] + Gen2[72:75] + Gen2[87:90] + Gen2[102:105] + Gen2[117:120] + Gen2[132:135]),
         statistics.mean(Gen3[12:15] + Gen3[27:30] + Gen3[42:45] + Gen3[57:60] + Gen3[72:75] + Gen3[87:90] + Gen3[102:105] + Gen3[117:120] + Gen3[132:135]),
         statistics.mean(Gen4[12:15] + Gen4[27:30] + Gen4[42:45] + Gen4[57:60] + Gen4[72:75] + Gen4[87:90] + Gen4[102:105] + Gen4[117:120] + Gen4[132:135]),
         statistics.mean(Gen5[12:15] + Gen5[27:30] + Gen5[42:45] + Gen5[57:60] + Gen5[72:75] + Gen5[87:90] + Gen5[102:105] + Gen5[117:120] + Gen5[132:135]),
         statistics.mean(Gen6[12:15] + Gen6[27:30] + Gen6[42:45] + Gen6[57:60] + Gen6[72:75] + Gen6[87:90] + Gen6[102:105] + Gen6[117:120] + Gen6[132:135]),
         statistics.mean(Gen7[12:15] + Gen7[27:30] + Gen7[42:45] + Gen7[57:60] + Gen7[72:75] + Gen7[87:90] + Gen7[102:105] + Gen7[117:120] + Gen7[132:135]),
         statistics.mean(Gen8[12:15] + Gen8[27:30] + Gen8[42:45] + Gen8[57:60] + Gen8[72:75] + Gen8[87:90] + Gen8[102:105] + Gen8[117:120] + Gen8[132:135])],
    marker=dict(color="black", size=11, symbol="pentagon"),
    mode="lines + markers",
    name="Mean Points for SampleNames 0.19"
))

fig.update_xaxes(title_text="Generations")
fig.update_yaxes(title_text="Cells")

fig.update_layout(font_family="Courier New", font_color="blue", title_font_family="Times New Roman", title_font_color="red", legend_title_font_color="green", height=500, width=2000, title={'text': "Modelling Immune Responses in Python"})
fig.show()

app.layout = html.Div(children=[
    html.H1(children='Modelling Immune Responses in Python'),

    html.Div(children='''
        Modelling Immune Responses in Python
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)
