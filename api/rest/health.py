from flask import jsonify


def hi():
    return jsonify({'okay':True})
