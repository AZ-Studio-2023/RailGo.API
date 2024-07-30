from bottle import Bottle

app = Bottle()


@app.route("/info")
def train_info():
    return "info"
