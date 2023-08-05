import dash
from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div('hello heyhey')

if __name__ =='__main__':
    app.run(debug=True)

