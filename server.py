from flask import Flask, render_template
from pip import main

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')

@app.route("/slider")
def slider():
    return render_template('slider.html')

if __name__ == "__main__":
    app.run(debug=True)