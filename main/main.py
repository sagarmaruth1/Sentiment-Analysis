from flask import Flask,render_template, request
import pickle

file = open('./model_pickle', 'rb')
model = pickle.load(file)
file.close()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./Index_ip.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    review = [request.form['sentiment']]

    rating = model.predict(review)

    return render_template("./Index_op.html", sentiment=str(review)[1:-1], result=str(rating)[1:-1])


if __name__ == "__main__":
    app.run(debug=True)
