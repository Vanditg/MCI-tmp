import dash
import plotly.graph_objs as mid
import plotly.figure_factory as ff
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
trace=mid.Scatter(x=[0,13,25,50],
                  y=[0,0,0,0],
                  mode="lines,markers",
                  marker=dict(size=8,
                             color='blue',
                             line=dict(
                                    width=2,
                                    color="rgb(152,152,152)",
                                )
                             ),
                  line={"shape":"linear"}
                  )

trace1=mid.Scatter(x=[0,13,25,50],
                  y=[0,0,0,0],
                  mode="lines,markers",
                  marker=dict(size=8,
                             color='green',
                             line=dict(
                                    width=2,
                                    color="rgb(152,152,152)",
                                )
                             ),
                  line={"shape":"linear"}
                  )

trace2=mid.Scatter(x=[0,13,25,50],
                  y=[0,0,0,0],
                  mode="lines,markers",
                  marker=dict(size=8,
                             color='red',
                             line=dict(
                                    width=2,
                                    color="rgb(152,152,152)",
                                )
                             ),
                  line={"shape":"linear"}
                  )

trace3=mid.Scatter(x=[0,13,25,50],
                  y=[0,0,0,0],
                  mode="lines,markers",
                  marker=dict(size=8,
                             color='yellow',
                             line=dict(
                                    width=2,
                                    color="rgb(152,152,152)",
                                )
                             ),
                  line={"shape":"linear"}
                  )

gen0 = mid.Figure(trace)
gen1 = mid.Figure(trace1)
gen2 = mid.Figure(trace2)
gen3 = mid.Figure(trace3)

app.layout=html.Div(
    children=[
        html.Div(
            children=[
                dcc.Slider(
                    id="N",
                    min=1,
                    max=8,
                    marks={i:"1000 cells" if i==1 else str((i)*1000) for i in range(1,9)},
                    value=1
                )
            ],style={'columnCount':2}
        ),
        html.Div(
            children=[
                dcc.Slider(
                    id="T1",
                    min=1,
                    max=24,
                    marks={i:"1 hours" if i==1 else str(i) for i in range(1,24)},
                    value=12,
                )
            ],style={'columnCount':1}
        ),
        html.Div(
            children=[
                dcc.Slider(
                    id="Ts",
                    min=1,
                    max=24,
                    marks={i:"1 hours" if i==1 else str(i) for i in range(1,24)},
                    value=6,
                )
            ],style={'columnCount':1}
        ),
        html.Div(
            children=[
                dcc.Slider(
                    id="Td",
                    min=1,
                    max=50,
                    marks={i:"1 hours" if i==1 else str(i) for i in range(1,51)},
                    value=48,
                )
            ],style={'columnCount':1}
        ),
        html.Div(
            children=[
                dcc.Dropdown(
                    id="generation",
                    options=[
                        {'label':'generation 0','value':'generation 0'},
                        {'label':'generation 1','value':'generation 1'},
                        {'label':'generation 2','value':'generation 2'},
                        {'label':'generation 3','value':'generation 3'},
                    ],
                    placeholder="choice",
                    value="generation 0",
                )
            ], style={"display": "inline-block", "width": '200px', "height": "200px", "position": "absolute","left": "40px", "top": "200px"},
        ),
        html.Div(
            children=[
                html.H2("the generation cell number"),
                dcc.Graph(
                    id='table_test1',
                )
            ],style={"left": "350px", "top": "1000px"}
        )
    ]
)

@app.callback(Output('table_test1','figure'),[Input('N','value')],[Input('T1','value')],[Input('Ts','value')],[Input('Td','value')],[Input('generation','value')])
def update_table(N,T1,Ts,Td,choice):
    print(N)
    print(T1)
    print(Ts)
    print(Td)
    numcellS=N*1000
    Firdiv=T1
    Subdiv=Ts
    Deatim=Td
    time=0
    generat=0
    for i in range(0,Deatim):
        if Firdiv>time:
            if time==0:
                gen0['data'][0]['y']=(str(numcellS),)+(0,)+gen0['data'][0]['y'][generat+2:]
                gen0['data'][0]['x'] =(0,)+(str(Firdiv),)+gen0['data'][0]['x'][generat+2:]

            time=time+1
        else:
            if time==Firdiv:
                generat=generat+1
                gen1['data'][0]['x']=gen1['data'][0]['x'][:generat]+(str(Firdiv),)+gen1['data'][0]['x'][generat+1:]
                gen1['data'][0]['y']=gen1['data'][0]['y'][:generat]+(str(numcellS*2),)+gen1['data'][0]['y'][generat+1:]
                gen1['data'][0]['x'] = gen1['data'][0]['x'][:generat+1] + (str(Firdiv+Subdiv),) + gen1['data'][0]['x'][generat + 2:]
                time = time + 1
            else:
                for j in range(time,Deatim):

                    if time==Firdiv+Subdiv :
                        numcellS=numcellS*2
                        generat=generat+1
                        if time==Firdiv+Subdiv:
                            if int(gen2['data'][0]['x'][-1])>=Deatim:
                                gen2['data'][0]['x'] = gen2['data'][0]['x'][:generat - 1] + (str(Firdiv),) + (str(Firdiv + Subdiv),)+ (str(Firdiv + 2*Subdiv),) + ((Deatim),)
                                gen2['data'][0]['y'] = gen2['data'][0]['y'][:generat] + (str(numcellS * 2),) + (0,)+(0,)
                            else:
                                gen2['data'][0]['x'] = gen2['data'][0]['x'][:generat-1] + (str(Firdiv),) +(str(Firdiv+Subdiv),) + gen2['data'][0]['x'][generat + 1:]+((Deatim),)
                                gen2['data'][0]['y']=gen2['data'][0]['y'][:generat]+(str(numcellS*2),)+gen2['data'][0]['y'][generat+1:]+ (0,)

                            print(gen2)
                            #time = time + 1

                    else:
                        if time == Firdiv+2*Subdiv:
                            if Firdiv+3*Subdiv<=Deatim:
                                gen3['data'][0]['x']=gen3['data'][0]['x'][:generat-1]+(str(Firdiv + Subdiv),)+(str(Firdiv + Subdiv*2),)+(str(Firdiv + Subdiv*3),)+((Deatim),)
                                generat = generat + 1
                                numcellS = numcellS * 2
                                gen3['data'][0]['y'] = gen3['data'][0]['y'][:generat-1]+(str(numcellS*2),)+(0,)+(0,)
                            

                    time=time+1


    print(choice)
    if choice!='choice':
         if choice=='generation 0':
            return gen0
         else:
            if choice=='generation 1':
                return gen1
            else:
                 if choice=='generation 2':
                    return gen2
                 else :
                    if choice=='generation 3':
                        return gen3

if __name__ == '__main__':
  app.run_server(debug=True)
