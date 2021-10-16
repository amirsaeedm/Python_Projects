import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_split_pane
import plotly.express as px
import pandas as pd
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
 
if __name__ == '__main__':
   app.run_server(debug=True)


# app.layout = html.Div(
# 	children=[
#    	html.H1(children='World Marathon Analysis',
#     style={'textAlign': 'center'}),
  
#    dash_split_pane.DashSplitPane(
#    	   children=[
  
# 	   html.Div(children=[
# 	        html.H1(children='Settings', style={'textAlign': 'center'}),
# 	           ], style={'margin-left': '50%', 'verticalAlign': 'middle'}),
# 	   html.Div(children=[
# 	        html.H1(children='Graph View', style={'textAlign': 'center'}),
# 	            ])
# 	   ],
#    id="splitter",
#    split="vertical",
#    size=1000,
# ) 
# ])



def convert_to_time(time_in_some_format):
   time_obj =  datetime.strptime(time_in_some_format, '%H:%M:%S').time()
   return time_obj
 
def get_data():
  df = pd.read_csv('world_marathon_majors.csv', engine="python")
  df['time'] = df['time'].apply(convert_to_time)
  return df



app.layout = html.Div(children=[
   html.H1(children='World Marathon Analysis',
    style={'textAlign': 'center'}),
  
   dash_split_pane.DashSplitPane(
   children=[
  
   html.Div(children=[
        html.H1(children='Settings', style={'textAlign': 'center'}),
        dcc.Dropdown(id='dropdown-menu', options=[{'label':x, 'value': x} for x in range(df['year'].min(), df['year'].max()+1)],
         value=df['year'].max(),
         style={'width': '220px','font-size': '90%','height': '40px',}
        )
    ], style={'margin-left': '50%', 'verticalAlign': 'middle'}),
   html.Div(children=[
        html.H1(children='Graph View', style={'textAlign': 'center'}),
        dcc.Graph( id='input-graph',figure=get_default_data())
    ]) 
   ],
   id="splitter",
   split="vertical",
   size=1000,
)
])



@app.callback(
   dash.dependencies.Output('input-graph', 'figure'),
   [dash.dependencies.Input('dropdown-menu', 'value')]
)
def update_output_div(value):
   test_sample = df[df['year'] == value]
   test_sample = test_sample.groupby('country')['time'].min().reset_index()
   tt = test_sample.sort_values(by=['time'])
   fig = px.bar(tt, y='country', x='time', orientation='h', hover_data=["time"], )
   return fig