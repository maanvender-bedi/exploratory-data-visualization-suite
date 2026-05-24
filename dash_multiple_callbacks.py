import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Multiple Callbacks Example"),
    dcc.Dropdown(
        id="continent-dropdown",
        options=[{"label": c, "value": c} for c in df["continent"].unique()],
        value="Asia"
    ),
    dcc.Slider(
        id="year-slider",
        min=df["year"].min(),
        max=df["year"].max(),
        value=2007,
        marks={str(y): str(y) for y in df["year"].unique()},
        step=None
    ),
    dcc.Graph(id="scatter-graph"),
    dcc.Graph(id="bar-graph")
])

@app.callback(
    [Output("scatter-graph", "figure"),
     Output("bar-graph", "figure")],
    [Input("continent-dropdown", "value"),
     Input("year-slider", "value")]
)
def update_graphs(continent, year):
    filtered = df[(df["continent"] == continent) & (df["year"] == year)]
    scatter = px.scatter(filtered, x="gdpPercap", y="lifeExp", size="pop", color="country",
                         hover_name="country", title=f"Life Expectancy vs GDP ({continent}, {year})")
    bar = px.bar(filtered, x="country", y="pop", color="country",
                 title=f"Population by Country ({continent}, {year})")
    return scatter, bar

if __name__ == "__main__":
    app.run(debug=True)