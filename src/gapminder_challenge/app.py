from flask import Flask, render_template
from dashboard import dash_app1, dash_app2, dash_app3, dash_app4




app = Flask(__name__)
app = dash_app1.add_dash(app)
app = dash_app2.add_dash(app)
app = dash_app3.add_dash(app)
app = dash_app4.add_dash(app)



@app.route('/')

def index():
    return render_template('index.html', app1=dash_app1.url, app2=dash_app2.url, app3=dash_app3.url,
    app4=dash_app4.url)

