from flask import Flask

app = Flask(__name__)
app.config


@app.route("/devices", methods=["GET"])
def get_all_devices():
    pass


@app.route("/devices", methods=["POST"])
def add_new_device():
    pass


if __name__ == "__main__":
    app.run(debug=True)
