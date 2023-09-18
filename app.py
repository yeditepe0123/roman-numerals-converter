from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_roman(decimal_num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    num_to_roman = ''

    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while decimal_num >= value:
            num_to_roman += numeral
            decimal_num -= value

    return num_to_roman

@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        if not alpha.isdecimal():
            return render_template('index.html', developer_name='osvaldo', not_valid=True)
        number = int(alpha)
        if not 0 < number < 4000:
            return render_template('index.html', developer_name='osvaldo', not_valid=True)
        return render_template('result.html', number_decimal=number, number_roman=convert_to_roman(number), developer_name='osvaldo')
    else:
        return render_template('index.html', developer_name='osvaldo', not_valid=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
