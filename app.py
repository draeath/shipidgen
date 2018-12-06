import random
import string
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_ship_id():
    return render_template('id_gen.html', ship_prefix=get_alpha_string(2), ship_suffix=get_digit_string(4))


def get_alpha_string(num: int) -> str:
    out = ''
    for i in range(abs(num)):
        out += random.choice(string.ascii_uppercase)
    return out


def get_digit_string(num: int) -> str:
    out = ''
    for i in range(abs(num)):
        out += random.choice(string.digits)
    return out


if __name__ == '__main__':
    random.seed()
    app.run(debug = True)
