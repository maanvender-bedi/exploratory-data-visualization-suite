import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Single Callback Example"),
    dcc.Dropdown(
        id="continent-dropdown",
        options=[{"label": c, "value": c} for c in df["continent"].unique()],
        value="Asia"
    ),
    dcc.Graph(id="life-exp-graph")
])

@app.callback(
    Output("life-exp-graph", "figure"),
    Input("continent-dropdown", "value")
)
def update_graph(continent):
    filtered = df[df["continent"] == continent]
    fig = px.line(filtered, x="year", y="lifeExp", color="country", title=f"Life Expectancy in {continent}")
    return fig

if __name__ == "__main__":
    app.run(debug=True)