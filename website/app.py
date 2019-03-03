from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")
if __name__ == "__main__":
    app.run()

@app.route("/About")
def about():
    return render_template("About.html")
