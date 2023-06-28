import pandas as pd
from dash import Dash, dcc, html
from data.util import get_data
from layout import create_layout
import os

PATH = os.path.join(os.getcwd(), "data/avocado.csv")


data = get_data(PATH)
app = Dash()
app.layout = create_layout(app,data)


if __name__ == "__main__":
    app.run_server(debug=True)