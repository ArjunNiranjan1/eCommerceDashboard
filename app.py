from dash import Dash, html, dcc
from dash_bootstrap_components.themes import CYBORG
import plotly.express as px
import pandas as pd

def main() -> None:
    app = Dash(external_stylesheets=[CYBORG])
    
    app.title = "Transactions Dashboard"
    app.layout = html.Div(children=[html.H2(children="Business Transactions Analysis"),html.Hr()])
    
    app.run()

if __name__ == "__main__":
    main()