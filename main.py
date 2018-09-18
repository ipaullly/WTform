from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gkb902#@9op2t'

@app.route('/', methods=['GET', 'POST'])
def index():
    return ''

if __name__ == '__main__':
    app.run(debug=True)