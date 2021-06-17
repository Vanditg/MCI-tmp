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
from scipy import stats
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
timeTitle = ['19.5', '27.5', '44', '52', '68', '80.5', '95.5', '124', '140']
totalCells = df["TotalCells"].tolist()
timeHrs = df["TimeHrs"].tolist()

fig = make_subplots(rows=9, cols=4, subplot_titles=("Cell Count vs Generation | T = 19.5h", "Cell Count vs Time-Period | Gen0", "Cohort Number vs Generation | T = 19.5", "Cohort Number vs Time-Period | Gen0",
                                                    "T = 27.5h", "Gen1", "T = 27.5h", "Gen1",
                                                    "T = 44h", "Gen2", "T = 44h", "Gen2",
                                                    "T = 52h", "Gen3", "T = 52h", "Gen3",
                                                    "T = 68h", "Gen4", "T = 68h", "Gen4",
                                                    "T = 80.5h", "Gen5", "T = 80.5h", "Gen5",
                                                    "T = 95.5h", "Gen6", "T = 95.5h", "Gen6",
                                                    "T = 124h", "Gen7", "T = 124h", "Gen7",
                                                    "T = 140h", "Gen8", "T = 140h", "Gen8"))
#######################################
# SampleNames 3 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[0:3]), statistics.mean(Gen1[0:3]), statistics.mean(Gen2[0:3]), statistics.mean(Gen3[0:3]), statistics.mean(Gen4[0:3]), statistics.mean(Gen5[0:3]), statistics.mean(Gen6[0:3]), statistics.mean(Gen7[0:3]), statistics.mean(Gen8[0:3])],
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",
    name="SampleNames 3"), row=1, col=1)

#######################################
# SampleNames 3 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[15:18]), statistics.mean(Gen1[15:18]), statistics.mean(Gen2[15:18]), statistics.mean(Gen3[15:18]), statistics.mean(Gen4[15:18]), statistics.mean(Gen5[15:18]), statistics.mean(Gen6[15:18]), statistics.mean(Gen7[15:18]), statistics.mean(Gen8[15:18])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=2, col=1)

#######################################
# SampleNames 3 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[30:33]), statistics.mean(Gen1[30:33]), statistics.mean(Gen2[30:33]), statistics.mean(Gen3[30:33]), statistics.mean(Gen4[30:33]), statistics.mean(Gen5[30:33]), statistics.mean(Gen6[30:33]), statistics.mean(Gen7[30:33]), statistics.mean(Gen8[30:33])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=3, col=1)

#######################################
# SampleNames 3 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[45:48]), statistics.mean(Gen1[45:48]), statistics.mean(Gen2[45:48]), statistics.mean(Gen3[45:48]), statistics.mean(Gen4[45:48]), statistics.mean(Gen5[45:48]), statistics.mean(Gen6[45:48]), statistics.mean(Gen7[45:48]), statistics.mean(Gen8[45:48])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=4, col=1)

#######################################
# SampleNames 3 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[60:63]), statistics.mean(Gen1[60:63]), statistics.mean(Gen2[60:63]), statistics.mean(Gen3[60:63]), statistics.mean(Gen4[60:63]), statistics.mean(Gen5[60:63]), statistics.mean(Gen6[60:63]), statistics.mean(Gen7[60:63]), statistics.mean(Gen8[60:63])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=5, col=1)

#######################################
# SampleNames 3 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[75:78]), statistics.mean(Gen1[75:78]), statistics.mean(Gen2[75:78]), statistics.mean(Gen3[75:78]), statistics.mean(Gen4[75:78]), statistics.mean(Gen5[75:78]), statistics.mean(Gen6[75:78]), statistics.mean(Gen7[75:78]), statistics.mean(Gen8[75:78])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=6, col=1)

#######################################
# SampleNames 3 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[90:93]), statistics.mean(Gen1[90:93]), statistics.mean(Gen2[90:93]), statistics.mean(Gen3[90:93]), statistics.mean(Gen4[90:93]), statistics.mean(Gen5[90:93]), statistics.mean(Gen6[90:93]), statistics.mean(Gen7[90:93]), statistics.mean(Gen8[90:93])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=7, col=1)

#######################################
# SampleNames 3 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[105:108]), statistics.mean(Gen1[105:108]), statistics.mean(Gen2[105:108]), statistics.mean(Gen3[105:108]), statistics.mean(Gen4[105:108]), statistics.mean(Gen5[105:108]), statistics.mean(Gen6[105:108]), statistics.mean(Gen7[105:108]), statistics.mean(Gen8[105:108])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=8, col=1)

#######################################
# SampleNames 3 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[120:123]), statistics.mean(Gen1[120:123]), statistics.mean(Gen2[120:123]), statistics.mean(Gen3[120:123]), statistics.mean(Gen4[120:123]), statistics.mean(Gen5[120:123]), statistics.mean(Gen6[120:123]), statistics.mean(Gen7[120:123]), statistics.mean(Gen8[120:123])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=9, col=1)

#######################################
# SampleNames 1.5 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[3:6]), statistics.mean(Gen1[3:6]), statistics.mean(Gen2[3:6]), statistics.mean(Gen3[3:6]), statistics.mean(Gen4[3:6]), statistics.mean(Gen5[3:6]), statistics.mean(Gen6[3:6]), statistics.mean(Gen7[3:6]), statistics.mean(Gen8[3:6])],
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",
    name="SampleNames 1.5"), row=1, col=1)

#######################################
# SampleNames 1.5 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[18:21]), statistics.mean(Gen1[18:21]), statistics.mean(Gen2[18:21]), statistics.mean(Gen3[18:21]), statistics.mean(Gen4[18:21]), statistics.mean(Gen5[18:21]), statistics.mean(Gen6[18:21]), statistics.mean(Gen7[18:21]), statistics.mean(Gen8[18:21])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=2, col=1)

#######################################
# SampleNames 1.5 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[33:36]), statistics.mean(Gen1[33:36]), statistics.mean(Gen2[33:36]), statistics.mean(Gen3[33:36]), statistics.mean(Gen4[33:36]), statistics.mean(Gen5[33:36]), statistics.mean(Gen6[33:36]), statistics.mean(Gen7[33:36]), statistics.mean(Gen8[33:36])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=3, col=1)

#######################################
# SampleNames 1.5 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[48:51]), statistics.mean(Gen1[48:51]), statistics.mean(Gen2[48:51]), statistics.mean(Gen3[48:51]), statistics.mean(Gen4[48:51]), statistics.mean(Gen5[48:51]), statistics.mean(Gen6[48:51]), statistics.mean(Gen7[48:51]), statistics.mean(Gen8[48:51])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=4, col=1)

#######################################
# SampleNames 1.5 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[63:66]), statistics.mean(Gen1[63:66]), statistics.mean(Gen2[63:66]), statistics.mean(Gen3[63:66]), statistics.mean(Gen4[63:66]), statistics.mean(Gen5[63:66]), statistics.mean(Gen6[63:66]), statistics.mean(Gen7[63:66]), statistics.mean(Gen8[63:66])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=5, col=1)

#######################################
# SampleNames 1.5 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[78:81]), statistics.mean(Gen1[78:81]), statistics.mean(Gen2[78:81]), statistics.mean(Gen3[78:81]), statistics.mean(Gen4[78:81]), statistics.mean(Gen5[78:81]), statistics.mean(Gen6[78:81]), statistics.mean(Gen7[78:81]), statistics.mean(Gen8[78:81])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=6, col=1)

#######################################
# SampleNames 1.5 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[93:96]), statistics.mean(Gen1[93:96]), statistics.mean(Gen2[93:96]), statistics.mean(Gen3[93:96]), statistics.mean(Gen4[93:96]), statistics.mean(Gen5[93:96]), statistics.mean(Gen6[93:96]), statistics.mean(Gen7[93:96]), statistics.mean(Gen8[93:96])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=7, col=1)

#######################################
# SampleNames 1.5 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[108:111]), statistics.mean(Gen1[108:111]), statistics.mean(Gen2[108:111]), statistics.mean(Gen3[108:111]), statistics.mean(Gen4[108:111]), statistics.mean(Gen5[108:111]), statistics.mean(Gen6[108:111]), statistics.mean(Gen7[108:111]), statistics.mean(Gen8[108:111])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=8, col=1)

#######################################
# SampleNames 1.5 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[123:126]), statistics.mean(Gen1[123:126]), statistics.mean(Gen2[123:126]), statistics.mean(Gen3[123:126]), statistics.mean(Gen4[123:126]), statistics.mean(Gen5[123:126]), statistics.mean(Gen6[123:126]), statistics.mean(Gen7[123:126]), statistics.mean(Gen8[123:126])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=9, col=1)

#######################################
# SampleNames 0.75 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[6:9]), statistics.mean(Gen1[6:9]), statistics.mean(Gen2[6:9]), statistics.mean(Gen3[6:9]), statistics.mean(Gen4[6:9]), statistics.mean(Gen5[6:9]), statistics.mean(Gen6[6:9]), statistics.mean(Gen7[6:9]), statistics.mean(Gen8[6:9])],
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",
    name="SampleNames 0.75"), row=1, col=1)

#######################################
# SampleNames 0.75 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[21:24]), statistics.mean(Gen1[21:24]), statistics.mean(Gen2[21:24]), statistics.mean(Gen3[21:24]), statistics.mean(Gen4[21:24]), statistics.mean(Gen5[21:24]), statistics.mean(Gen6[21:24]), statistics.mean(Gen7[21:24]), statistics.mean(Gen8[21:24])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=2, col=1)

#######################################
# SampleNames 0.75 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[36:39]), statistics.mean(Gen1[36:39]), statistics.mean(Gen2[36:39]), statistics.mean(Gen3[36:39]), statistics.mean(Gen4[36:39]), statistics.mean(Gen5[36:39]), statistics.mean(Gen6[36:39]), statistics.mean(Gen7[36:39]), statistics.mean(Gen8[36:39])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=3, col=1)

#######################################
# SampleNames 0.75 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[51:54]), statistics.mean(Gen1[51:54]), statistics.mean(Gen2[51:54]), statistics.mean(Gen3[51:54]), statistics.mean(Gen4[51:54]), statistics.mean(Gen5[51:54]), statistics.mean(Gen6[51:54]), statistics.mean(Gen7[51:54]), statistics.mean(Gen8[51:54])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=4, col=1)

#######################################
# SampleNames 0.75 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[66:69]), statistics.mean(Gen1[66:69]), statistics.mean(Gen2[66:69]), statistics.mean(Gen3[66:69]), statistics.mean(Gen4[66:69]), statistics.mean(Gen5[66:69]), statistics.mean(Gen6[66:69]), statistics.mean(Gen7[66:69]), statistics.mean(Gen8[66:69])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=5, col=1)

#######################################
# SampleNames 0.75 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[81:84]), statistics.mean(Gen1[81:84]), statistics.mean(Gen2[81:84]), statistics.mean(Gen3[81:84]), statistics.mean(Gen4[81:84]), statistics.mean(Gen5[81:84]), statistics.mean(Gen6[81:84]), statistics.mean(Gen7[81:84]), statistics.mean(Gen8[81:84])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=6, col=1)

#######################################
# SampleNames 0.75 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[96:99]), statistics.mean(Gen1[96:99]), statistics.mean(Gen2[96:99]), statistics.mean(Gen3[96:99]), statistics.mean(Gen4[96:99]), statistics.mean(Gen5[96:99]), statistics.mean(Gen6[96:99]), statistics.mean(Gen7[96:99]), statistics.mean(Gen8[96:99])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=7, col=1)

#######################################
# SampleNames 0.75 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[111:114]), statistics.mean(Gen1[111:114]), statistics.mean(Gen2[111:114]), statistics.mean(Gen3[111:114]), statistics.mean(Gen4[111:114]), statistics.mean(Gen5[111:114]), statistics.mean(Gen6[111:114]), statistics.mean(Gen7[111:114]), statistics.mean(Gen8[111:114])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=8, col=1)

#######################################
# SampleNames 0.75 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[126:129]), statistics.mean(Gen1[126:129]), statistics.mean(Gen2[126:129]), statistics.mean(Gen3[126:129]), statistics.mean(Gen4[126:129]), statistics.mean(Gen5[126:129]), statistics.mean(Gen6[126:129]), statistics.mean(Gen7[126:129]), statistics.mean(Gen8[126:129])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=9, col=1)

#######################################
# SampleNames 0.38 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[9:12]), statistics.mean(Gen1[9:12]), statistics.mean(Gen2[9:12]), statistics.mean(Gen3[9:12]), statistics.mean(Gen4[9:12]), statistics.mean(Gen5[9:12]), statistics.mean(Gen6[9:12]), statistics.mean(Gen7[9:12]), statistics.mean(Gen8[9:12])],
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",
    name="SampleNames 0.38"), row=1, col=1)

#######################################
# SampleNames 0.38 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[24:27]), statistics.mean(Gen1[24:27]), statistics.mean(Gen2[24:27]), statistics.mean(Gen3[24:27]), statistics.mean(Gen4[24:27]), statistics.mean(Gen5[24:27]), statistics.mean(Gen6[24:27]), statistics.mean(Gen7[24:27]), statistics.mean(Gen8[24:27])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=1)

#######################################
# SampleNames 0.38 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[39:42]), statistics.mean(Gen1[39:42]), statistics.mean(Gen2[39:42]), statistics.mean(Gen3[39:42]), statistics.mean(Gen4[39:42]), statistics.mean(Gen5[39:42]), statistics.mean(Gen6[39:42]), statistics.mean(Gen7[39:42]), statistics.mean(Gen8[39:42])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=1)

#######################################
# SampleNames 0.38 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[54:57]), statistics.mean(Gen1[54:57]), statistics.mean(Gen2[54:57]), statistics.mean(Gen3[54:57]), statistics.mean(Gen4[54:57]), statistics.mean(Gen5[54:57]), statistics.mean(Gen6[54:57]), statistics.mean(Gen7[54:57]), statistics.mean(Gen8[54:57])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=1)

#######################################
# SampleNames 0.38 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[69:72]), statistics.mean(Gen1[69:72]), statistics.mean(Gen2[69:72]), statistics.mean(Gen3[69:72]), statistics.mean(Gen4[69:72]), statistics.mean(Gen5[69:72]), statistics.mean(Gen6[69:72]), statistics.mean(Gen7[69:72]), statistics.mean(Gen8[69:72])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=1)

#######################################
# SampleNames 0.38 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[84:87]), statistics.mean(Gen1[84:87]), statistics.mean(Gen2[84:87]), statistics.mean(Gen3[84:87]), statistics.mean(Gen4[84:87]), statistics.mean(Gen5[84:87]), statistics.mean(Gen6[84:87]), statistics.mean(Gen7[84:87]), statistics.mean(Gen8[84:87])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=1)

#######################################
# SampleNames 0.38 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[99:102]), statistics.mean(Gen1[99:102]), statistics.mean(Gen2[99:102]), statistics.mean(Gen3[99:102]), statistics.mean(Gen4[99:102]), statistics.mean(Gen5[99:102]), statistics.mean(Gen6[99:102]), statistics.mean(Gen7[99:102]), statistics.mean(Gen8[99:102])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=1)

#######################################
# SampleNames 0.38 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[114:117]), statistics.mean(Gen1[114:117]), statistics.mean(Gen2[114:117]), statistics.mean(Gen3[114:117]), statistics.mean(Gen4[114:117]), statistics.mean(Gen5[114:117]), statistics.mean(Gen6[114:117]), statistics.mean(Gen7[114:117]), statistics.mean(Gen8[114:117])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=1)

#######################################
# SampleNames 0.38 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[129:132]), statistics.mean(Gen1[129:132]), statistics.mean(Gen2[129:132]), statistics.mean(Gen3[129:132]), statistics.mean(Gen4[129:132]), statistics.mean(Gen5[129:132]), statistics.mean(Gen6[129:132]), statistics.mean(Gen7[129:132]), statistics.mean(Gen8[129:132])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=1)

#######################################
# SampleNames 0.19 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[12:15]), statistics.mean(Gen1[12:15]), statistics.mean(Gen2[12:15]), statistics.mean(Gen3[12:15]), statistics.mean(Gen4[12:15]), statistics.mean(Gen5[12:15]), statistics.mean(Gen6[12:15]), statistics.mean(Gen7[12:15]), statistics.mean(Gen8[12:15])],
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",
    name="SampleNames 0.19"), row=1, col=1)

#######################################
# SampleNames 0.19 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[27:30]), statistics.mean(Gen1[27:30]), statistics.mean(Gen2[27:30]), statistics.mean(Gen3[27:30]), statistics.mean(Gen4[27:30]), statistics.mean(Gen5[27:30]), statistics.mean(Gen6[27:30]), statistics.mean(Gen7[27:30]), statistics.mean(Gen8[27:30])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=1)

#######################################
# SampleNames 0.19 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[42:45]), statistics.mean(Gen1[42:45]), statistics.mean(Gen2[42:45]), statistics.mean(Gen3[42:45]), statistics.mean(Gen4[42:45]), statistics.mean(Gen5[42:45]), statistics.mean(Gen6[42:45]), statistics.mean(Gen7[42:45]), statistics.mean(Gen8[42:45])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=1)

#######################################
# SampleNames 0.19 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[57:60]), statistics.mean(Gen1[57:60]), statistics.mean(Gen2[57:60]), statistics.mean(Gen3[57:60]), statistics.mean(Gen4[57:60]), statistics.mean(Gen5[57:60]), statistics.mean(Gen6[57:60]), statistics.mean(Gen7[57:60]), statistics.mean(Gen8[57:60])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=1)

#######################################
# SampleNames 0.19 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[72:75]), statistics.mean(Gen1[72:75]), statistics.mean(Gen2[72:75]), statistics.mean(Gen3[72:75]), statistics.mean(Gen4[72:75]), statistics.mean(Gen5[72:75]), statistics.mean(Gen6[72:75]), statistics.mean(Gen7[72:75]), statistics.mean(Gen8[72:75])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=1)

#######################################
# SampleNames 0.19 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[87:90]), statistics.mean(Gen1[87:90]), statistics.mean(Gen2[87:90]), statistics.mean(Gen3[87:90]), statistics.mean(Gen4[87:90]), statistics.mean(Gen5[87:90]), statistics.mean(Gen6[87:90]), statistics.mean(Gen7[87:90]), statistics.mean(Gen8[87:90])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=1)

#######################################
# SampleNames 0.19 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[102:105]), statistics.mean(Gen1[102:105]), statistics.mean(Gen2[102:105]), statistics.mean(Gen3[102:105]), statistics.mean(Gen4[102:105]), statistics.mean(Gen5[102:105]), statistics.mean(Gen6[102:105]), statistics.mean(Gen7[102:105]), statistics.mean(Gen8[102:105])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=1)

#######################################
# SampleNames 0.19 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[117:120]), statistics.mean(Gen1[117:120]), statistics.mean(Gen2[117:120]), statistics.mean(Gen3[117:120]), statistics.mean(Gen4[117:120]), statistics.mean(Gen5[117:120]), statistics.mean(Gen6[117:120]), statistics.mean(Gen7[117:120]), statistics.mean(Gen8[117:120])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=1)

#######################################
# SampleNames 0.19 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [statistics.mean(Gen0[132:135]), statistics.mean(Gen1[132:135]), statistics.mean(Gen2[132:135]), statistics.mean(Gen3[132:135]), statistics.mean(Gen4[132:135]), statistics.mean(Gen5[132:135]), statistics.mean(Gen6[132:135]), statistics.mean(Gen7[132:135]), statistics.mean(Gen8[132:135])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=1)
#########################################################################

#######################################
# SampleNames 3 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen0[0:3]), statistics.mean(Gen0[15:18]), statistics.mean(Gen0[30:33]), statistics.mean(Gen0[45:48]),
       statistics.mean(Gen0[60:63]), statistics.mean(Gen0[75:78]), statistics.mean(Gen0[90:93]), statistics.mean(Gen0[105:108]),
       statistics.mean(Gen0[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=1, col=2)

#######################################
# SampleNames 3 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen1[0:3]), statistics.mean(Gen1[15:18]), statistics.mean(Gen1[30:33]), statistics.mean(Gen1[45:48]),
       statistics.mean(Gen1[60:63]), statistics.mean(Gen1[75:78]), statistics.mean(Gen1[90:93]), statistics.mean(Gen1[105:108]),
       statistics.mean(Gen1[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=2, col=2)

#######################################
# SampleNames 3 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen2[0:3]), statistics.mean(Gen2[15:18]), statistics.mean(Gen2[30:33]), statistics.mean(Gen2[45:48]),
       statistics.mean(Gen2[60:63]), statistics.mean(Gen2[75:78]), statistics.mean(Gen2[90:93]), statistics.mean(Gen2[105:108]),
       statistics.mean(Gen2[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=3, col=2)

#######################################
# SampleNames 3 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen3[0:3]), statistics.mean(Gen3[15:18]), statistics.mean(Gen3[30:33]), statistics.mean(Gen3[45:48]),
       statistics.mean(Gen3[60:63]), statistics.mean(Gen3[75:78]), statistics.mean(Gen3[90:93]), statistics.mean(Gen3[105:108]),
       statistics.mean(Gen3[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=4, col=2)

#######################################
# SampleNames 3 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen4[0:3]), statistics.mean(Gen4[15:18]), statistics.mean(Gen4[30:33]), statistics.mean(Gen4[45:48]),
       statistics.mean(Gen4[60:63]), statistics.mean(Gen4[75:78]), statistics.mean(Gen4[90:93]), statistics.mean(Gen4[105:108]),
       statistics.mean(Gen4[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=5, col=2)

#######################################
# SampleNames 3 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen5[0:3]), statistics.mean(Gen5[15:18]), statistics.mean(Gen5[30:33]), statistics.mean(Gen5[45:48]),
       statistics.mean(Gen5[60:63]), statistics.mean(Gen5[75:78]), statistics.mean(Gen5[90:93]), statistics.mean(Gen5[105:108]),
       statistics.mean(Gen5[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=6, col=2)

#######################################
# SampleNames 3 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen6[0:3]), statistics.mean(Gen6[15:18]), statistics.mean(Gen6[30:33]), statistics.mean(Gen6[45:48]),
       statistics.mean(Gen6[60:63]), statistics.mean(Gen6[75:78]), statistics.mean(Gen6[90:93]), statistics.mean(Gen6[105:108]),
       statistics.mean(Gen6[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=7, col=2)

#######################################
# SampleNames 3 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen7[0:3]), statistics.mean(Gen7[15:18]), statistics.mean(Gen7[30:33]), statistics.mean(Gen7[45:48]),
       statistics.mean(Gen7[60:63]), statistics.mean(Gen7[75:78]), statistics.mean(Gen7[90:93]), statistics.mean(Gen7[105:108]),
       statistics.mean(Gen7[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=8, col=2)

#######################################
# SampleNames 3 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen8[0:3]), statistics.mean(Gen8[15:18]), statistics.mean(Gen8[30:33]), statistics.mean(Gen8[45:48]),
       statistics.mean(Gen8[60:63]), statistics.mean(Gen8[75:78]), statistics.mean(Gen8[90:93]), statistics.mean(Gen8[105:108]),
       statistics.mean(Gen8[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=9, col=2)

#######################################
# SampleNames 1.5 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen0[3:6]), statistics.mean(Gen0[18:21]), statistics.mean(Gen0[33:36]), statistics.mean(Gen0[48:51]),
       statistics.mean(Gen0[63:66]), statistics.mean(Gen0[78:81]), statistics.mean(Gen0[93:96]), statistics.mean(Gen0[108:111]),
       statistics.mean(Gen0[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=1, col=2)

#######################################
# SampleNames 1.5 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen1[3:6]), statistics.mean(Gen1[18:21]), statistics.mean(Gen1[33:36]), statistics.mean(Gen1[48:51]),
       statistics.mean(Gen1[63:66]), statistics.mean(Gen1[78:81]), statistics.mean(Gen1[93:96]), statistics.mean(Gen1[108:111]),
       statistics.mean(Gen1[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=2, col=2)

#######################################
# SampleNames 1.5 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen2[3:6]), statistics.mean(Gen2[18:21]), statistics.mean(Gen2[33:36]), statistics.mean(Gen2[48:51]),
       statistics.mean(Gen2[63:66]), statistics.mean(Gen2[78:81]), statistics.mean(Gen2[93:96]), statistics.mean(Gen2[108:111]),
       statistics.mean(Gen2[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=3, col=2)

#######################################
# SampleNames 1.5 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen3[3:6]), statistics.mean(Gen3[18:21]), statistics.mean(Gen3[33:36]), statistics.mean(Gen3[48:51]),
       statistics.mean(Gen3[63:66]), statistics.mean(Gen3[78:81]), statistics.mean(Gen3[93:96]), statistics.mean(Gen3[108:111]),
       statistics.mean(Gen3[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=4, col=2)

#######################################
# SampleNames 1.5 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen4[3:6]), statistics.mean(Gen4[18:21]), statistics.mean(Gen4[33:36]), statistics.mean(Gen4[48:51]),
       statistics.mean(Gen4[63:66]), statistics.mean(Gen4[78:81]), statistics.mean(Gen4[93:96]), statistics.mean(Gen4[108:111]),
       statistics.mean(Gen4[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=5, col=2)

#######################################
# SampleNames 1.5 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen5[3:6]), statistics.mean(Gen5[18:21]), statistics.mean(Gen5[33:36]), statistics.mean(Gen5[48:51]),
       statistics.mean(Gen5[63:66]), statistics.mean(Gen5[78:81]), statistics.mean(Gen5[93:96]), statistics.mean(Gen5[108:111]),
       statistics.mean(Gen5[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=6, col=2)

#######################################
# SampleNames 1.5 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen6[3:6]), statistics.mean(Gen6[18:21]), statistics.mean(Gen6[33:36]), statistics.mean(Gen6[48:51]),
       statistics.mean(Gen6[63:66]), statistics.mean(Gen6[78:81]), statistics.mean(Gen6[93:96]), statistics.mean(Gen6[108:111]),
       statistics.mean(Gen6[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=7, col=2)

#######################################
# SampleNames 1.5 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen7[3:6]), statistics.mean(Gen7[18:21]), statistics.mean(Gen7[33:36]), statistics.mean(Gen7[48:51]),
       statistics.mean(Gen7[63:66]), statistics.mean(Gen7[78:81]), statistics.mean(Gen7[93:96]), statistics.mean(Gen7[108:111]),
       statistics.mean(Gen7[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=8, col=2)

#######################################
# SampleNames 1.5 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen8[3:6]), statistics.mean(Gen8[18:21]), statistics.mean(Gen8[33:36]), statistics.mean(Gen8[48:51]),
       statistics.mean(Gen8[63:66]), statistics.mean(Gen8[78:81]), statistics.mean(Gen8[93:96]), statistics.mean(Gen8[108:111]),
       statistics.mean(Gen8[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=9, col=2)

#######################################
# SampleNames 0.75 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen0[6:9]), statistics.mean(Gen0[21:24]), statistics.mean(Gen0[36:39]), statistics.mean(Gen0[51:54]),
       statistics.mean(Gen0[66:69]), statistics.mean(Gen0[81:84]), statistics.mean(Gen0[96:99]), statistics.mean(Gen0[111:114]),
       statistics.mean(Gen0[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=1, col=2)

#######################################
# SampleNames 0.75 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen1[6:9]), statistics.mean(Gen1[21:24]), statistics.mean(Gen1[36:39]), statistics.mean(Gen1[51:54]),
       statistics.mean(Gen1[66:69]), statistics.mean(Gen1[81:84]), statistics.mean(Gen1[96:99]), statistics.mean(Gen1[111:114]),
       statistics.mean(Gen1[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=2, col=2)

#######################################
# SampleNames 0.75 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen2[6:9]), statistics.mean(Gen2[21:24]), statistics.mean(Gen2[36:39]), statistics.mean(Gen2[51:54]),
       statistics.mean(Gen2[66:69]), statistics.mean(Gen2[81:84]), statistics.mean(Gen2[96:99]), statistics.mean(Gen2[111:114]),
       statistics.mean(Gen2[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=3, col=2)

#######################################
# SampleNames 0.75 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen3[6:9]), statistics.mean(Gen3[21:24]), statistics.mean(Gen3[36:39]), statistics.mean(Gen3[51:54]),
       statistics.mean(Gen3[66:69]), statistics.mean(Gen3[81:84]), statistics.mean(Gen3[96:99]), statistics.mean(Gen3[111:114]),
       statistics.mean(Gen3[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=4, col=2)

#######################################
# SampleNames 0.75 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen4[6:9]), statistics.mean(Gen4[21:24]), statistics.mean(Gen4[36:39]), statistics.mean(Gen4[51:54]),
       statistics.mean(Gen4[66:69]), statistics.mean(Gen4[81:84]), statistics.mean(Gen4[96:99]), statistics.mean(Gen4[111:114]),
       statistics.mean(Gen4[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=5, col=2)

#######################################
# SampleNames 0.75 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen5[6:9]), statistics.mean(Gen5[21:24]), statistics.mean(Gen5[36:39]), statistics.mean(Gen5[51:54]),
       statistics.mean(Gen5[66:69]), statistics.mean(Gen5[81:84]), statistics.mean(Gen5[96:99]), statistics.mean(Gen5[111:114]),
       statistics.mean(Gen5[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=6, col=2)

#######################################
# SampleNames 0.75 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen6[6:9]), statistics.mean(Gen6[21:24]), statistics.mean(Gen6[36:39]), statistics.mean(Gen6[51:54]),
       statistics.mean(Gen6[66:69]), statistics.mean(Gen6[81:84]), statistics.mean(Gen6[96:99]), statistics.mean(Gen6[111:114]),
       statistics.mean(Gen6[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=7, col=2)

#######################################
# SampleNames 0.75 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen7[6:9]), statistics.mean(Gen7[21:24]), statistics.mean(Gen7[36:39]), statistics.mean(Gen7[51:54]),
       statistics.mean(Gen7[66:69]), statistics.mean(Gen7[81:84]), statistics.mean(Gen7[96:99]), statistics.mean(Gen7[111:114]),
       statistics.mean(Gen7[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=8, col=2)

#######################################
# SampleNames 0.75 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen8[6:9]), statistics.mean(Gen8[21:24]), statistics.mean(Gen8[36:39]), statistics.mean(Gen8[51:54]),
       statistics.mean(Gen8[66:69]), statistics.mean(Gen8[81:84]), statistics.mean(Gen8[96:99]), statistics.mean(Gen8[111:114]),
       statistics.mean(Gen8[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=9, col=2)

#######################################
# SampleNames 0.38 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen0[9:12]), statistics.mean(Gen0[24:27]), statistics.mean(Gen0[39:42]), statistics.mean(Gen0[54:57]),
       statistics.mean(Gen0[69:72]), statistics.mean(Gen0[84:87]), statistics.mean(Gen0[99:102]), statistics.mean(Gen0[114:117]),
       statistics.mean(Gen0[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=1, col=2)

#######################################
# SampleNames 0.38 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen1[9:12]), statistics.mean(Gen1[24:27]), statistics.mean(Gen1[39:42]), statistics.mean(Gen1[54:57]),
       statistics.mean(Gen1[69:72]), statistics.mean(Gen1[84:87]), statistics.mean(Gen1[99:102]), statistics.mean(Gen1[114:117]),
       statistics.mean(Gen1[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=2)

#######################################
# SampleNames 0.38 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen2[9:12]), statistics.mean(Gen2[24:27]), statistics.mean(Gen2[39:42]), statistics.mean(Gen2[54:57]),
       statistics.mean(Gen2[69:72]), statistics.mean(Gen2[84:87]), statistics.mean(Gen2[99:102]), statistics.mean(Gen2[114:117]),
       statistics.mean(Gen2[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=2)

#######################################
# SampleNames 0.38 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen3[9:12]), statistics.mean(Gen3[24:27]), statistics.mean(Gen3[39:42]), statistics.mean(Gen3[54:57]),
       statistics.mean(Gen3[69:72]), statistics.mean(Gen3[84:87]), statistics.mean(Gen3[99:102]), statistics.mean(Gen3[114:117]),
       statistics.mean(Gen3[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=2)

#######################################
# SampleNames 0.38 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen4[9:12]), statistics.mean(Gen4[24:27]), statistics.mean(Gen4[39:42]), statistics.mean(Gen4[54:57]),
       statistics.mean(Gen4[69:72]), statistics.mean(Gen4[84:87]), statistics.mean(Gen4[99:102]), statistics.mean(Gen4[114:117]),
       statistics.mean(Gen4[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=2)

#######################################
# SampleNames 0.38 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen5[9:12]), statistics.mean(Gen5[24:27]), statistics.mean(Gen5[39:42]), statistics.mean(Gen5[54:57]),
       statistics.mean(Gen5[69:72]), statistics.mean(Gen5[84:87]), statistics.mean(Gen5[99:102]), statistics.mean(Gen5[114:117]),
       statistics.mean(Gen5[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=2)

#######################################
# SampleNames 0.38 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen6[9:12]), statistics.mean(Gen6[24:27]), statistics.mean(Gen6[39:42]), statistics.mean(Gen6[54:57]),
       statistics.mean(Gen6[69:72]), statistics.mean(Gen6[84:87]), statistics.mean(Gen6[99:102]), statistics.mean(Gen6[114:117]),
       statistics.mean(Gen6[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=2)

#######################################
# SampleNames 0.38 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen7[9:12]), statistics.mean(Gen7[24:27]), statistics.mean(Gen7[39:42]), statistics.mean(Gen7[54:57]),
       statistics.mean(Gen7[69:72]), statistics.mean(Gen7[84:87]), statistics.mean(Gen7[99:102]), statistics.mean(Gen7[114:117]),
       statistics.mean(Gen7[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=2)

#######################################
# SampleNames 0.38 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen8[9:12]), statistics.mean(Gen8[24:27]), statistics.mean(Gen8[39:42]), statistics.mean(Gen8[54:57]),
       statistics.mean(Gen8[69:72]), statistics.mean(Gen8[84:87]), statistics.mean(Gen8[99:102]), statistics.mean(Gen8[114:117]),
       statistics.mean(Gen8[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=2)

#######################################
# SampleNames 0.19 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen0[12:15]), statistics.mean(Gen0[27:30]), statistics.mean(Gen0[42:45]), statistics.mean(Gen0[57:60]),
       statistics.mean(Gen0[72:75]), statistics.mean(Gen0[87:90]), statistics.mean(Gen0[102:105]), statistics.mean(Gen0[117:120]),
       statistics.mean(Gen0[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=1, col=2)

#######################################
# SampleNames 0.19 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen1[12:15]), statistics.mean(Gen1[27:30]), statistics.mean(Gen1[42:45]), statistics.mean(Gen1[57:60]),
       statistics.mean(Gen1[72:75]), statistics.mean(Gen1[87:90]), statistics.mean(Gen1[102:105]), statistics.mean(Gen1[117:120]),
       statistics.mean(Gen1[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=2)

#######################################
# SampleNames 0.19 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen2[12:15]), statistics.mean(Gen2[27:30]), statistics.mean(Gen2[42:45]), statistics.mean(Gen2[57:60]),
       statistics.mean(Gen2[72:75]), statistics.mean(Gen2[87:90]), statistics.mean(Gen2[102:105]), statistics.mean(Gen2[117:120]),
       statistics.mean(Gen2[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=2)

#######################################
# SampleNames 0.19 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen3[12:15]), statistics.mean(Gen3[27:30]), statistics.mean(Gen3[42:45]), statistics.mean(Gen3[57:60]),
       statistics.mean(Gen3[72:75]), statistics.mean(Gen3[87:90]), statistics.mean(Gen3[102:105]), statistics.mean(Gen3[117:120]),
       statistics.mean(Gen3[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=2)

#######################################
# SampleNames 0.19 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen4[12:15]), statistics.mean(Gen4[27:30]), statistics.mean(Gen4[42:45]), statistics.mean(Gen4[57:60]),
       statistics.mean(Gen4[72:75]), statistics.mean(Gen4[87:90]), statistics.mean(Gen4[102:105]), statistics.mean(Gen4[117:120]),
       statistics.mean(Gen4[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=2)

#######################################
# SampleNames 0.19 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen5[12:15]), statistics.mean(Gen5[27:30]), statistics.mean(Gen5[42:45]), statistics.mean(Gen5[57:60]),
       statistics.mean(Gen5[72:75]), statistics.mean(Gen5[87:90]), statistics.mean(Gen5[102:105]), statistics.mean(Gen5[117:120]),
       statistics.mean(Gen5[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=2)

#######################################
# SampleNames 0.19 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen6[12:15]), statistics.mean(Gen6[27:30]), statistics.mean(Gen6[42:45]), statistics.mean(Gen6[57:60]),
       statistics.mean(Gen6[72:75]), statistics.mean(Gen6[87:90]), statistics.mean(Gen6[102:105]), statistics.mean(Gen6[117:120]),
       statistics.mean(Gen6[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=2)

#######################################
# SampleNames 0.19 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen7[12:15]), statistics.mean(Gen7[27:30]), statistics.mean(Gen7[42:45]), statistics.mean(Gen7[57:60]),
       statistics.mean(Gen7[72:75]), statistics.mean(Gen7[87:90]), statistics.mean(Gen7[102:105]), statistics.mean(Gen7[117:120]),
       statistics.mean(Gen7[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=2)

#######################################
# SampleNames 0.19 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[statistics.mean(Gen8[12:15]), statistics.mean(Gen8[27:30]), statistics.mean(Gen8[42:45]), statistics.mean(Gen8[57:60]),
       statistics.mean(Gen8[72:75]), statistics.mean(Gen8[87:90]), statistics.mean(Gen8[102:105]), statistics.mean(Gen8[117:120]),
       statistics.mean(Gen8[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=2)

########################################
#######################################
# SampleNames 3 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[0:3]), stats.sem(Gen1[0:3]), stats.sem(Gen2[0:3]), stats.sem(Gen3[0:3]), stats.sem(Gen4[0:3]), stats.sem(Gen5[0:3]), stats.sem(Gen6[0:3]), stats.sem(Gen7[0:3]), stats.sem(Gen8[0:3])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=1, col=3)

#######################################
# SampleNames 3 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[15:18]), stats.sem(Gen1[15:18]), stats.sem(Gen2[15:18]), stats.sem(Gen3[15:18]), stats.sem(Gen4[15:18]), stats.sem(Gen5[15:18]), stats.sem(Gen6[15:18]), stats.sem(Gen7[15:18]), stats.sem(Gen8[15:18])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=2, col=3)

#######################################
# SampleNames 3 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[30:33]), stats.sem(Gen1[30:33]), stats.sem(Gen2[30:33]), stats.sem(Gen3[30:33]), stats.sem(Gen4[30:33]), stats.sem(Gen5[30:33]), stats.sem(Gen6[30:33]), stats.sem(Gen7[30:33]), stats.sem(Gen8[30:33])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=3, col=3)

#######################################
# SampleNames 3 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[45:48]), stats.sem(Gen1[45:48]), stats.sem(Gen2[45:48]), stats.sem(Gen3[45:48]), stats.sem(Gen4[45:48]), stats.sem(Gen5[45:48]), stats.sem(Gen6[45:48]), stats.sem(Gen7[45:48]), stats.sem(Gen8[45:48])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=4, col=3)

#######################################
# SampleNames 3 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[60:63]), stats.sem(Gen1[60:63]), stats.sem(Gen2[60:63]), stats.sem(Gen3[60:63]), stats.sem(Gen4[60:63]), stats.sem(Gen5[60:63]), stats.sem(Gen6[60:63]), stats.sem(Gen7[60:63]), stats.sem(Gen8[60:63])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=5, col=3)

#######################################
# SampleNames 3 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[75:78]), stats.sem(Gen1[75:78]), stats.sem(Gen2[75:78]), stats.sem(Gen3[75:78]), stats.sem(Gen4[75:78]), stats.sem(Gen5[75:78]), stats.sem(Gen6[75:78]), stats.sem(Gen7[75:78]), stats.sem(Gen8[75:78])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=6, col=3)

#######################################
# SampleNames 3 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[90:93]), stats.sem(Gen1[90:93]), stats.sem(Gen2[90:93]), stats.sem(Gen3[90:93]), stats.sem(Gen4[90:93]), stats.sem(Gen5[90:93]), stats.sem(Gen6[90:93]), stats.sem(Gen7[90:93]), stats.sem(Gen8[90:93])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=7, col=3)

#######################################
# SampleNames 3 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[105:108]), stats.sem(Gen1[105:108]), stats.sem(Gen2[105:108]), stats.sem(Gen3[105:108]), stats.sem(Gen4[105:108]), stats.sem(Gen5[105:108]), stats.sem(Gen6[105:108]), stats.sem(Gen7[105:108]), stats.sem(Gen8[105:108])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=8, col=3)

#######################################
# SampleNames 3 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[120:123]), stats.sem(Gen1[120:123]), stats.sem(Gen2[120:123]), stats.sem(Gen3[120:123]), stats.sem(Gen4[120:123]), stats.sem(Gen5[120:123]), stats.sem(Gen6[120:123]), stats.sem(Gen7[120:123]), stats.sem(Gen8[120:123])],
    showlegend=False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=9, col=3)

#######################################
# SampleNames 1.5 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[3:6]), stats.sem(Gen1[3:6]), stats.sem(Gen2[3:6]), stats.sem(Gen3[3:6]), stats.sem(Gen4[3:6]), stats.sem(Gen5[3:6]), stats.sem(Gen6[3:6]), stats.sem(Gen7[3:6]), stats.sem(Gen8[3:6])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=1, col=3)

#######################################
# SampleNames 1.5 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[18:21]), stats.sem(Gen1[18:21]), stats.sem(Gen2[18:21]), stats.sem(Gen3[18:21]), stats.sem(Gen4[18:21]), stats.sem(Gen5[18:21]), stats.sem(Gen6[18:21]), stats.sem(Gen7[18:21]), stats.sem(Gen8[18:21])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=2, col=3)

#######################################
# SampleNames 1.5 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[33:36]), stats.sem(Gen1[33:36]), stats.sem(Gen2[33:36]), stats.sem(Gen3[33:36]), stats.sem(Gen4[33:36]), stats.sem(Gen5[33:36]), stats.sem(Gen6[33:36]), stats.sem(Gen7[33:36]), stats.sem(Gen8[33:36])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=3, col=3)

#######################################
# SampleNames 1.5 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[48:51]), stats.sem(Gen1[48:51]), stats.sem(Gen2[48:51]), stats.sem(Gen3[48:51]), stats.sem(Gen4[48:51]), stats.sem(Gen5[48:51]), stats.sem(Gen6[48:51]), stats.sem(Gen7[48:51]), stats.sem(Gen8[48:51])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=4, col=3)

#######################################
# SampleNames 1.5 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[63:66]), stats.sem(Gen1[63:66]), stats.sem(Gen2[63:66]), stats.sem(Gen3[63:66]), stats.sem(Gen4[63:66]), stats.sem(Gen5[63:66]), stats.sem(Gen6[63:66]), stats.sem(Gen7[63:66]), stats.sem(Gen8[63:66])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=5, col=3)

#######################################
# SampleNames 1.5 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[78:81]), stats.sem(Gen1[78:81]), stats.sem(Gen2[78:81]), stats.sem(Gen3[78:81]), stats.sem(Gen4[78:81]), stats.sem(Gen5[78:81]), stats.sem(Gen6[78:81]), stats.sem(Gen7[78:81]), stats.sem(Gen8[78:81])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=6, col=3)

#######################################
# SampleNames 1.5 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[93:96]), stats.sem(Gen1[93:96]), stats.sem(Gen2[93:96]), stats.sem(Gen3[93:96]), stats.sem(Gen4[93:96]), stats.sem(Gen5[93:96]), stats.sem(Gen6[93:96]), stats.sem(Gen7[93:96]), stats.sem(Gen8[93:96])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=7, col=3)

#######################################
# SampleNames 1.5 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[108:111]), stats.sem(Gen1[108:111]), stats.sem(Gen2[108:111]), stats.sem(Gen3[108:111]), stats.sem(Gen4[108:111]), stats.sem(Gen5[108:111]), stats.sem(Gen6[108:111]), stats.sem(Gen7[108:111]), stats.sem(Gen8[108:111])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=8, col=3)

#######################################
# SampleNames 1.5 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[123:126]), stats.sem(Gen1[123:126]), stats.sem(Gen2[123:126]), stats.sem(Gen3[123:126]), stats.sem(Gen4[123:126]), stats.sem(Gen5[123:126]), stats.sem(Gen6[123:126]), stats.sem(Gen7[123:126]), stats.sem(Gen8[123:126])],
    showlegend=False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=9, col=3)

#######################################
# SampleNames 0.75 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[6:9]), stats.sem(Gen1[6:9]), stats.sem(Gen2[6:9]), stats.sem(Gen3[6:9]), stats.sem(Gen4[6:9]), stats.sem(Gen5[6:9]), stats.sem(Gen6[6:9]), stats.sem(Gen7[6:9]), stats.sem(Gen8[6:9])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=1, col=3)

#######################################
# SampleNames 0.75 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[21:24]), stats.sem(Gen1[21:24]), stats.sem(Gen2[21:24]), stats.sem(Gen3[21:24]), stats.sem(Gen4[21:24]), stats.sem(Gen5[21:24]), stats.sem(Gen6[21:24]), stats.sem(Gen7[21:24]), stats.sem(Gen8[21:24])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=2, col=3)

#######################################
# SampleNames 0.75 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[36:39]), stats.sem(Gen1[36:39]), stats.sem(Gen2[36:39]), stats.sem(Gen3[36:39]), stats.sem(Gen4[36:39]), stats.sem(Gen5[36:39]), stats.sem(Gen6[36:39]), stats.sem(Gen7[36:39]), stats.sem(Gen8[36:39])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=3, col=3)

#######################################
# SampleNames 0.75 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[51:54]), stats.sem(Gen1[51:54]), stats.sem(Gen2[51:54]), stats.sem(Gen3[51:54]), stats.sem(Gen4[51:54]), stats.sem(Gen5[51:54]), stats.sem(Gen6[51:54]), stats.sem(Gen7[51:54]), stats.sem(Gen8[51:54])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=4, col=3)

#######################################
# SampleNames 0.75 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[66:69]), stats.sem(Gen1[66:69]), stats.sem(Gen2[66:69]), stats.sem(Gen3[66:69]), stats.sem(Gen4[66:69]), stats.sem(Gen5[66:69]), stats.sem(Gen6[66:69]), stats.sem(Gen7[66:69]), stats.sem(Gen8[66:69])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=5, col=3)

#######################################
# SampleNames 0.75 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[81:84]), stats.sem(Gen1[81:84]), stats.sem(Gen2[81:84]), stats.sem(Gen3[81:84]), stats.sem(Gen4[81:84]), stats.sem(Gen5[81:84]), stats.sem(Gen6[81:84]), stats.sem(Gen7[81:84]), stats.sem(Gen8[81:84])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=6, col=3)

#######################################
# SampleNames 0.75 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[96:99]), stats.sem(Gen1[96:99]), stats.sem(Gen2[96:99]), stats.sem(Gen3[96:99]), stats.sem(Gen4[96:99]), stats.sem(Gen5[96:99]), stats.sem(Gen6[96:99]), stats.sem(Gen7[96:99]), stats.sem(Gen8[96:99])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=7, col=3)

#######################################
# SampleNames 0.75 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[111:114]), stats.sem(Gen1[111:114]), stats.sem(Gen2[111:114]), stats.sem(Gen3[111:114]), stats.sem(Gen4[111:114]), stats.sem(Gen5[111:114]), stats.sem(Gen6[111:114]), stats.sem(Gen7[111:114]), stats.sem(Gen8[111:114])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=8, col=3)

#######################################
# SampleNames 0.75 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[126:129]), stats.sem(Gen1[126:129]), stats.sem(Gen2[126:129]), stats.sem(Gen3[126:129]), stats.sem(Gen4[126:129]), stats.sem(Gen5[126:129]), stats.sem(Gen6[126:129]), stats.sem(Gen7[126:129]), stats.sem(Gen8[126:129])],
    showlegend=False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=9, col=3)

#######################################
# SampleNames 0.38 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[9:12]), stats.sem(Gen1[9:12]), stats.sem(Gen2[9:12]), stats.sem(Gen3[9:12]), stats.sem(Gen4[9:12]), stats.sem(Gen5[9:12]), stats.sem(Gen6[9:12]), stats.sem(Gen7[9:12]), stats.sem(Gen8[9:12])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=1, col=3)

#######################################
# SampleNames 0.38 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[24:27]), stats.sem(Gen1[24:27]), stats.sem(Gen2[24:27]), stats.sem(Gen3[24:27]), stats.sem(Gen4[24:27]), stats.sem(Gen5[24:27]), stats.sem(Gen6[24:27]), stats.sem(Gen7[24:27]), stats.sem(Gen8[24:27])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=3)

#######################################
# SampleNames 0.38 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[39:42]), stats.sem(Gen1[39:42]), stats.sem(Gen2[39:42]), stats.sem(Gen3[39:42]), stats.sem(Gen4[39:42]), stats.sem(Gen5[39:42]), stats.sem(Gen6[39:42]), stats.sem(Gen7[39:42]), stats.sem(Gen8[39:42])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=3)

#######################################
# SampleNames 0.38 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[54:57]), stats.sem(Gen1[54:57]), stats.sem(Gen2[54:57]), stats.sem(Gen3[54:57]), stats.sem(Gen4[54:57]), stats.sem(Gen5[54:57]), stats.sem(Gen6[54:57]), stats.sem(Gen7[54:57]), stats.sem(Gen8[54:57])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=3)

#######################################
# SampleNames 0.38 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[69:72]), stats.sem(Gen1[69:72]), stats.sem(Gen2[69:72]), stats.sem(Gen3[69:72]), stats.sem(Gen4[69:72]), stats.sem(Gen5[69:72]), stats.sem(Gen6[69:72]), stats.sem(Gen7[69:72]), stats.sem(Gen8[69:72])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=3)

#######################################
# SampleNames 0.38 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[84:87]), stats.sem(Gen1[84:87]), stats.sem(Gen2[84:87]), stats.sem(Gen3[84:87]), stats.sem(Gen4[84:87]), stats.sem(Gen5[84:87]), stats.sem(Gen6[84:87]), stats.sem(Gen7[84:87]), stats.sem(Gen8[84:87])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=3)

#######################################
# SampleNames 0.38 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[99:102]), stats.sem(Gen1[99:102]), stats.sem(Gen2[99:102]), stats.sem(Gen3[99:102]), stats.sem(Gen4[99:102]), stats.sem(Gen5[99:102]), stats.sem(Gen6[99:102]), stats.sem(Gen7[99:102]), stats.sem(Gen8[99:102])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=3)

#######################################
# SampleNames 0.38 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[114:117]), stats.sem(Gen1[114:117]), stats.sem(Gen2[114:117]), stats.sem(Gen3[114:117]), stats.sem(Gen4[114:117]), stats.sem(Gen5[114:117]), stats.sem(Gen6[114:117]), stats.sem(Gen7[114:117]), stats.sem(Gen8[114:117])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=3)

#######################################
# SampleNames 0.38 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[129:132]), stats.sem(Gen1[129:132]), stats.sem(Gen2[129:132]), stats.sem(Gen3[129:132]), stats.sem(Gen4[129:132]), stats.sem(Gen5[129:132]), stats.sem(Gen6[129:132]), stats.sem(Gen7[129:132]), stats.sem(Gen8[129:132])],
    showlegend=False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=3)

#######################################
# SampleNames 0.19 Time-Period 19.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[12:15]), stats.sem(Gen1[12:15]), stats.sem(Gen2[12:15]), stats.sem(Gen3[12:15]), stats.sem(Gen4[12:15]), stats.sem(Gen5[12:15]), stats.sem(Gen6[12:15]), stats.sem(Gen7[12:15]), stats.sem(Gen8[12:15])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=1, col=3)

#######################################
# SampleNames 0.19 Time-Period 27.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[27:30]), stats.sem(Gen1[27:30]), stats.sem(Gen2[27:30]), stats.sem(Gen3[27:30]), stats.sem(Gen4[27:30]), stats.sem(Gen5[27:30]), stats.sem(Gen6[27:30]), stats.sem(Gen7[27:30]), stats.sem(Gen8[27:30])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=3)

#######################################
# SampleNames 0.19 Time-Period 44
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[42:45]), stats.sem(Gen1[42:45]), stats.sem(Gen2[42:45]), stats.sem(Gen3[42:45]), stats.sem(Gen4[42:45]), stats.sem(Gen5[42:45]), stats.sem(Gen6[42:45]), stats.sem(Gen7[42:45]), stats.sem(Gen8[42:45])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=3)

#######################################
# SampleNames 0.19 Time-Period 52
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[57:60]), stats.sem(Gen1[57:60]), stats.sem(Gen2[57:60]), stats.sem(Gen3[57:60]), stats.sem(Gen4[57:60]), stats.sem(Gen5[57:60]), stats.sem(Gen6[57:60]), stats.sem(Gen7[57:60]), stats.sem(Gen8[57:60])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=3)

#######################################
# SampleNames 0.19 Time-Period 68
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[72:75]), stats.sem(Gen1[72:75]), stats.sem(Gen2[72:75]), stats.sem(Gen3[72:75]), stats.sem(Gen4[72:75]), stats.sem(Gen5[72:75]), stats.sem(Gen6[72:75]), stats.sem(Gen7[72:75]), stats.sem(Gen8[72:75])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=3)

#######################################
# SampleNames 0.19 Time-Period 80.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[87:90]), stats.sem(Gen1[87:90]), stats.sem(Gen2[87:90]), stats.sem(Gen3[87:90]), stats.sem(Gen4[87:90]), stats.sem(Gen5[87:90]), stats.sem(Gen6[87:90]), stats.sem(Gen7[87:90]), stats.sem(Gen8[87:90])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=3)

#######################################
# SampleNames 0.19 Time-Period 95.5
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[102:105]), stats.sem(Gen1[102:105]), stats.sem(Gen2[102:105]), stats.sem(Gen3[102:105]), stats.sem(Gen4[102:105]), stats.sem(Gen5[102:105]), stats.sem(Gen6[102:105]), stats.sem(Gen7[102:105]), stats.sem(Gen8[102:105])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=3)

#######################################
# SampleNames 0.19 Time-Period 124
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[117:120]), stats.sem(Gen1[117:120]), stats.sem(Gen2[117:120]), stats.sem(Gen3[117:120]), stats.sem(Gen4[117:120]), stats.sem(Gen5[117:120]), stats.sem(Gen6[117:120]), stats.sem(Gen7[117:120]), stats.sem(Gen8[117:120])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=3)

#######################################
# SampleNames 0.19 Time-Period 140
#######################################
fig.add_trace(go.Scatter(
    x = [genTitle[0], genTitle[1], genTitle[2], genTitle[3], genTitle[4], genTitle[5], genTitle[6], genTitle[7], genTitle[8]],
    y = [stats.sem(Gen0[132:135]), stats.sem(Gen1[132:135]), stats.sem(Gen2[132:135]), stats.sem(Gen3[132:135]), stats.sem(Gen4[132:135]), stats.sem(Gen5[132:135]), stats.sem(Gen6[132:135]), stats.sem(Gen7[132:135]), stats.sem(Gen8[132:135])],
    showlegend=False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=3)
#######################################
#######################################
# SampleNames 3 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen0[0:3]), stats.sem(Gen0[15:18]), stats.sem(Gen0[30:33]), stats.sem(Gen0[45:48]),
       stats.sem(Gen0[60:63]), stats.sem(Gen0[75:78]), stats.sem(Gen0[90:93]), stats.sem(Gen0[105:108]),
       stats.sem(Gen0[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=1, col=4)

#######################################
# SampleNames 3 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen1[0:3]), stats.sem(Gen1[15:18]), stats.sem(Gen1[30:33]), stats.sem(Gen1[45:48]),
       stats.sem(Gen1[60:63]), stats.sem(Gen1[75:78]), stats.sem(Gen1[90:93]), stats.sem(Gen1[105:108]),
       stats.sem(Gen1[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=2, col=4)

#######################################
# SampleNames 3 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen2[0:3]), stats.sem(Gen2[15:18]), stats.sem(Gen2[30:33]), stats.sem(Gen2[45:48]),
       stats.sem(Gen2[60:63]), stats.sem(Gen2[75:78]), stats.sem(Gen2[90:93]), stats.sem(Gen2[105:108]),
       stats.sem(Gen2[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=3, col=4)

#######################################
# SampleNames 3 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen3[0:3]), stats.sem(Gen3[15:18]), stats.sem(Gen3[30:33]), stats.sem(Gen3[45:48]),
       stats.sem(Gen3[60:63]), stats.sem(Gen3[75:78]), stats.sem(Gen3[90:93]), stats.sem(Gen3[105:108]),
       stats.sem(Gen3[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=4, col=4)

#######################################
# SampleNames 3 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen4[0:3]), stats.sem(Gen4[15:18]), stats.sem(Gen4[30:33]), stats.sem(Gen4[45:48]),
       stats.sem(Gen4[60:63]), stats.sem(Gen4[75:78]), stats.sem(Gen4[90:93]), stats.sem(Gen4[105:108]),
       stats.sem(Gen4[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=5, col=4)

#######################################
# SampleNames 3 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen5[0:3]), stats.sem(Gen5[15:18]), stats.sem(Gen5[30:33]), stats.sem(Gen5[45:48]),
       stats.sem(Gen5[60:63]), stats.sem(Gen5[75:78]), stats.sem(Gen5[90:93]), stats.sem(Gen5[105:108]),
       stats.sem(Gen5[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=6, col=4)

#######################################
# SampleNames 3 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen6[0:3]), stats.sem(Gen6[15:18]), stats.sem(Gen6[30:33]), stats.sem(Gen6[45:48]),
       stats.sem(Gen6[60:63]), stats.sem(Gen6[75:78]), stats.sem(Gen6[90:93]), stats.sem(Gen6[105:108]),
       stats.sem(Gen6[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=7, col=4)

#######################################
# SampleNames 3 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen7[0:3]), stats.sem(Gen7[15:18]), stats.sem(Gen7[30:33]), stats.sem(Gen7[45:48]),
       stats.sem(Gen7[60:63]), stats.sem(Gen7[75:78]), stats.sem(Gen7[90:93]), stats.sem(Gen7[105:108]),
       stats.sem(Gen7[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=8, col=4)

#######################################
# SampleNames 3 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen8[0:3]), stats.sem(Gen8[15:18]), stats.sem(Gen8[30:33]), stats.sem(Gen8[45:48]),
       stats.sem(Gen8[60:63]), stats.sem(Gen8[75:78]), stats.sem(Gen8[90:93]), stats.sem(Gen8[105:108]),
       stats.sem(Gen8[120:123])],
    showlegend = False,
    marker=dict(color="blue", size=11, symbol="star-square"),
    mode="lines + markers",), row=9, col=4)

#######################################
# SampleNames 1.5 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen0[3:6]), stats.sem(Gen0[18:21]), stats.sem(Gen0[33:36]), stats.sem(Gen0[48:51]),
       stats.sem(Gen0[63:66]), stats.sem(Gen0[78:81]), stats.sem(Gen0[93:96]), stats.sem(Gen0[108:111]),
       stats.sem(Gen0[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=1, col=4)

#######################################
# SampleNames 1.5 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen1[3:6]), stats.sem(Gen1[18:21]), stats.sem(Gen1[33:36]), stats.sem(Gen1[48:51]),
       stats.sem(Gen1[63:66]), stats.sem(Gen1[78:81]), stats.sem(Gen1[93:96]), stats.sem(Gen1[108:111]),
       stats.sem(Gen1[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=2, col=4)

#######################################
# SampleNames 1.5 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen2[3:6]), stats.sem(Gen2[18:21]), stats.sem(Gen2[33:36]), stats.sem(Gen2[48:51]),
       stats.sem(Gen2[63:66]), stats.sem(Gen2[78:81]), stats.sem(Gen2[93:96]), stats.sem(Gen2[108:111]),
       stats.sem(Gen2[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=3, col=4)

#######################################
# SampleNames 1.5 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen3[3:6]), stats.sem(Gen3[18:21]), stats.sem(Gen3[33:36]), stats.sem(Gen3[48:51]),
       stats.sem(Gen3[63:66]), stats.sem(Gen3[78:81]), stats.sem(Gen3[93:96]), stats.sem(Gen3[108:111]),
       stats.sem(Gen3[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=4, col=4)

#######################################
# SampleNames 1.5 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen4[3:6]), stats.sem(Gen4[18:21]), stats.sem(Gen4[33:36]), stats.sem(Gen4[48:51]),
       stats.sem(Gen4[63:66]), stats.sem(Gen4[78:81]), stats.sem(Gen4[93:96]), stats.sem(Gen4[108:111]),
       stats.sem(Gen4[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=5, col=4)

#######################################
# SampleNames 1.5 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen5[3:6]), stats.sem(Gen5[18:21]), stats.sem(Gen5[33:36]), stats.sem(Gen5[48:51]),
       stats.sem(Gen5[63:66]), stats.sem(Gen5[78:81]), stats.sem(Gen5[93:96]), stats.sem(Gen5[108:111]),
       stats.sem(Gen5[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=6, col=4)

#######################################
# SampleNames 1.5 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen6[3:6]), stats.sem(Gen6[18:21]), stats.sem(Gen6[33:36]), stats.sem(Gen6[48:51]),
       stats.sem(Gen6[63:66]), stats.sem(Gen6[78:81]), stats.sem(Gen6[93:96]), stats.sem(Gen6[108:111]),
       stats.sem(Gen6[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=7, col=4)

#######################################
# SampleNames 1.5 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen7[3:6]), stats.sem(Gen7[18:21]), stats.sem(Gen7[33:36]), stats.sem(Gen7[48:51]),
       stats.sem(Gen7[63:66]), stats.sem(Gen7[78:81]), stats.sem(Gen7[93:96]), stats.sem(Gen7[108:111]),
       stats.sem(Gen7[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=8, col=4)

#######################################
# SampleNames 1.5 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen8[3:6]), stats.sem(Gen8[18:21]), stats.sem(Gen8[33:36]), stats.sem(Gen8[48:51]),
       stats.sem(Gen8[63:66]), stats.sem(Gen8[78:81]), stats.sem(Gen8[93:96]), stats.sem(Gen8[108:111]),
       stats.sem(Gen8[123:126])],
    showlegend = False,
    marker=dict(color="red", size=8, symbol="star-square"),
    mode="lines + markers",), row=9, col=4)

#######################################
# SampleNames 0.75 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen0[6:9]), stats.sem(Gen0[21:24]), stats.sem(Gen0[36:39]), stats.sem(Gen0[51:54]),
       stats.sem(Gen0[66:69]), stats.sem(Gen0[81:84]), stats.sem(Gen0[96:99]), stats.sem(Gen0[111:114]),
       stats.sem(Gen0[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=1, col=4)

#######################################
# SampleNames 0.75 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen1[6:9]), stats.sem(Gen1[21:24]), stats.sem(Gen1[36:39]), stats.sem(Gen1[51:54]),
       stats.sem(Gen1[66:69]), stats.sem(Gen1[81:84]), stats.sem(Gen1[96:99]), stats.sem(Gen1[111:114]),
       stats.sem(Gen1[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=2, col=4)

#######################################
# SampleNames 0.75 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen2[6:9]), stats.sem(Gen2[21:24]), stats.sem(Gen2[36:39]), stats.sem(Gen2[51:54]),
       stats.sem(Gen2[66:69]), stats.sem(Gen2[81:84]), stats.sem(Gen2[96:99]), stats.sem(Gen2[111:114]),
       stats.sem(Gen2[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=3, col=4)

#######################################
# SampleNames 0.75 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen3[6:9]), stats.sem(Gen3[21:24]), stats.sem(Gen3[36:39]), stats.sem(Gen3[51:54]),
       stats.sem(Gen3[66:69]), stats.sem(Gen3[81:84]), stats.sem(Gen3[96:99]), stats.sem(Gen3[111:114]),
       stats.sem(Gen3[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=4, col=4)

#######################################
# SampleNames 0.75 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen4[6:9]), stats.sem(Gen4[21:24]), stats.sem(Gen4[36:39]), stats.sem(Gen4[51:54]),
       stats.sem(Gen4[66:69]), stats.sem(Gen4[81:84]), stats.sem(Gen4[96:99]), stats.sem(Gen4[111:114]),
       stats.sem(Gen4[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=5, col=4)

#######################################
# SampleNames 0.75 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen5[6:9]), stats.sem(Gen5[21:24]), stats.sem(Gen5[36:39]), stats.sem(Gen5[51:54]),
       stats.sem(Gen5[66:69]), stats.sem(Gen5[81:84]), stats.sem(Gen5[96:99]), stats.sem(Gen5[111:114]),
       stats.sem(Gen5[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=6, col=4)

#######################################
# SampleNames 0.75 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen6[6:9]), stats.sem(Gen6[21:24]), stats.sem(Gen6[36:39]), stats.sem(Gen6[51:54]),
       stats.sem(Gen6[66:69]), stats.sem(Gen6[81:84]), stats.sem(Gen6[96:99]), stats.sem(Gen6[111:114]),
       stats.sem(Gen6[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=7, col=4)

#######################################
# SampleNames 0.75 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen7[6:9]), stats.sem(Gen7[21:24]), stats.sem(Gen7[36:39]), stats.sem(Gen7[51:54]),
       stats.sem(Gen7[66:69]), stats.sem(Gen7[81:84]), stats.sem(Gen7[96:99]), stats.sem(Gen7[111:114]),
       stats.sem(Gen7[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=8, col=4)

#######################################
# SampleNames 0.75 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen8[6:9]), stats.sem(Gen8[21:24]), stats.sem(Gen8[36:39]), stats.sem(Gen8[51:54]),
       stats.sem(Gen8[66:69]), stats.sem(Gen8[81:84]), stats.sem(Gen8[96:99]), stats.sem(Gen8[111:114]),
       stats.sem(Gen8[126:129])],
    showlegend = False,
    marker=dict(color="green", size=7, symbol="star-square"),
    mode="lines + markers",), row=9, col=4)

#######################################
# SampleNames 0.38 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen0[9:12]), stats.sem(Gen0[24:27]), stats.sem(Gen0[39:42]), stats.sem(Gen0[54:57]),
       stats.sem(Gen0[69:72]), stats.sem(Gen0[84:87]), stats.sem(Gen0[99:102]), stats.sem(Gen0[114:117]),
       stats.sem(Gen0[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=1, col=4)

#######################################
# SampleNames 0.38 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen1[9:12]), stats.sem(Gen1[24:27]), stats.sem(Gen1[39:42]), stats.sem(Gen1[54:57]),
       stats.sem(Gen1[69:72]), stats.sem(Gen1[84:87]), stats.sem(Gen1[99:102]), stats.sem(Gen1[114:117]),
       stats.sem(Gen1[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=4)

#######################################
# SampleNames 0.38 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen2[9:12]), stats.sem(Gen2[24:27]), stats.sem(Gen2[39:42]), stats.sem(Gen2[54:57]),
       stats.sem(Gen2[69:72]), stats.sem(Gen2[84:87]), stats.sem(Gen2[99:102]), stats.sem(Gen2[114:117]),
       stats.sem(Gen2[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=4)

#######################################
# SampleNames 0.38 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen3[9:12]), stats.sem(Gen3[24:27]), stats.sem(Gen3[39:42]), stats.sem(Gen3[54:57]),
       stats.sem(Gen3[69:72]), stats.sem(Gen3[84:87]), stats.sem(Gen3[99:102]), stats.sem(Gen3[114:117]),
       stats.sem(Gen3[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=4)

#######################################
# SampleNames 0.38 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen4[9:12]), stats.sem(Gen4[24:27]), stats.sem(Gen4[39:42]), stats.sem(Gen4[54:57]),
       stats.sem(Gen4[69:72]), stats.sem(Gen4[84:87]), stats.sem(Gen4[99:102]), stats.sem(Gen4[114:117]),
       stats.sem(Gen4[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=4)

#######################################
# SampleNames 0.38 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen5[9:12]), stats.sem(Gen5[24:27]), stats.sem(Gen5[39:42]), stats.sem(Gen5[54:57]),
       stats.sem(Gen5[69:72]), stats.sem(Gen5[84:87]), stats.sem(Gen5[99:102]), stats.sem(Gen5[114:117]),
       stats.sem(Gen5[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=4)

#######################################
# SampleNames 0.38 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen6[9:12]), stats.sem(Gen6[24:27]), stats.sem(Gen6[39:42]), stats.sem(Gen6[54:57]),
       stats.sem(Gen6[69:72]), stats.sem(Gen6[84:87]), stats.sem(Gen6[99:102]), stats.sem(Gen6[114:117]),
       stats.sem(Gen6[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=4)

#######################################
# SampleNames 0.38 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen7[9:12]), stats.sem(Gen7[24:27]), stats.sem(Gen7[39:42]), stats.sem(Gen7[54:57]),
       stats.sem(Gen7[69:72]), stats.sem(Gen7[84:87]), stats.sem(Gen7[99:102]), stats.sem(Gen7[114:117]),
       stats.sem(Gen7[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=4)

#######################################
# SampleNames 0.38 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen8[9:12]), stats.sem(Gen8[24:27]), stats.sem(Gen8[39:42]), stats.sem(Gen8[54:57]),
       stats.sem(Gen8[69:72]), stats.sem(Gen8[84:87]), stats.sem(Gen8[99:102]), stats.sem(Gen8[114:117]),
       stats.sem(Gen8[129:132])],
    showlegend = False,
    marker=dict(color="orange", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=4)

#######################################
# SampleNames 0.19 Generation 0
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen0[12:15]), stats.sem(Gen0[27:30]), stats.sem(Gen0[42:45]), stats.sem(Gen0[57:60]),
       stats.sem(Gen0[72:75]), stats.sem(Gen0[87:90]), stats.sem(Gen0[102:105]), stats.sem(Gen0[117:120]),
       stats.sem(Gen0[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=1, col=4)

#######################################
# SampleNames 0.19 Generation 1
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen1[12:15]), stats.sem(Gen1[27:30]), stats.sem(Gen1[42:45]), stats.sem(Gen1[57:60]),
       stats.sem(Gen1[72:75]), stats.sem(Gen1[87:90]), stats.sem(Gen1[102:105]), stats.sem(Gen1[117:120]),
       stats.sem(Gen1[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=2, col=4)

#######################################
# SampleNames 0.19 Generation 2
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen2[12:15]), stats.sem(Gen2[27:30]), stats.sem(Gen2[42:45]), stats.sem(Gen2[57:60]),
       stats.sem(Gen2[72:75]), stats.sem(Gen2[87:90]), stats.sem(Gen2[102:105]), stats.sem(Gen2[117:120]),
       stats.sem(Gen2[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=3, col=4)

#######################################
# SampleNames 0.19 Generation 3
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen3[12:15]), stats.sem(Gen3[27:30]), stats.sem(Gen3[42:45]), stats.sem(Gen3[57:60]),
       stats.sem(Gen3[72:75]), stats.sem(Gen3[87:90]), stats.sem(Gen3[102:105]), stats.sem(Gen3[117:120]),
       stats.sem(Gen3[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=4, col=4)

#######################################
# SampleNames 0.19 Generation 4
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen4[12:15]), stats.sem(Gen4[27:30]), stats.sem(Gen4[42:45]), stats.sem(Gen4[57:60]),
       stats.sem(Gen4[72:75]), stats.sem(Gen4[87:90]), stats.sem(Gen4[102:105]), stats.sem(Gen4[117:120]),
       stats.sem(Gen4[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=5, col=4)

#######################################
# SampleNames 0.19 Generation 5
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen5[12:15]), stats.sem(Gen5[27:30]), stats.sem(Gen5[42:45]), stats.sem(Gen5[57:60]),
       stats.sem(Gen5[72:75]), stats.sem(Gen5[87:90]), stats.sem(Gen5[102:105]), stats.sem(Gen5[117:120]),
       stats.sem(Gen5[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=6, col=4)

#######################################
# SampleNames 0.19 Generation 6
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen6[12:15]), stats.sem(Gen6[27:30]), stats.sem(Gen6[42:45]), stats.sem(Gen6[57:60]),
       stats.sem(Gen6[72:75]), stats.sem(Gen6[87:90]), stats.sem(Gen6[102:105]), stats.sem(Gen6[117:120]),
       stats.sem(Gen6[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=7, col=4)

#######################################
# SampleNames 0.19 Generation 7
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen7[12:15]), stats.sem(Gen7[27:30]), stats.sem(Gen7[42:45]), stats.sem(Gen7[57:60]),
       stats.sem(Gen7[72:75]), stats.sem(Gen7[87:90]), stats.sem(Gen7[102:105]), stats.sem(Gen7[117:120]),
       stats.sem(Gen7[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=8, col=4)

#######################################
# SampleNames 0.19 Generation 8
#######################################
fig.add_trace(go.Scatter(
    x = [timeTitle[0], timeTitle[1], timeTitle[2], timeTitle[3], timeTitle[4], timeTitle[5], timeTitle[6], timeTitle[7], timeTitle[8]],
    y=[stats.sem(Gen8[12:15]), stats.sem(Gen8[27:30]), stats.sem(Gen8[42:45]), stats.sem(Gen8[57:60]),
       stats.sem(Gen8[72:75]), stats.sem(Gen8[87:90]), stats.sem(Gen8[102:105]), stats.sem(Gen8[117:120]),
       stats.sem(Gen8[132:135])],
    showlegend = False,
    marker=dict(color="black", size=9, symbol="star-square"),
    mode="lines + markers",), row=9, col=4)

fig.update_xaxes(title_text="Generations", row=9, col=1)

fig.update_xaxes(title_text="Generations", row=1, col=1)
fig.update_xaxes(title_text="Generations", row=2, col=1)
fig.update_xaxes(title_text="Generations", row=9, col=3)
fig.update_xaxes(title_text="Time - Period", row=9, col=2)
fig.update_xaxes(title_text="Time - Period", row=1, col=2)
fig.update_xaxes(title_text="Time - Period", row=2, col=2)
fig.update_xaxes(title_text="Time - Period", row=9, col=4)

fig.update_yaxes(range=[0, 73000], row=1, col=1)
fig.update_yaxes(range=[0, 73000], row=2, col=1)
fig.update_yaxes(range=[0, 73000], row=3, col=1)
fig.update_yaxes(range=[0, 73000], row=4, col=1)
fig.update_yaxes(range=[0, 73000], row=5, col=1)
fig.update_yaxes(range=[0, 73000], row=6, col=1)
fig.update_yaxes(range=[0, 73000], row=7, col=1)
fig.update_yaxes(range=[0, 73000], row=8, col=1)
fig.update_yaxes(range=[0, 73000], row=9, col=1)

fig.update_yaxes(range=[0, 73000], row=1, col=2)
fig.update_yaxes(range=[0, 73000], row=2, col=2)
fig.update_yaxes(range=[0, 73000], row=3, col=2)
fig.update_yaxes(range=[0, 73000], row=4, col=2)
fig.update_yaxes(range=[0, 73000], row=5, col=2)
fig.update_yaxes(range=[0, 73000], row=6, col=2)
fig.update_yaxes(range=[0, 73000], row=7, col=2)
fig.update_yaxes(range=[0, 73000], row=8, col=2)
fig.update_yaxes(range=[0, 73000], row=9, col=2)

fig.update_yaxes(range=[0, 3300], row=1, col=3)
fig.update_yaxes(range=[0, 3300], row=2, col=3)
fig.update_yaxes(range=[0, 3300], row=3, col=3)
fig.update_yaxes(range=[0, 3300], row=4, col=3)
fig.update_yaxes(range=[0, 3300], row=5, col=3)
fig.update_yaxes(range=[0, 3300], row=6, col=3)
fig.update_yaxes(range=[0, 3300], row=7, col=3)
fig.update_yaxes(range=[0, 3300], row=8, col=3)
fig.update_yaxes(range=[0, 3300], row=9, col=3)

fig.update_yaxes(range=[0, 3300], row=1, col=4)
fig.update_yaxes(range=[0, 3300], row=2, col=4)
fig.update_yaxes(range=[0, 3300], row=3, col=4)
fig.update_yaxes(range=[0, 3300], row=4, col=4)
fig.update_yaxes(range=[0, 3300], row=5, col=4)
fig.update_yaxes(range=[0, 3300], row=6, col=4)
fig.update_yaxes(range=[0, 3300], row=7, col=4)
fig.update_yaxes(range=[0, 3300], row=8, col=4)
fig.update_yaxes(range=[0, 3300], row=9, col=4)
fig.update_yaxes(title_text="Generation Cells", row=4, col=1)
fig.update_yaxes(title_text="Generation Cells", row=1, col=1)
fig.update_yaxes(title_text="Generation Cells", row=2, col=1)
fig.update_yaxes(title_text="Cohort Number", row=4, col=3)
fig.update_yaxes(title_text="Cohort Number", row=4, col=4)

fig.update_layout(font_family="Courier New", font_color="blue", title_font_family="Times New Roman", title_font_color="red", legend_title_font_color="green", height=2000, width=1900, title={'text': "Modelling Immune Responses in Python"},)
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
