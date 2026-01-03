import dash
from dash import html, dcc, Input, Output
import plotly.express as px

def dashboard_visualization(df):
    app = dash.Dash(__name__)

    numeric_cols = df.select_dtypes(include='number').columns

    options = [
        {"label": col, "value": col} for col in numeric_cols
    ]

    app.layout = html.Div([
        html.H1("Interactive Dashboard"),

        html.Label("Select Column"),
        dcc.Dropdown(
            id="col",
            options=options,
            value=numeric_cols[0]
        ),

        dcc.Graph(id="graph")
    ])

    @app.callback(
        Output("graph", "figure"),
        Input("col", "value")
    )
    def update_graph(selected_col):
        fig = px.bar(
            df.head(20),
            x=df.head(20).index,
            y=selected_col,
            title=f"{selected_col} Visualization"
        )
        return fig

    return app  
