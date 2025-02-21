from flask import Flask, render_template


app = Flask(__name__)

app.debug = True

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/templates/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")