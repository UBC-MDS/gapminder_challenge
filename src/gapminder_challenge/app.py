from flask import Flask, render_template
from dashboard import dash_app1, dash_app2


app = Flask(__name__)
app = dash_app1.add_dash(app)
app = dash_app2.add_dash(app)


@app.route('/')
def hello():
    return render_template('index.html', app1=dash_app1.url, app2=dash_app2.url)
