from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bill_calculator():
    total_price = None

    if request.method == 'POST':
        xray_price = float(request.form['xray_price'])
        blood_test_price = float(request.form['blood_test_price'])
        total_price = xray_price + blood_test_price
    return render_template('index.html', total_price=total_price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

