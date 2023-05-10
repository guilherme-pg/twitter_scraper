from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/process_form", methods=['POST'])
def process_form():
    input_name = request.form.get('input_name')
    input_word = request.form.get('input_word')
    input_date_init = request.form.get('input_date_init')
    input_date_end = request.form.get('input_date_end')
    return "Data received"


@app.route("/statistics", methods=['GET'])
def home():
    return render_template("statistics.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
