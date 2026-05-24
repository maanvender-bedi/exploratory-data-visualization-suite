import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Graph Interaction Example"),
    dcc.Graph(id="main-graph",
              figure=px.scatter(df[df["year"] == 2007],
                                x="gdpPercap", y="lifeExp",
                                color="continent", hover_name="country")),
    dcc.Graph(id="detail-graph")
])

@app.callback(
    Output("detail-graph", "figure"),
    Input("main-graph", "clickData")
)
def update_detail(clickData):
    if clickData is None:
        return px.line(df[df["country"] == "India"], x="year", y="lifeExp", title="Default: India")
    country = clickData["points"][0]["hovertext"]
    filtered = df[df["country"] == country]
    return px.line(filtered, x="year", y="lifeExp", title=f"Life Expectancy of {country}")

if __name__ == "__main__":
    app.run(debug=True)