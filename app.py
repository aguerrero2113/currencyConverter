from flask import Flask, render_template, request

from backend.helper_functions import currency_converter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            input_currency = request.form.get('input_currency')
            output_currency = request.form.get('output_currency')
            amount = float(request.form.get('amount')
                           if request.form.get('amount') else 0)
            input = {
                'input_currency': input_currency,
                'output_currency': output_currency,
                'amount': amount
            }
            output = currency_converter(
                input_currency=input_currency, output_currency=output_currency, amount=amount)
            return render_template('index.html', input=input, output=output)
    except Exception as error:
        print("############################ ERROR ############################")
        print(error)
        print("###############################################################")
    return render_template('index.html')
