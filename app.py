import pandas as pd
from flask import Flask, render_template, request
from twitter_scraper import process_data
from twitter_analytics import process_analytics

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/process_form", methods=['POST'])
def process_form():
    input_search = request.form.get('input_search')
    input_max_tweets = request.form.get('input_max_tweets')
    input_date_init = request.form.get('input_date_init')
    input_date_end = request.form.get('input_date_end')

    process_data(input_search, input_max_tweets, input_date_init, input_date_end)

    return render_template("statistics.html")


@app.route("/statistics", methods=['GET'])
def statistics():
    df = pd.read_csv(r'dataframe/df_tweets.csv')
    process_analytics(df)
    # render in /statistics.html images produced by statis analytics: get dataframe and make plots
    return render_template("statistics.html")


@app.route("/process_form", methods=['POST'])
def analytics_form():
    input_word = request.form.get('input_word')
    process_data(input_word)
    return render_template("statistics.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
