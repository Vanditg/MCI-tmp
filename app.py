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

top_markdown_text = '''
This is my first deployed app
'''
app.layout = html.Div([

    dcc.Markdown(children=top_markdown_text),

])
      
#Main method
if __name__=='__main__':
    app.run_server(debug=True)
