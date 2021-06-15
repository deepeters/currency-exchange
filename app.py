from flask import Flask, render_template, request, url_for, flash, redirect
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret_key"

currencys = ['ALL', 'XCD', 'EUR', 'BBD', 'BTN', 'BND', 'XAF', 'CUP', 'USD', 'FKP', 'GIP', 'HUF', 'IRR', 'JMD', 'AUD', 'LAK', 'LYD', 'MKD', 'XOF', 'NZD', 'OMR', 'PGK', 'RWF', 'WST', 'RSD', 'SEK', 'TZS', 'AMD', 'BSD', 'BAM', 'CVE', 'CNY', 'CRC', 'CZK', 'ERN', 'GEL', 'HTG', 'INR', 'JOD', 'KRW', 'LBP', 'MWK', 'MRO', 'MZN', 'ANG', 'PEN', 'QAR', 'STD', 'SLL', 'SOS', 'SDG', 'SYP', 'AOA', 'AWG', 'BHD', 'BZD', 'BWP', 'BIF', 'KYD', 'COP', 'DKK', 'GTQ', 'HNL', 'IDR', 'ILS', 'KZT', 'KWD', 'LSL', 'MYR', 'MUR', 'MNT', 'MMK', 'NGN', 'PAB', 'PHP', 'RON', 'SAR', 'SGD', 'ZAR', 'SRD', 'TWD', 'TOP', 'VEF', 'DZD', 'ARS', 'AZN', 'BYR', 'BOB', 'BGN', 'CAD', 'CLP', 'CDF', 'DOP', 'FJD', 'GMD', 'GYD', 'ISK', 'IQD', 'JPY', 'KPW', 'LVL', 'CHF', 'MGA', 'MDL', 'MAD', 'NPR', 'NIO', 'PKR', 'PYG', 'SHP', 'SCR', 'SBD', 'LKR', 'THB', 'TRY', 'AED', 'VUV', 'YER', 'AFN', 'BDT', 'BRL', 'KHR', 'KMF', 'HRK', 'DJF', 'EGP', 'ETB', 'XPF', 'GHS', 'GNF', 'HKD', 'XDR', 'KES', 'KGS', 'LRD', 'MOP', 'MVR', 'MXN', 'NAD', 'NOK', 'PLN', 'RUB', 'SZL', 'TJS', 'TTD', 'UGX', 'UYU', 'VND', 'TND', 'UAH', 'UZS', 'TMT', 'GBP', 'ZMW', 'BTC', 'BYN', 'BMD', 'GGP', 'CLF', 'CUC', 'IMP', 'JEP', 'SVC', 'ZMK', 'XAG', 'ZWL']

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        API = os.environ.get("CURR_API")
        fromCurr = request.form.get('fromCurr')
        toCurr = request.form.get('toCurr')
        if fromCurr and toCurr:
            try:
                url = f"https://free.currconv.com/api/v7/convert?q={fromCurr}_{toCurr}&compact=ultra&apiKey=385fcd73db41fdffd372"
                rates = requests.get(url).json()[f'{fromCurr}_{toCurr}']
                return render_template('index.html', currency=currencys, result=f"{rates} {toCurr}")
            except:
                flash("Error Occured", 'danger')
                return redirect(url_for('index'))
        else:
            flash("Error Occured", 'danger')
            return redirect(url_for('index'))

    return render_template('index.html', currency=currencys)

if __name__ == "__main__":
    app.run(debug=True)