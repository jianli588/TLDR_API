import algorithm
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    output = request.form.to_dict()
    print(output["url-input"])
    website_url = output["url-input"]

    shortened_text = algorithm.run(website_url)
    sentence_list = []
    for text in shortened_text:
        sentence_list.append(text[0])
    return render_template("index.html", sentence_list=sentence_list)

if(__name__ == '__main__'):
    app.run()









