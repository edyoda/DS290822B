# pip install Flask

from flask import Flask

app = Flask(__name__)

@app.route("/edyoda")
def fun():
    return {"name":"Bharati"}

if __name__ == "__main__":
    app.run()