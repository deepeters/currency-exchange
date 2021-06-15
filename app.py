from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    """API = os.environ.get("CURR_API")
    fromCurr = "USD"
    toCurr = "KES"
    url = f"https://free.currconv.com/api/v7/convert?q={fromCurr}_{toCurr}&compact=ultra&apiKey=385fcd73db41fdffd372"
    rates = requests.get(url).json()"""
    if request.method == "POST":
        return ""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)