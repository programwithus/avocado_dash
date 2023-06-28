from dash import html, dcc 

def create_layout(app, data):
    return html.Div(
            [
                html.H1("Avocado Analytics"),
                html.P("Analyze the behavior of avocado prices and the number"
               " of avocados sold in the US between 2015 and 2018"),
            dcc.Graph(
                figure={
                "data": [
                        {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                         "type": "lines",
                        },
                    ],
                        "layout": {"title": "Average Price of Avocados"},
                 },
            ),
            dcc.Graph(
                figure={
                "data": [
                {
                "x": data["Date"],
                "y": data["Total Volume"],
                "type": "lines",
                },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)