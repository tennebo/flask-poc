#!/usr/bin/env python3
"""My web service.

This module is a REST web service.

To run the app:
    $ python service.py
"""

import os

from flask import Flask, Response
from flask_jsonpify import jsonify
from flask_restful import Api

from jsonencoder import IsoJSONEncoder


app = Flask(__name__)


@app.route("/test", methods=['GET'])
def get() -> Response:
    """For smoke testing: Return a JSON message."""
    return jsonify(message='Yes we can!')


def to_bool(bool_str):
    """Parse a boolean environment variable."""
    return bool_str.lower() in ("yes", "true", "1")


def main():
    """Entry point."""
    app.json_encoder = IsoJSONEncoder

    api = Api(app)

    debug = to_bool(os.environ.get('DEBUG', 'False'))
    host = os.environ.get('HOST', 'localhost')
    port = int(os.environ.get('PORT', 8080))

    # From the Flask doc:
    #   While lightweight and easy to use, Flask's built-in server is not suitable for production
    #   as it doesn't scale well and by default serves only one request at a time.
    app.run(host=host, debug=debug, port=port)


if __name__ == '__main__':
    main()
