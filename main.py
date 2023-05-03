from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [f"film{x}" for x in range(10)]
    return render_template("homepage.html", movies=movies)

if __name__ == "__main__":
    app.run()