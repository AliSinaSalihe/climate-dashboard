from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/forecasts")
def forecasts():
    return render_template("forecasts.html")

@app.route("/historical")
def historical():
    return render_template("historical.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

if __name__ == "__main__":
    app.run(debug=True)
