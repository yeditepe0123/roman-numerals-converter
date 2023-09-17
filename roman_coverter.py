from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Roman numeral conversion function
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral

# Route for the index page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if re.match("^[1-9][0-9]{0,3}$", user_input):
            num = int(user_input)
            if 1 <= num <= 3999:
                roman_numeral = int_to_roman(num)
                return render_template("result.html", num=num, roman_numeral=roman_numeral)
        return render_template("index.html", not_valid=True)
    return render_template("index.html", not_valid=False)

if __name__ == "__main__":
    app.run(debug=True)
