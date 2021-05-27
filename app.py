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

fig = make_subplots(rows=5, cols=1)

#######################################
# SampleNames 3
#######################################
fig.add_trace(go.Scatter(
    x = timeHrs[0:1] + timeHrs[15:16] + timeHrs[30:31] + timeHrs[45:46] + timeHrs[60:61] + timeHrs[75:76] + timeHrs[90:91] + timeHrs[105:106] + timeHrs[120:121],
    y = [statistics.mean(totalCells[0:3]), statistics.mean(totalCells[15:18]), statistics.mean(totalCells[30:33]), statistics.mean(totalCells[45:48]), statistics.mean(totalCells[60:63]), statistics.mean(totalCells[75:78]), statistics.mean(totalCells[90:93]), statistics.mean(totalCells[105:108]), statistics.mean(totalCells[120:123])],
    marker=dict(color="blue", size=12, symbol="hexagon"),
    mode="lines + markers",
    name="Mean Points for SampleNames 3"
), row=1, col=1)
#######################################
# SampleNames 1.5
#######################################
fig.add_trace(go.Scatter(
    x = timeHrs[0:1] + timeHrs[15:16] + timeHrs[30:31] + timeHrs[45:46] + timeHrs[60:61] + timeHrs[75:76] + timeHrs[90:91] + timeHrs[105:106] + timeHrs[120:121],
    y = [statistics.mean(totalCells[3:6]), statistics.mean(totalCells[18:21]), statistics.mean(totalCells[33:36]), statistics.mean(totalCells[48:51]), statistics.mean(totalCells[63:66]), statistics.mean(totalCells[78:81]), statistics.mean(totalCells[93:96]), statistics.mean(totalCells[108:111]), statistics.mean(totalCells[123:126])],
    marker=dict(color="red", size=12, symbol="diamond"),
    mode="lines + markers",
    name="Mean Points for SampleNames 1.5"
), row=2, col=1)

#######################################
# SampleNames 0.75
#######################################
fig.add_trace(go.Scatter(
    x = timeHrs[0:1] + timeHrs[15:16] + timeHrs[30:31] + timeHrs[45:46] + timeHrs[60:61] + timeHrs[75:76] + timeHrs[90:91] + timeHrs[105:106] + timeHrs[120:121],
    y = [statistics.mean(totalCells[6:9]), statistics.mean(totalCells[21:24]), statistics.mean(totalCells[36:39]), statistics.mean(totalCells[51:54]), statistics.mean(totalCells[66:69]), statistics.mean(totalCells[81:84]), statistics.mean(totalCells[96:99]), statistics.mean(totalCells[111:114]), statistics.mean(totalCells[126:129])],
    marker=dict(color="orange", size=12, symbol="square"),
    mode="lines + markers",
    name="Mean Points for SampleNames 0.75"
), row=3, col=1)

#######################################
# SampleNames 0.38
#######################################
fig.add_trace(go.Scatter(
    x = timeHrs[0:1] + timeHrs[15:16] + timeHrs[30:31] + timeHrs[45:46] + timeHrs[60:61] + timeHrs[75:76] + timeHrs[90:91] + timeHrs[105:106] + timeHrs[120:121],
    y = [statistics.mean(totalCells[9:12]), statistics.mean(totalCells[24:27]), statistics.mean(totalCells[39:42]), statistics.mean(totalCells[54:57]), statistics.mean(totalCells[69:72]), statistics.mean(totalCells[84:87]), statistics.mean(totalCells[99:102]), statistics.mean(totalCells[114:117]), statistics.mean(totalCells[129:132])],
    marker=dict(color="green", size=11, symbol="cross"),
    mode="lines + markers",
    name="Mean Points for SampleNames 0.38"
), row=4, col=1)

#######################################
# SampleNames 0.19
#######################################
fig.add_trace(go.Scatter(
    x = timeHrs[0:1] + timeHrs[15:16] + timeHrs[30:31] + timeHrs[45:46] + timeHrs[60:61] + timeHrs[75:76] + timeHrs[90:91] + timeHrs[105:106] + timeHrs[120:121],
    y = [statistics.mean(totalCells[12:15]), statistics.mean(totalCells[27:30]), statistics.mean(totalCells[42:45]), statistics.mean(totalCells[57:60]), statistics.mean(totalCells[72:75]), statistics.mean(totalCells[87:90]), statistics.mean(totalCells[102:105]), statistics.mean(totalCells[117:120]), statistics.mean(totalCells[132:135])],
    marker=dict(color="black", size=11, symbol="star-square"),
    mode="lines + markers",
    name="Mean Points for SampleNames 0.19"
), row=5, col=1)

fig.update_xaxes(title_text="TimeHrs", row=5, col=1)
fig.update_yaxes(range=[0, 200000])
fig.update_yaxes(title_text="TotalCells", row=3, col=1)

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
