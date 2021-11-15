from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def test():
    if request.method == 'POST':
        resp = request.form
        fetch_name = str(resp.get('fetch'))
        return render_template('result.html', name="Name is {}".format(fetch_name))

if __name__ == "__main__":
    app.run(debug=True)
