import plotly.express as px
import pandas as pd
import plotly
import json
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
        df = pd.read_csv('book1.csv')
        fig = px.scatter_mapbox(df, lat="LATITUDE", lon="LONGITUDE", hover_name="PLACE",
                                hover_data=["TIME", "OCCURRANCE DATE", "ROAD", "ACCIDENT TYPE", "WEATHER"],
                                color_discrete_sequence=["fuchsia"], zoom=3, height=600)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('s.html', graphJSON=graphJSON)
app.run(debug=True)