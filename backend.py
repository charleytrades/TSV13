from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")


def run():
    app.run(host="0.0.0.0", port=8002)


if __name__ == "__main__":
    run()
