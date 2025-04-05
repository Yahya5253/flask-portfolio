from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/gold-analysis')
def gold_analysis():
    return "<h2>Gold Analysis Project Page Coming Soon!</h2>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/projects/gold_price')
def gold_price():
    return render_template('projects/gold_price.html')
