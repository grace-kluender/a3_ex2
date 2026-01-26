from flask import Flask, Response, jsonify, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    data = {
            "available_endpoints": {
                "/uppercase/<text>":
                    "Returns an uppercase version of the <text> "
                    "from the URL path"
                ,
                "/lowercase/<text>":
                    "Returns a lowercase version of the <text> "
                    "from the URL path"
                ,
                "/charcount/<text>":
                    "Returns the character count from the <text> "
                    "from the URL path"
            }
        }
    return Response(
        json.dumps(data, indent=2),
        mimetype="application/json",
    )


@app.route("/uppercase/<text>", methods=['GET'])
def uppercase(text):
    """
    Returns an uppercase version of the text from the URL path
    """
    return jsonify(text.upper())

@app.route("/lowercase/<text>", methods=['GET'])
def lowercase(text):
    """
    Returns a lowercase version of the text from the URL path
    """
    return jsonify(text.lower())

@app.route("/charcount/<text>", methods=['GET'])
def charactercount(text):
    """
    Returns the character count from the text in the URL path, excluding spaces
    """
    count = 0
    for char in text:
        if char != ' ':
            count += 1

    return jsonify(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)